"""
Demo of using the SVD to numerically check stability of a method.
"""
import scipy.sparse as sp
import numpy as np
import matplotlib.pyplot as plt


# set this flag to true to run tests at the beginning
RUN_TESTS = True

def build_matrix(n, lb_type='D'):
    """
    Generates a matrix for the 2nd-order discretization of the problem

      u''   = f
      u(0) = u_0   OR   u'(0) = u'_0
      u(1)  = u_1

    where the flag lb_type determines the left boundary type.

    Parameters
    ----------
    n : int
        The number of interior grid points.
    lb_type : str
        The left boundary condition type. 'D' for Dirichlet, 'N' for Neumann.

    Returns
    -------
    A : spmatrix
        A sparse (n+2)-by-(n+2) matrix for the system.
    """

    # set up lists to build the matrix
    I = []
    J = []
    data = []

    # compute the step size
    h = 1/(n+1)

    # handle the first row
    if lb_type == 'N':
        I.extend([0, 0, 0])
        J.extend([0, 1, 2])
        data.extend([-3/(2*h), 2/h, -1/(2*h)])
    elif lb_type == 'D':
        I.append(0)
        J.append(0)
        data.append(1)
    else:
        raise RuntimeError('Boundary type {} unknown'.format(lb_type))

    # handle the intermediate rows
    for i in range(1, n+1):
        I.extend([i, i, i])
        J.extend([i-1, i, i+1])
        data.extend([1/h**2, -2/h**2, 1/h**2])

    # handle the last row
    I.append(n+1)
    J.append(n+1)
    data.append(1)

    return sp.csr_matrix((data, (I, J)), (n+2, n+2))

def run_tests():
    "Some simple tests to make sure we build the correct matrix."

    # print out a small matrix
    print()
    print("build_matrix(4, 'N') = ")
    print(build_matrix(4, 'N').toarray())

    # check that the matrix evaluates correctly on a quadratic
    n = 20
    A = build_matrix(n, 'N')
    x = np.linspace(0, 1, n+2)
    u = 3*x**2 - 6*x
    Au = A*u
    expected = np.array([-6] + n*[6] + [-3])
    np.testing.assert_almost_equal(Au, expected)
    print()
    print("Quadratic test passed")
    print(Au)


def plot_norms():
    """
    Plots matrix norms to check stability.

    Notes
    -----
    The following is not super efficient, but it gets the job done for an
    in-class demonstration.

    """

    ns = range(50, 1000, 50)
    test_types = (('D', 2), ('N', 2), ('D', np.inf), ('N', np.inf))
    norms = [[] for tt in test_types]

    # loop over n
    for n in ns:

        # loop over test types
        for i, (bc, order) in enumerate(test_types):
            A = build_matrix(n, bc).toarray()
            Ai = np.linalg.inv(A)
            norms[i].append(np.linalg.norm(Ai, order))

    for i, tt in enumerate(test_types):
        plt.plot(ns, norms[i], label=tt)
    plt.legend()
    plt.xlabel('n')
    plt.ylabel('norm')
    plt.show()



if __name__ == "__main__":

    # should we run the tests?
    if RUN_TESTS:
        run_tests()

    plot_norms()
