import numpy as np
import matplotlib.pyplot as plt
import random
# qty = int(input('provide number of points to plot\n '))
np.set_printoptions(linewidth=np.inf) # prevents output array from wrapping to next line in the "run" window


def get_points(n):

    # obtain x and y of each point. No two x positions can be the same.
    # This means there must be at least as many random numbers to choose from as there are points
    xset = set()
    x = np.array([])
    y = np.array([])

    while len(xset) < n:
        xset.add(random.randint(1, n+5))
    x = np.append(x, sorted(list(xset)))
    for i in range(n):
        y = np.append(y, np.array([random.randint(1, n+5)]))
    print(x)
    print(y)
    return x, y


def create_curves(p):
    x, y = get_points(p)
    a = np.array([])
    b = np.array([])
    f = np.array([])
    for i in range(p):
        # create polynomials to connect each point.
        # we will solve at = b
        # t is the vector with all the unknown coefficients for the polynomial
        # entries are coefficients of: [ti1, ti2, ti3, ti4,  t(i+1)1,  t(i+1)2, t(i+1)3]
        if i < p - 1:
            zeros_left = np.zeros(4 * i)  # staggering
            zeros_right = np.zeros(4 * (p - i) - 8)  # staggering
            if i == 0:
                m = x[1] - x[0]
                row_a = np.append((np.append(zeros_left, [m ** 3, m ** 2, m, 1, 0, 0, 0])), zeros_right)
                row_b = np.append((np.append(zeros_left, [0, 0, 0, 1, 0, 0, 0])), zeros_right)  # ti4 is equal to y[i]
                row_c = np.append(
                    (np.append(zeros_left, [3 * m ** 2, 2 * m, 1, 0, 0, 0, -1])),
                    zeros_right)  # 1st derivative minus a_(i+1)3 = 0
                row_d = np.append((np.append(zeros_left, [6 * m, 0, 0, 0, 0, -2, 0])),
                                  zeros_right)  # 2nd derivative minus 2(a_(i+1)2) = 0
                row_e = np.append((np.append(zeros_left, [0, 1, 0, 0, 0, 0, 0])),
                                  zeros_right)  # 2nd derivative of curve at 1st point is 0
                a = np.vstack((row_a, row_b, row_c, row_d, row_e))
                b = np.append(b, [y[1], y[0], 0, 0, 0])
            else:
                m = x[i + 1] - x[i]
                row_f = np.append((np.append(zeros_left, [m ** 3, m ** 2, m, 1, 0, 0, 0])), zeros_right)
                row_g = np.append((np.append(zeros_left, [0, 0, 0, 1, 0, 0, 0])), zeros_right)  # ti4 is equal to y[i-1]
                row_h = np.append((np.append(zeros_left, [3 * m ** 2, 2 * m, 1, 0, 0, 0, -1])), zeros_right)  # 1st derivative minus a_(i+1)3 = 0
                row_i = np.append((np.append(zeros_left, [6 * m, 2, 0, 0, 0, -2, 0])), zeros_right)  # 2nd derivative minus 2(a_(i+1)2) = 0
                a = np.vstack((a, row_f, row_g, row_h, row_i))
                b = np.append(b, [y[i + 1], y[i], 0, 0])

        if i == p - 1:  # 2nd derivative of curve at last point is 0`
            zeros_left = np.zeros(4 * (p - 1))
            row_j = np.append(zeros_left, [6 * (x[p - 1] - x[p - 2]), 2, 0])
            a = np.vstack((a, row_j))
            a = np.delete(a, a.shape[1] - 1, 1)
            b = np.append(b, 0)
            # return a, b  # used for debugging
            print(b)

    t = np.linalg.solve(a, b)
    print(t)
    for c in range(p - 1):
        f = np.array([])
        x_1 = np.linspace(x[c], x[c + 1], 60)  # x_1 is the independent variable input into the function
        for d in x_1:
            m = d - x[c]
            l = 4 * c
            f = np.append(f, ([(t[l] * (m ** 3)) + (t[l + 1] * (m ** 2)) + (t[l + 2] * m) + t[l + 3]]))
            # print(f)

        plt.plot(x_1, f, color='#e84a27')
        plt.plot(x, y, color='lightgray', zorder=0)

create_curves(6)
plt.show()
#a, b = create_curves()
#print(a)
#print(a.shape)
#a_solve = np.linalg.solve(a, b)
#print(a_solve)