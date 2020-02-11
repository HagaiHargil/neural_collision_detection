"""
Aggregation of tools to analyze the graphs generated by
'graph_parsing.py'.
"""
import pathlib
import multiprocessing as mp
import itertools

import attr
from attr.validators import instance_of
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import numba

from ncd_post_process.graph_parsing import CollisionNode


plt.rcParams.update({"font.size": 22})
neuron_names = {
    # "AP120410_s1c1": "V",
    # "AP120410_s3c1": "V",
    # "AP120412_s3c2": "V",
    # "AP120416_s3c1": "IV",
    # "AP120419_s1c1": "VI",
    # "AP120420_s1c1": "IV",
    # "AP120420_s2c1": "II/II",
    "AP120507_s3c1": "II/II",
    # "AP120510_s1c1": "II/II",
    # "AP120522_s3c1": "I",
    # "AP120524_s2c1": "II/II",
    # "AP120614_s1c2": "V",
    # "AP130312_s1c1": "II/II",
    "AP131105_s1c1": "II/II",
}


@attr.s
class CollisionsDistNaive:
    """Calculate and plot the collision counts as a function of
    the topological distance of the neuron. This class is "naive" since it doesn't
    interpolate the neural coordinates, it uses the raw output from the
    Neurolucida files as its input.

    To use it, run the "run" method to first create the necessary data structures.
    The "plot_all()" method can show the data and write it to disk.

    Parameters
    ----------
    graph : nx.Graph
        A parsed graph that was generated by networkx and ``NeuronToGraph`` in
        ``graph_parsing.py``.
    neuron_name : str
        The label of the neuron
    normalize_collisions_by : int
        Number of possible locations that the neuron could've been in. This factor turns
        the number of collisions into the probability of collision.
    """

    graph = attr.ib(validator=instance_of(nx.Graph))
    neuron_name = attr.ib(default="neuron", validator=instance_of(str))
    normalize_collisions_by = attr.ib(default=100_000, validator=instance_of(int))
    results_folder = attr.ib(
        default=pathlib.Path("/data/neural_collision_detection/results/2019_2_10")
    )
    num_of_nodes = attr.ib(init=False)
    parsed_axon = attr.ib(init=False)
    parsed_dend = attr.ib(init=False)
    labels_and_colors = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.num_of_nodes = self.graph.number_of_nodes()
        coll_ax = np.zeros(self.num_of_nodes, dtype=np.uint64)
        coll_dend = coll_ax.copy()
        dist_ax = np.zeros(self.num_of_nodes, dtype=np.float64)
        dist_dend = dist_ax.copy()
        self.parsed_axon = pd.DataFrame(
            {"coll": coll_ax, "dist": dist_ax, "x": dist_ax, "y": dist_ax, "z": dist_ax}
        )
        self.parsed_dend = pd.DataFrame(
            {
                "coll": coll_dend,
                "dist": dist_dend,
                "x": dist_dend,
                "y": dist_dend,
                "z": dist_dend,
            }
        )
        self.labels_and_colors = {
            "axon": ("C2", "Axonal", "Greens"),
            "dend": ("C1", "Dendritic", "Oranges"),
        }

    @classmethod
    def from_graph(cls, fname: pathlib.Path, neuron: str, **kwargs):
        """Instantiate from an existing graph file by deserializing it."""
        try:
            graph = nx.readwrite.gml.read_gml(
                str(fname), destringizer=CollisionNode.from_str
            )
        except FileNotFoundError:
            raise
        else:
            return cls(graph, neuron, **kwargs)

    def run(self):
        """Run analysis pipeline."""
        self._populate_collisions()
        self.parsed_axon["coll_normed"] = self._normalize_by_density(self.parsed_axon)
        self.parsed_dend["coll_normed"] = self._normalize_by_density(self.parsed_dend)

    def _populate_collisions(self):
        """Traverse a specific graph and find the number of
        collisions in it as a function of the topological distance
        from the cell body.
        """
        idx_axon, idx_dend = 0, 0
        for node in self.graph.nodes():
            if node.tree_type == "Axon":
                self.parsed_axon.loc[idx_axon, "coll"] = (
                    node.collisions / self.normalize_collisions_by
                )
                self.parsed_axon.loc[idx_axon, "dist"] = node.dist_to_body
                self.parsed_axon.loc[idx_axon, "x":"z"] = node.loc
                idx_axon += 1
            else:
                self.parsed_dend.loc[idx_dend, "coll"] = (
                    node.collisions / self.normalize_collisions_by
                )
                self.parsed_dend.loc[idx_dend, "dist"] = node.dist_to_body
                self.parsed_dend.loc[idx_dend, "x":"z"] = node.loc
                idx_dend += 1

        self.parsed_axon = self.parsed_axon.loc[:idx_axon, :]
        self.parsed_dend = self.parsed_dend.loc[:idx_dend, :]

    def _normalize_by_density(self, data):
        """Takes the parsed graph data and normalizes the collision counts by the
        neural density at that distance, since the more neuron there is the more likely
        it is for it to encounter blood vessels. This function actually returns the chance
        for a (normalized) collision, since it also divided the result by the number of
        NCD iterations.
        """
        dist_int = data["dist"].to_numpy().astype(np.int64)
        bincounts = np.bincount(dist_int, minlength=dist_int.max())
        normed = norm_colls(bincounts, dist_int, data["coll"].to_numpy())
        return normed

    def plot_all_jointplots(self):
        """Small wrapper for plotting the full jointplot of
        all cells and both axons and dendrites."""
        for data, neurite in zip(
            (self.parsed_axon, self.parsed_dend), ("axon", "dend")
        ):
            self._plot_jointplot(data, neurite, with_norm=False)
            self._plot_jointplot(data, neurite, with_norm=True)

    def plot_all_hexbins(self):
        """Small wrapper for plotting the only the hexbin
        all cells and both axons and dendrites."""
        for data, neurite in zip(
            (self.parsed_axon, self.parsed_dend), ("axon", "dend")
        ):
            self._plot_hexbin(data, neurite, with_norm=True)

    def scatter(self):
        """Scatter the axon and dendrite collisions"""
        fig, ax = plt.subplots()
        ax.scatter(
            self.parsed_axon["dist"], self.parsed_axon["coll"], c="C2", s=0.3, alpha=0.5
        )
        ax.scatter(
            self.parsed_dend["dist"], self.parsed_dend["coll"], c="C1", s=0.3, alpha=0.5
        )
        self._format_scatter_plot(ax)
        fig, ax = plt.subplots()
        ax.scatter(
            self.parsed_axon["dist"],
            self.parsed_axon["coll_normed"],
            c="C2",
            s=0.3,
            alpha=0.5,
        )
        ax.scatter(
            self.parsed_dend["dist"],
            self.parsed_dend["coll_normed"],
            c="C1",
            s=0.3,
            alpha=0.5,
        )
        self._format_scatter_plot(ax, "_normed")

    def _format_scatter_plot(self, ax, normed=""):
        ax.set_title(f"Collisions vs topodist {self.neuron_name}")
        ax.set_ylabel("Collisions" if normed == "" else "P(Collisions)")
        ax.set_xlabel("Topodist [um]")
        ax.figure.savefig(
            self.results_folder / f"colls_dist{normed}_{self.neuron_name}.png",
            transparent=True,
            dpi=300,
        )

    def _plot_jointplot(self, data, neurite, with_norm=False, window_size=30):
        """Creates a jointplot with hexagons which show the probability of collision
        as a function of the topological distance from the soma.
        """
        new_ycol_name = f"{self.labels_and_colors[neurite][1]} chance for collision"
        data = data.copy().rename(
            {
                "dist": "Length of branch [um]",
                "coll": new_ycol_name,
                "coll_normed": f"{new_ycol_name} (normalized)",
            },
            axis=1,
        )
        if with_norm:
            y_col = new_ycol_name + " (normalized)"
            fname = f"results/for_article/fig2/{self.neuron_name}_colls_vs_dist_jointplot_normed_{neurite}.png"
        else:
            y_col = new_ycol_name
            fname = f"results/for_article/fig2/{self.neuron_name}_colls_vs_dist_jointplot_no_normed_{neurite}.png"

        ax = sns.jointplot(
            "Length of branch [um]",
            y_col,
            data=data,
            kind="hex",
            height=8,
            color=self.labels_and_colors[neurite][0],
        )
        plt.subplots_adjust(left=0.11)
        data_sorted = data.sort_values(["Length of branch [um]"])
        avg_x_data = data_sorted["Length of branch [um]"]
        avg_y_data = data_sorted[y_col].rolling(window_size).mean()
        ax.ax_joint.plot(avg_x_data, avg_y_data, c="k", alpha=0.3)
        ax.savefig(
            fname, transparent=True, dpi=300,
        )

    def _plot_hexbin(self, data, neurite, with_norm=False):
        """Plots a hexbin plot of the data."""
        new_ycol_name = f"{self.labels_and_colors[neurite][1]} chance for collision"
        data = data.copy().rename(
            {
                "dist": "Length of branch [um]",
                "coll": new_ycol_name,
                "coll_normed": f"{new_ycol_name} (normalized)",
            },
            axis=1,
        )
        if with_norm:
            y_col = new_ycol_name + " (normalized)"
            normed = "normed"
        else:
            y_col = new_ycol_name
            normed = "not_normed"

        x = data["Length of branch [um]"]
        y = data[y_col]
        ymin = 0
        ymax = max(y.max() * 1.1, y.mean() * 4)
        extent = (x.min(), x.max(), ymin, ymax)
        fig, ax = plt.subplots(figsize=(8, 8))
        h = ax.hexbin(
            x,
            y,
            gridsize=30,
            cmap=self.labels_and_colors[neurite][2],
            mincnt=1,
            extent=extent,
        )
        ax.axis("off")

        fname = f"results/for_article/fig2/{self.neuron_name}_colls_vs_dist_only_hexbin_{normed}_{neurite}.png"
        fig.savefig(fname, transparent=True, dpi=300)


def plot_running_avg_for_all():
    """Creates a plot in which each neuron is represented by the running average
    of its number  of collisions over the distance. The plot dissects axons,
    dendrites, L23 and L5 neurons.
    """
    l23_neurons, rest_of_neurons = filter_l23_neurons(neuron_names)
    l23_neurons = ((l23_neuron, "II/III") for l23_neuron in l23_neurons)
    rest_of_neurons = ((rest, "I/IV/V/VI") for rest in rest_of_neurons)
    all_neurons = itertools.chain.from_iterable((l23_neurons, rest_of_neurons))
    analyzed_data = []
    for neuron, layer in all_neurons:
        coll_dist = _neuron_to_obj(neuron)
        if not coll_dist:
            continue
        print(neuron)
        coll_dist.run()
        for df, neurite in zip(
            (coll_dist.parsed_axon, coll_dist.parsed_dend), ("Axon", "Dendrite")
        ):
            df = df.sort_values("dist")
            df["avg_coll"] = df["coll_normed"].rolling(30).mean()
            df["cumsum"] = df["coll_normed"].cumsum()
            df["type"] = neurite
            df["layer"] = layer
            df["name"] = neuron
            df = df.astype(
                {"type": "category", "layer": "category", "name": "category"}
            )
            analyzed_data.append(df)
    return analyzed_data


@numba.jit(nopython=True, parallel=True)
def norm_colls(bincounts, distances, collisions):
    """Iterate over the collision counts and normalize
    them by the neural density at that distance.
    """
    normed_collisions = np.zeros_like(collisions)
    for idx in numba.prange(len(collisions)):
        normed_collisions[idx] = collisions[idx] / bincounts[distances[idx]]
    return normed_collisions


def _name_to_graph_fname(
    neuron, folder=pathlib.Path("/data/neural_collision_detection/results/2019_2_10")
):
    return folder / f"graph_{neuron}_with_collisions.gml"


def _neuron_to_obj(
    neuron,
    results_folder=pathlib.Path("/data/neural_collision_detection/results/2019_2_10"),
):
    """Parses a filename containing a graph repr of a neuron
    into an CollisionsDistNative object"""
    graph_fname = _name_to_graph_fname(neuron, results_folder)
    try:
        coll_dist = CollisionsDistNaive.from_graph(
            graph_fname, neuron, results_folder=results_folder
        )
        return coll_dist
    except FileNotFoundError:
        return


def mp_main(neuron):
    """Run all functions in a parallel manner."""
    results_folder = pathlib.Path("/data/neural_collision_detection/results/2020_02_10")
    coll_dist = _neuron_to_obj(neuron, results_folder)
    if not coll_dist:
        return
    coll_dist.run()
    coll_dist.plot_all_jointplots()
    # coll_dist.plot_all_hexbins()
    # coll_dist.scatter()
    return coll_dist


def filter_l23_neurons(neuron_names):
    rest_of_neurons = neuron_names.copy()
    l23_neurons_idx = [-1, -4, 7, 8, 6, -2]
    l23_neurons = list(rest_of_neurons.pop(idx) for idx in l23_neurons_idx)
    return l23_neurons, rest_of_neurons


if __name__ == "__main__":
    # l23_neurons, rest_of_neurons = filter_l23_neurons(neuron_names)

    # multicore exec
    # with mp.Pool() as pool:
    #     res = pool.map(mp_main, neuron_names)

    # single core
    _ = [mp_main(neuron) for neuron in neuron_names]

    # plot_running_avg_for_all()
    plt.show(block=False)
