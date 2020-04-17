import math

def func(x):
    func_result = math.sin(0.5 + x) - 2 * x + 0.5
    return func_result

def cord_func(x, y):
    cord_func_result = x - ( (y - x) / (func(y) - func(x) ) ) * func(x)
    return cord_func_result

def cord_method(a, b, accuracy):
    cord_method_accuracy = abs(a - b)
    iteration_count = 0
    x = a

    while cord_method_accuracy >= accuracy:
        previous_x = x
        iteration_count += 1
        x = cord_func(x, b)

        if func(x) * func(b) >= 0:
            b = previous_x

        cord_method_accuracy = abs(previous_x - x)

    return x, iteration_count

a = float(input("Введите левую границу: "))
b = float(input("Введите правую границу: "))
accuracy = float(input("Введите точность: "))

x, it_c = cord_method(a, b, accuracy)

print ("Результат: " + str(x))
print ("Он был получен за " + str(it_c) + " итераций")
