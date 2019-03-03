"""
Comparison of "spectral" solvers using equispaced and Chebyshev-spaced grids.
"""

import numpy as np
import matplotlib.pyplot as plt
import fd_tools as fd

SHOW_EQUISPACED_SOLUTION = True
SHOW_CHEBYSHEV_SOLUTION = True

def build_matrix(x):
    n = len(x)
    A = np.zeros((n,n))

    # first row is a Neumann condition
    A[0,:] = fd.fd_coeff_fornberg(1, x[0], x)

    # intermediate rows approximate u''
    for i in range(1,n-1):
        A[i,:] = fd.fd_coeff_fornberg(2, x[i], x)

    # last row is Dirichlet
    A[-1,-1] = 1

    return A

def run_example():

    # left and right boundary locations
    xl = -1.8
    xr = 2.1

    # known solution
    def sol(x):
        a = 2.8
        b = 1.1
        return np.cos(a*x - b)

    # first derivative of solution
    def d_sol(x):
        a = 2.8
        b = 1.1
        return -a*np.sin(a*x - b)

    # second derivative of solution
    def d2_sol(x):
        a = 2.8
        b = 1.1
        return -a**2*np.cos(a*x - b)

    ns = range(5, 50, 5)
    errs_equi = []
    errs_cheb = []

    for n in ns:

        # equispaced grid
        x = np.linspace(xl, xr, n)

        # build the right-hand side
        b = np.zeros(n)
        b[0] = d_sol(x[0])
        b[1:-1] = d2_sol(x[1:-1])
        b[-1] = sol(x[-1])

        # build the matrix
        A = build_matrix(x)

        # solve
        u = np.linalg.solve(A, b)

        errs_equi.append(np.linalg.norm(u - sol(x), np.inf))

        # chebyshev grid
        z = np.linspace(0, 1, n)
        x = xl + 0.5*(xr-xl)*(1 + np.cos(np.pi*(1 - z)))

        # build the right-hand side
        b = np.zeros(n)
        b[0] = d_sol(x[0])
        b[1:-1] = d2_sol(x[1:-1])
        b[-1] = sol(x[-1])

        # build the matrix
        A = build_matrix(x)

        # solve
        u = np.linalg.solve(A, b)

        errs_cheb.append(np.linalg.norm(u - sol(x), np.inf))

    if SHOW_EQUISPACED_SOLUTION:
        plt.semilogy(ns, errs_equi, label='equispaced')
    if SHOW_CHEBYSHEV_SOLUTION:
        plt.semilogy(ns, errs_cheb, label='chebyshev')
    plt.xlabel('n')
    plt.ylabel('max error')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_example()