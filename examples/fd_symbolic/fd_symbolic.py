"""
Code to symbolically find finite difference weights.
"""

def fd_weights(k, x, h):
    """
    Computes the finite difference weights for a kth derivative approximation
    at 0 using the points given in x.  The function prints the answer as
    well as various intermediate steps.

    Parameters
    ----------
    k : int
        The order of derivative to approximate.

    x : iterable
        The grid points to use for the approximation.  These should be symbolic
        expressions in some variable 'h'.

    h : symbolic variable
        The symbolic variable used in x.
    """

    from sympy import symbols, Function, pprint, series, factorial, Matrix, zeros, linsolve, O, diff

    # number of grid points
    r = len(x)

    # create symbols for the coefficients
    c = symbols('c0:{}'.format(r))

    # create the symbol for the function u
    u = Function('u')

    # symbolic variable for evaluating u
    x_sym = symbols('x')

    # generate the weighted sum
    S = sum([c[i]*u(x[i]) for i in range(r)])

    print()
    print('weighted sum = ', S)

    # create the Vandermonde system
    def vand(i, j):
        return x[j]**i/factorial(i)
    A = Matrix(r, r, vand)
    print()
    print("A = ")
    pprint(A)

    b = zeros(r, 1)
    b[k] = 1
    print()
    print("b = ")
    pprint(b)

    # solve the system
    sol = list(linsolve((A, b)))[0]
    print()
    print("c = ")
    pprint(sol)

    # form the approximation
    print()
    print("approximation = ")
    S_sol = S.subs(zip(c, sol))
    pprint(S_sol)

    # taret derivative
    target = diff(u(x_sym), x_sym, k).subs(x_sym, 0)
    print()
    print("order of approximation = ")
    pprint(O(series(S_sol-target, h)))


def run_example():
    "Runs an example of the symbolic FD weight approximation function."

    from sympy import Symbol

    # symbol to use for the step size
    h = Symbol('h')

    # derivative order
    k = 1

    # points to use for the derivative approximation
    x = [0, h]

    # find the approximation
    fd_weights(k, x, h)


if __name__ == "__main__":
    run_example()
