"""
Another good option.
"""

# initial and final times
t_init, t_fin = 0.0, 8.0

# number of time increments
N_t = 100000

# time step size (for this option, we don't compute dt)
# dt = (t_fin-t_init)/N_t

# initialize increment counter
i = 0

# loop over times
while(True):

    # find t
    t = t_init + (t_fin-t_init)*(i/N_t)

    # print the current time
    print('t = {}'.format(t))

    # if we've reached the final time, stop
    if i == N_t:
        break

    # otherwise, increment the time
    i += 1