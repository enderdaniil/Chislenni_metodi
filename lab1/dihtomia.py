import math

def func(x):
    func_result = math.sin(0.5 + x) - 2 * x + 0.5
    return func_result

def dihtomia(a, b, accuracy):
    diht_accuracy = abs(b - a)
    iteration_count = 1
    result = (a + b) / 2
    func_res = func(result)
    func_a = func(a)

    if (func_a * func_res < 0):
        b = result
    else:
        a = result

    while diht_accuracy >= accuracy:
        previous_result = result
        iteration_count += 1
        result = (a + b) / 2
        func_res = func(result)
        func_a = func(a)
        if(func_a * func_res < 0):
            b = result
        else:
            a = result
        diht_accuracy = abs(result - previous_result)

    return result, iteration_count
#
a = float(input("Введите левую границу: "))
b = float(input("Введите правую границу: "))
accuracy = float(input("Введите точность: "))

x, it_c = dihtomia(a, b, accuracy)

print ("Результат: " + str(x))
print ("Он был получен за " + str(it_c) + " итераций")
