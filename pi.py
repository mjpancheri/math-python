import math
import random
import time


def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        # get two random numbers between 0 and 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # calculate distance from origin
        distance = x**2 + y**2
        # count points inside circle
        if distance <= 1:
            inside_circle += 1
    # estimate PI using formula (keep in mind that the accuracy of this estimate depends on the number of points generated)
    pi_estimate = (inside_circle / num_points) * 4
    return pi_estimate


def estimate_pi_2(num_points):
    # Initialize denominator
    k = 1

    # Initialize sum
    pi_estimate = 0

    for i in range(num_points):
        # even index elements are positive
        if i % 2 == 0:
            pi_estimate += 4 / k
        else:
            # odd index elements are negative
            pi_estimate -= 4 / k

        # denominator is odd
        k += 2

    return pi_estimate


def pi():
    return 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679


start_time = time.time()

num_points = 1000000

estimated_pi = estimate_pi_2(num_points)

print("--- {:.6f} seconds ---".format(time.time() - start_time))
print(f"Estimated value of π with {num_points} points: {estimated_pi}")
print(f"Actual value of π: {math.pi}")
