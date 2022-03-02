#include "sde.h"

double single_step(double y, double dt, double drift_const,
                   double noise, double lb, double ub) {
    return fmax(fmin(y + drift_const*(dt/y) + sqrt(dt)*noise, ub), lb);
}

double var_dt(double y, double kappa_sq) {
    return kappa_sq*y;
}

void interval(double* y, double dt, double drift_const, double lb,
                double ub, double kappa_sq, gsl_rng* rng) {
    double internal_time = 0;
    double noise = 0;
    double wdt = 0;
    while(internal_time < dt) {
        wdt = var_dt(*y, kappa_sq);
        wdt = fmin(wdt, dt-internal_time);
        
        noise = gsl_ran_gaussian_ziggurat(rng, 1.0);
        *y = single_step(*y, wdt, drift_const, noise, lb, ub);
        
        internal_time = internal_time + wdt;
    }
}

double transform(double x, double eta) {
    return 1/((eta-1)*pow(x, eta-1));
}

double inverseT(double y, double eta) {
    return pow((eta-1)*y, 1/(1-eta));
}

void generate_series(int n_points, double dt, double lambda, double eta,
                     double x_0, double lb, double ub, double kappa,
                     long seed, double* series) {
    int point = 0;
    // initialize GSL random number generator
    gsl_rng_env_setup();
    gsl_rng * rng = gsl_rng_alloc(gsl_rng_taus);
    gsl_rng_set(rng,seed);
    // precompute terms
    double drift_const = (lambda - eta)/(2.0 * (eta - 1.0));
    double trans_lb = transform(lb, eta);
    double trans_ub = transform(ub, eta);
    double bessel_lb = fmin(trans_lb, trans_ub);
    double bessel_ub = fmax(trans_lb, trans_ub);
    double kappa_sq = kappa*kappa;
    // THE MAIN LOOP
    double y = transform(x_0, eta);
    for(point=0; point<n_points; point=point+1) {
        interval(&y, dt, drift_const, bessel_lb, bessel_ub, kappa_sq, rng);
        series[point] = inverseT(y, eta);
    }
    // destroy GSL random number generator
    gsl_rng_free(rng);
}
