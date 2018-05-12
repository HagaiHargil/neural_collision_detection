import os, sys

def main(argv):
	if len(argv) < 4:
		print "Usage: %s <output file> <radius> <location>" % argv[0]
		return 1
	
	filename = argv[1]
	r = float(argv[2])
	x,y,z = [float(x) for x in argv[3].split(",")]

	x_low = x - r
	x_high = x + r
	y_low = y - r
	y_high = y + r
	z_low = z - r
	z_high = z + r

	cube = """
v {x_low} {y_low} {z_low}
v {x_high} {y_low} {z_low}
v {x_high} {y_high} {z_low}
v {x_low} {y_high} {z_low}
v {x_low} {y_low} {z_high}
v {x_high} {y_low} {z_high}
v {x_high} {y_high} {z_high}
v {x_low} {y_high} {z_high}
f 1 5 6
f 1 6 2
f 2 6 7
f 2 7 3
f 3 7 8
f 3 8 4
f 4 8 5
f 4 5 1
f 6 8 7
f 6 5 8
f 4 2 3
f 4 1 2
	""".format(**locals())

	with open(filename, "w") as f:
		f.write(cube)


if __name__ == "__main__":
	main(sys.argv)