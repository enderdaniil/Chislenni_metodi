import math

def func(x):
    return math.pow(math.log(5 * x), 2)


def simpson_integral_solvation(fragmentation_count):

    fragmentation_count *= 2

    step = (100 - 1) / fragmentation_count
    current_x = 1 + step
    integral_value = 0

    for i in range(1, fragmentation_count, 2):
        integral_value += (step / 3) * (func(current_x - step) + 4 * func(current_x) + func(current_x + step))
        current_x += 2 * step

    return integral_value


needed_value = 2817.84234744392

for i in range(1, 7):
    fragmentation = int(math.pow(10, i))
    integral = simpson_integral_solvation(fragmentation)
    error = abs(needed_value - integral)
    print("Amount of fragmentations: " + str(fragmentation) + ". Integral Value = " + str(integral)+ ". Error = " + str(error))
