import math

def jakobi(accuracy):
    iteration_count = 0
    previous_x = 0
    previous_y = 0

    x = math.sin(previous_y + 0.5) - 1
    y = -math.cos(previous_x - 2)

    epsilon = max(abs(x - previous_x), abs(y - previous_y))

    while (epsilon > accuracy):

        iteration_count += 1
        previous_x = x
        previous_y = y

        x = math.sin(previous_y + 0.5) - 1
        y = -math.cos(previous_x - 2)

        epsilon = max(abs(x - previous_x), abs(y - previous_y))


    return x, y, iteration_count



accuracy = float(input("Введите точность: "))

x, y, it_count = jakobi(accuracy)

print("x = " + str(x) + ", y = " + str(y) + ", iteration count = " + str(it_count))
