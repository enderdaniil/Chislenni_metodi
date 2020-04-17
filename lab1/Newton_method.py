import math

def func(x):
    func_result = math.sin(0.5 + x) - 2 * x + 0.5
    return func_result

def func_derivative(x):
    func_derivative_result = math.cos(0.5 + x) - 2
    return func_derivative_result

def func_second_derivative(x):
    func_second_derivative_result = math.sin(0.5 + x)
    return func_second_derivative_result

def newton(a, b, accuracy):
    x = 0
    iteration_count = 0

    if (func(a) * func_second_derivative(a) < 0):
        x = a
    else:
        x = b

    newton_accuracy = abs(a - b)

    while (newton_accuracy >= accuracy):
        iteration_count += 1
        previous_result = x
        x = x - (func(x)/func_derivative(x))
        newton_accuracy = abs(x - previous_result)

    return x, iteration_count

a = float(input("Введите левую границу: "))
b = float(input("Введите правую границу: "))
accuracy = float(input("Введите точность: "))

x, it_c = newton(a, b, accuracy)

print ("Результат: " + str(x))
print ("Он был получен за " + str(it_c) + " итераций")
