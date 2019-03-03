"""
A slightly better time loop. (Still not great)
"""

# initial and final times
t_init, t_fin = 0.0, 8.0

# number of time increments
N_t = 100000

# time step size
dt = (t_fin-t_init)/N_t

# initialize t variable
t = t_init

# loop over times
while(True):

    # print the current time
    print('t = {}'.format(t))

    # if we've reached the final time, stop
    if t >= t_fin:
        break

    # otherwise, increment the time
    t += dt

print()
print('8-t = {}'.format(8-t))
