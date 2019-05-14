"""
Tools for Chebyshev differentiation.
"""

import numpy as np

def cheb(n, x_left=-1, x_right=1):
    """
    Computes the Chebyshev grid and differentiation matrix on n+1 points.

    Parameters
    ----------
    n : int
        n+1 is the number of grid points.
    x_left : float
        Location of the left grid point.
    x_right : float
        Location of the right grid point.

    Returns
    -------
    D : array_like
        The (n+1)-by-(n+1) Chebyshev differentiation matrix.
    x : array_like
        The Chebyshev nodes on the interval [-x_left,x_right].

    Notes
    -----
    This function is based on cheb.m from Trefethen's Spectral
    Methods in MATLAB.  Unlike Trefethen's, however, this function
    orders the nodes from left to right.  That is, x[0] = x_left
    and x[-1] = x_right
    """

    # Trefethen's algorithm
    n_range = np.arange(n+1)
    x = np.cos(np.pi*n_range/n)
    c = np.array([2] + (n-1)*[1] + [2]) * (-1)**n_range

    X = np.tile(x, (n+1, 1)).T
    dX = X - X.T

    D = np.outer(c, 1/c)/(dX + np.eye(n+1))
    D -= np.diag(np.sum(D, axis=1))

    # swap orders of nodes so x=-1 is first
    x = x[::-1]
    D = D[::-1, ::-1]

    # change variables for given interval
    x = 0.5*((x_right-x_left)*x + x_left + x_right)
    D *= 2/(x_right-x_left)

    return D, x
