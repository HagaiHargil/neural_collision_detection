#!/usr/bin/python

import os, sys, re
import multiprocessing
from aggregator import aggregate, get_vascular

def get_ncd_results(ncd_output_file, max_collisions):
	results = []
	with open(ncd_output_file, "r") as f:
		for l in f:
			splitted = l.split(",")
			if len(splitted) < 7:
				continue
			if int(splitted[7]) > max_collisions:
				continue
			results.append(l)

	return results
	

def process_main(results, out_dir, threshold_distance, vascular):
	for res in results:
		splitted = res.split(",")

		neuron_name = splitted[0]
		location = [splitted[1], splitted[2], splitted[3]]
		rotation = [splitted[4], splitted[5], splitted[6]]

		l = ",".join(location)
		r = ",".join(rotation)

		location = [int(x) for x in location]
		rotation = [int(x) for x in rotation]

		# TODO: get rid also of these files
		out_file = "{0}/out_{1}_{2}_{3}.txt".format(out_dir, neuron_name, l, r).replace(",", "_")
		neuron_name = neuron_name.replace(".obj", "_balls.csv")
		neuron_fname = "../../neurons/" + neuron_name
		vascular_fname = "../../vascular/vascular_balls.csv"

		aggregate(vascular_fname, neuron_fname, location, rotation, out_file, threshold_distance, vascular)


def main(argv):
	if len(argv) < 4:
		print("Usage: %s <ncd output file> <max collisions> <threshold distance> <out dir>" % argv[0])
		return 1

	ncd_output_file = argv[1]
	max_collisions = int(argv[2])
	threshold_distance = int(argv[3])
	out_dir = argv[4]

	os.system("mkdir {0}".format(out_dir))

	ncd_results = get_ncd_results(ncd_output_file, max_collisions)
	print("Running over {0} results".format(len(ncd_results)))

	process_count = 20
	results_per_process = 1.0 * len(ncd_results) / process_count
	processes = []
	last_idx = 0
	vascular_fname = "../../vascular/vascular_balls.csv"
	vascular = get_vascular(vascular_fname)

	for i in range(process_count):
		next_idx = int(results_per_process * (i + 1))
		if i == process_count - 1:
			next_idx = len(ncd_results)

		params = (ncd_results[last_idx : next_idx], out_dir, threshold_distance, vascular)
		print(len(params[0]))

		p = multiprocessing.Process(target=process_main, args = params)
		processes.append(p)
		p.start()
		last_idx = next_idx

	for i in range(process_count):
		processes[i].join()

if __name__ == "__main__":
	sys.exit(main(sys.argv))
