import pathlib

import attr
from attr.validators import instance_of
import matplotlib.pyplot as plt
import networkx as nx

from find_branching_density import BranchDensity
from src.ncd_post_process.graph_parsing import load_neuron
from src.ncd_post_process.analyze_graph import graph_file_to_graph_object


@attr.s
class BranchDensityAndCollisions:
    """
    Takes a generated BranchDensity object and a serialized neuron and compares
    the branching density of that neuron as computed in the BranchDensity class
    with the number of collisions each point on the neuronal tree has. Finally
    it will also plot the result.
    """

    bdens = attr.ib(validator=instance_of(BranchDensity))
    graph = attr.ib(validator=instance_of(nx.Graph))
    counts = attr.ib(init=False)

    def main(self):
        """ Main pipeline """
        self.counts = self._get_counts_from_bdens()
        self._pop_counts_with_colls()
        self._plot_colls_and_dens()

    def _get_counts_from_bdens(self):
        """
        Runs the main analysis pipeline of the BranchDensity class to
        receive a DataFrame containing the density data per radius.
        :return pd.DataFrame:
        """
        counts = bdens.main()
        return counts

    def _pop_counts_with_colls(self):
        self.counts['collisions'] = 0
        row_idx = 0
        for node in self.graph.nodes():
            self.counts.iloc[row_idx, -1] = node.collisions
            row_idx += 1

    def _plot_colls_and_dens(self):
        """
        Uses the populated DataFrame from "_pop_counts_with_colls" to plot
        the correlation between number of collisions and the density of each
        point.
        :return:
        """
        fig, ax = plt.subplots()
        r = 10
        axon_idx = self.counts.index.get_level_values('tree') == 'Axon'
        axon_df = self.counts.loc[axon_idx]
        dend_df = self.counts.loc[~axon_idx]
        ax.scatter(axon_df[r], axon_df['collisions'], c='C2', s=0.2, alpha=0.8, label='Axon')
        ax.scatter(dend_df[r], dend_df['collisions'], c='C1', s=0.2, alpha=0.8, label='Dendrite')
        ax.set_xlabel(f'U(r={r})')
        ax.set_ylabel('# of collisions')
        ax.legend()
        ax.set_title(f'Collisions as a function of density for a single neuron with r={r} um')

if __name__ == '__main__':
    neuron_name = 'AP120410_s1c1'
    neuron_fname = pathlib.Path(__file__).resolve().parents[
                      3] / "data" / "neurons" / f"{neuron_name}.xml"
    py3dn_folder = pathlib.Path(__file__).resolve().parents[2] / "py3DN"
    bdens = BranchDensity(neuron_fname, py3dn_folder)
    neuron_graph = pathlib.Path(__file__).resolve().parents[
                       3] / "results" / "2019_2_10" /\
                       f'graph_{neuron_name}_with_collisions.gml'
    graph = graph_file_to_graph_object(neuron_graph)
    bdens_coll = BranchDensityAndCollisions(bdens, graph)
    bdens_coll.main()
    plt.show()
