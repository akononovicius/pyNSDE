#include <math.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_randist.h>

extern void generate_series(int n_points, double dt, double lambda, double eta, double x_0, double lb, double ub, double kappa, long seed, double* series);
