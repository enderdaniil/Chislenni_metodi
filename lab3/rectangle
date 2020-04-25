import math

def func(x):
    return math.pow(math.log(5 * x), 2)


def rectangle_integral_solvation(fragmentation_count):

    step = (100 - 1) / fragmentation_count
    current_x = 1
    integral_value = 0

    for i in range(fragmentation_count):
        integral_value += step * func(current_x)
        current_x += step

    return integral_value

needed_value = 2817.84234744392

for i in range(1, 7):
    fragmentation = int(math.pow(10, i))
    integral = rectangle_integral_solvation(fragmentation)
    error = abs(needed_value - integral)
    print("Amount of fragmentations: " + str(fragmentation) + ". Integral Value = " + str(integral)+ ". Error = " + str(error))
