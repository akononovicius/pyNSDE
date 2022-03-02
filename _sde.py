import ctypes as c
import gc
import os as os

import numpy as np

___ctypes_local_dir = os.path.dirname(os.path.realpath(__file__)) + "/"
___lib_c = c.CDLL(___ctypes_local_dir + "libsde.so")
___lib_c.generate_series.argtypes = [
    c.c_int,  # n_points
    c.c_double,  # dt
    c.c_double,  # lambda
    c.c_double,  # eta
    c.c_double,  # x_0
    c.c_double,  # lb
    c.c_double,  # ub
    c.c_double,  # kappa
    c.c_long,  # seed
    c.POINTER(c.c_double),  # *series
]
___lib_c.generate_series.restype = None


def generate_series(
    n_points: int,
    dt: float,
    *,
    la: float = 3,
    eta: float = 1.5,
    x_0: float = 2,
    lb: float = 1,
    ub: float = 1000,
    kappa: float = 0.01,
    seed: int = -1
) -> np.ndarray:
    """Generate time series, which would be solution of the nonlinear SDE.

    Input:
        n_points:
            The desired length of the time series.
        dt:
            Time step in between the samples recorded within the time series.
        la: (default: 3)
            Value of the NSDE parameter lambda, which determines the slope of
            the stationary PDF of the process.
        eta: (default: 1.5)
            Value of the NSDE parameter eta (the nonlinearity / 
            multiplicativity) exponent.
        x_0: (default: 2)
            Initial condition for the stochastic process.
        lb: (default: 1)
            Lower (minimum) bound of the interval within which the stochastic
            process is forced to stay.
        ub: (default: 1000)
            Upper (maximum) bound of the interval within which the stochastic
            process is forced to stay.
        kappa: (default: 0.01)
            Numerical precission parameter. The smaller, the better the
            quality of the generated series, but the simulations will likewise
            take more time.
        seed: (default: -1)
            RNG seed. If negative value is passed (which is the default), then
            the seed will be randomly generated by `np.random.rand(2**20)`.

    Output:
        Numpy array of length n_points containing stochastic process samples
        each dt time ticks.

    Examples:
        ```
        >> from sde import generate_series
        >> series = generate_series(1048576, 1e-3, seed=123)
        >> series[:10]
            array([1.88769125, 1.88685838, 1.81436495, 1.87488873, 1.90115641,
                   1.88570894, 1.83027003, 1.86009928, 1.92396902, 2.12918531])
        ```
    """
    # auto-generate seed
    if seed < 0:
        np.random.seed()
        seed = np.random.randint(0, int(2 ** 20))

    data = (c.c_double * n_points)()
    ___lib_c.generate_series(n_points, dt, la, eta, x_0, lb, ub, kappa, seed, data)
    ret = np.array([d for d in data])
    del data
    gc.collect()

    return ret