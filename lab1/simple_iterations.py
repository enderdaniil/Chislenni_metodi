import math

def func(x):
    func_result = (math.sin(0.5 + x) + 0.5) / 2
    return func_result

def simple_iterations(a, b, accuracy):
    x = (a + b) / 2
    simple_iterations_accuracy = abs(b - a)
    iteration_count = 0

    while simple_iterations_accuracy >= accuracy:
        previous_result = x
        iteration_count += 1
        x = func(x)
        simple_iterations_accuracy = x - previous_result

    return x, iteration_count

a = float(input("Введите левую границу: "))
b = float(input("Введите правую границу: "))
accuracy = float(input("Введите точность: "))

x, it_c = simple_iterations(a, b, accuracy)

print ("Результат: " + str(x))
print ("Он был получен за " + str(it_c) + " итераций")
