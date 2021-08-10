#include <math.h>

double square(double i) {
	return sqrt(i);
}

double squareTimes(double i, int times) {
	double res = 0;
	for (int j = 0; j < times; j++)
	{
		res += i;
		res = sqrt(res);
	}
	return res;
}
