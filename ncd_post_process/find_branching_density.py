"""
Using a serialized neuron, finds the number of branching points
every point along the neuronal path has by wrapping it in spheres
and counting the number of branches inside it
"""
import pathlib

import numpy as np
import pandas as pd
import scipy
import attr
from attr.validators import instance_of

from graph_parsing import load_neuron
from blender.general_methods import name_neuron_trees


@attr.s
class BranchDensity:
    neuron_fname = attr.ib(
        validator=instance_of(pathlib.Path)
    )  # a neuron from the NeuroLucida XML parser
    py3dn_folder = attr.ib(validator=instance_of(pathlib.Path))
    neuron_coords = attr.ib(init=False)
    neuron_branch_coords = attr.ib(init=False)
    branch_counts = attr.ib(init=False)
    sphere_sizes = attr.ib(init=False)
    branch_points = attr.ib(init=False)
    tree_of_point = attr.ib(init=False)

    def main(self):
        """
        Runs the pipeline.
        """
        with load_neuron(self.py3dn_folder, self.neuron_fname) as neuron:
            num_of_nodes = self._get_num_of_nodes(neuron)
            self.neuron_coords, self.neuron_branch_coords, self.tree_of_point = self._get_coords(
                neuron, num_of_nodes
            )
        self.sphere_sizes, self.branch_counts = self._setup_data_structs()
        distances = self._calc_distance_bet_all_coords_and_branches()
        for radius in self.sphere_sizes:
            self.branch_counts[radius] = self._count_encircled_points(distances, radius)
        return self.branch_counts

    def _get_num_of_nodes(self, neuron) -> int:
        """ Count number of nodes on an XML neuron """
        num_of_nodes = 0
        for tree in neuron.tree:
            num_of_nodes += tree.total_rawpoints
        return num_of_nodes

    def _setup_data_structs(self):
        """
        Generates a DataFrame with its index being the different neural coordinates with
        their corresponding tree, and columns that correspond to a radius of a sphere circling each coordinates.
        The values of the DF are the number of branching points inside that sphere
        radius for each coordinate.
        """
        sphere_sizes = np.arange(1, 11, dtype=np.uint64)
        coord_num = self.neuron_coords.shape[0]
        df_dict = {
            sphere_size: np.zeros(coord_num, dtype=np.uint32)
            for sphere_size in sphere_sizes
        }
        df_dict["tree"] = self.tree_of_point
        df_dict["num"] = np.arange(coord_num)
        branch_counts = (
            pd.DataFrame(df_dict)
            .assign(x=self.neuron_coords[:, 0])
            .assign(y=self.neuron_coords[:, 1])
            .assign(z=self.neuron_coords[:, 2])
            .set_index(["num", "tree", "x", "y", "z"])
        )
        return sphere_sizes, branch_counts

    def _get_coords(self, neuron, num_of_nodes):
        """
        Parses the neuronal tree, populating an array with the coordinates
        of all the points in that tree (in Euclidean space), as well as
        points which are also branching points ('nodes').
        """

        neuronal_nodes = np.zeros((num_of_nodes, 3), dtype=np.float64)
        tree_of_point = np.zeros(num_of_nodes, dtype=object)
        neuronal_coords = neuronal_nodes.copy()
        coord_number = 0
        node_number = 0
        tree_names = name_neuron_trees(neuron)
        for tree, tree_name in zip(neuron.tree, tree_names):
            for point in tree.rawpoint:
                tree_of_point[coord_number] = tree_name
                p = point.P
                neuronal_coords[coord_number] = p
                if (
                    point.ptype == "standard"
                    or point.ptype == "node"
                    or point.ptype == "endpoint"
                ):
                    neuronal_nodes[node_number] = p
                    node_number += 1
                coord_number += 1

        return neuronal_coords, neuronal_nodes[:node_number], tree_of_point

    def _calc_distance_bet_all_coords_and_branches(self):
        """
        Returns a distance matrix between all neuronal coordinates and
        the branch points of that same neuron.
        The number of rows is the number of coordinates on the neuron,
        and the number of columns is the number of branching points.
        The results are in microns.
        """
        return scipy.spatial.distance.cdist(
            self.neuron_coords, self.neuron_branch_coords
        )

    def _count_encircled_points(self, distmat, radius):
        """
        With the given distance matrix (from calc_distance_bet_all_coords)
        and the current radius, finds and counts the number of points
        located in a sphere of radius "radius" and returns that number.
        """
        encircled = (distmat < radius).sum(axis=1)
        return encircled


if __name__ == "__main__":
    neuron_fname = (
        pathlib.Path(__file__).resolve().parents[1] / "data" / "neurons" / "AP120410_s1c1.xml",
        pathlib.Path(__file__).resolve().parents[1] / "data" / "neurons" / "AP120410_s3c1.xml",
        pathlib.Path(__file__).resolve().parents[1] / "data" / "neurons" / "AP120412_s3c2.xml",
        pathlib.Path(__file__).resolve().parents[1] / "data" / "neurons" / "AP120416_s3c1.xml",
    )
    py3dn_folder = pathlib.Path(__file__).resolve().parents[1] / "py3DN"
    for nf in neuron_fname[:1]:
        branch_den = BranchDensity(nf, py3dn_folder)
        counts = branch_den.main()
        counts.hist()
