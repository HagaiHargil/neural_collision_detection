"""
Aggregation of tools to analyze the graphs generated by
'graph_parsing.py'.
"""
import pathlib
import multiprocessing as mp
import itertools

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numba
import seaborn as sns
import scipy.spatial.distance

from ncd_post_process.create_neuron_id.collisions_vs_dist_naive import (
    CollisionsDistNaive,
)


plt.rcParams.update({"font.size": 22})
neuron_names = {
    "AP120410_s1c1": "V",
    "AP120410_s3c1": "V",
    "AP120412_s3c2": "V",
    "AP120416_s3c1": "IV",
    "AP120419_s1c1": "VI",
    "AP120420_s1c1": "IV",
    "AP120420_s2c1": "II/III",
    "AP120507_s3c1": "II/III",
    "AP120510_s1c1": "II/III",
    "AP120522_s3c1": "I",  # ?
    "AP120523_s2c1": "V",
    "AP120524_s2c1": "II/III",
    "AP120614_s1c2": "V",
    "AP130312_s1c1": "II/III",
    "AP131105_s1c1": "II/III",  # ?
    "AP130606_s2c1": "II/III",
    # "MW120607_LH3": "IV",
    "AP130110_s2c1": "II/III",
}


def _build_running_avg_df(neuron, layer):
    coll_dist = _neuron_to_obj(neuron)
    if not coll_dist:
        return
    coll_dist.run()
    all_data = []
    for df, neurite in zip(
        (coll_dist.parsed_axon, coll_dist.parsed_dend), ("Axon", "Dendrite")
    ):
        df = df.sort_values("dist")
        df["avg_coll"] = df["coll_normed"].rolling(30).mean()
        df["cumsum"] = df["coll_normed"].cumsum()
        df["type"] = neurite
        df["layer"] = layer
        df["name"] = neuron
        df = df.astype({"type": "category", "layer": "category", "name": "category"})
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)


def plot_running_avg_for_all():
    """Creates a plot in which each neuron is represented by the running average
    of its number  of collisions over the distance. The plot dissects axons,
    dendrites, L23 and L5 neurons.
    """
    l23_neurons = ((name, val) for name, val in neuron_names.items() if val == "II/III")
    rest_of_neurons = (
        (name, "I/IV/V/VI") for name, val in neuron_names.items() if val != "II/III"
    )
    all_neurons = itertools.chain.from_iterable((l23_neurons, rest_of_neurons))
    with mp.Pool() as pool:
        analyzed_data = pool.starmap(_build_running_avg_df, all_neurons)
    analyzed_data = pd.concat(analyzed_data, ignore_index=True)
    # ax_cumsum = sns.relplot(data=analyzed_data, x='dist', y='cumsum', hue='layer', col='type', kind='line')
    canonical_dists = np.linspace(
        analyzed_data["dist"].min(), analyzed_data["dist"].max(), 1000
    )
    analyzed_data["dist_norm"] = canonize_dists(
        analyzed_data.loc[:, "dist"].to_numpy(), canonical_dists
    )
    ax_dist = sns.relplot(
        data=analyzed_data,
        x="dist_norm",
        y="coll_normed",
        col="layer",
        hue="type",
        kind="line",
        alpha=0.4,
        hue_order=["Axon", "Dendrite"],
        palette=["C2", "C1"],
    )
    return ax_dist, 0, analyzed_data


def canonize_dists(current: np.ndarray, new: np.ndarray):
    """Find the closest canonized distance for each real one.

    We canonize the distances to make sure that the averaged plot will have a correct
    x axis, so we have to transform the real distance into a canonized one.
    """
    dists = scipy.spatial.distance.cdist(new[:, np.newaxis], current[:, np.newaxis])
    closest = dists.argmin(0)
    return new[closest]


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
    neuron, folder=pathlib.Path("/data/neural_collision_detection/results/2020_09_05")
):
    return folder / f"graph_{neuron}_with_collisions.gml"


def _neuron_to_obj(
    neuron,
    results_folder=pathlib.Path("/data/neural_collision_detection/results/2020_09_05"),
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


if __name__ == "__main__":
    ax_cumsum, ax_dist, analyzed_data = plot_running_avg_for_all()
    plt.show(block=False)
