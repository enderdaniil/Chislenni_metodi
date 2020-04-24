import math

def kramer(x,y):

    main_determinant = math.sin(x - 2) * math.cos(y + 0.5) - 1

    first_determinant = -math.sin(y + 0.5) + x + 1 + math.cos(y + 0.5) * math.cos(x - 2) + y * math.cos(y + 0.5)

    second_determinant = math.cos(x - 2) + y - (-math.sin(x - 2) * (-math.sin(y + 0.5) + x + 1))

    delta_x = first_determinant / main_determinant
    delta_y = second_determinant / main_determinant

    return delta_x, delta_y



def newton(accur):

    iteration_count = 0
    previous_x = 0
    previous_y = 0
    delta_x, delta_y = kramer(previous_x, previous_y)
    x = previous_x + delta_x
    y = previous_y + delta_y

    while (accur < abs(delta_x) or accur < abs(delta_y)):

        iteration_count +=1
        previous_x = x
        previous_y = y

        delta_x, delta_y = kramer(previous_x, previous_y)

        x = previous_x + delta_x
        y = previous_y + delta_y


    return x, y, iteration_count


accuracy = float(input("Введите точность: "))

x, y, it_count = newton(accuracy)

print("x = " + str(x) + ", y = " + str(y) + ", iteration count = " + str(it_count))
