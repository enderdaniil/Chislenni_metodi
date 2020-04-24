import math

k = 6

def progonka(quation_lines):


    x = [0] * quation_lines
    u = [0] * quation_lines
    v = [0] * quation_lines

    a = [0] * (quation_lines)
    b = [0] * quation_lines
    c = [0] * quation_lines
    d = [0] * quation_lines

    b[1] = -1
    c[1] = pow(5, 7)
    d[1] = 5
    u[1] = - c[1] / b[1]
    v[1] = d[1] / b[1]

    for i in range(2, quation_lines):

        a[i] = i + k

        b[i] = math.pow(-1, i + k)
        c[i] = math.pow(-i + k, i + k)
        d[i] = k - i

        u[i] = - c[i] / (a[i] * u[i - 1] + b[i])
        v[i] = (d[i] - a[i] * v[i-1]) / (a[i] * v[i - 1] + b[i])

    x[quation_lines - 1] = (d[quation_lines - 1] - a[quation_lines - 1] * v[quation_lines - 1 - 1]) / (a[quation_lines - 1] * u[quation_lines - 1 - 1] + b[quation_lines - 1])

    for i in range(quation_lines - 2, 0, -1):
        x[i] = u[i] * x[i + 1] + v[i]

    return x

n = int (input("Введите количество строк: "))
n += 1

c = []

if n > 1:
    c = progonka(n)
else:
    c[0] = -5

for i in range(1, n):
    print(c[i])
