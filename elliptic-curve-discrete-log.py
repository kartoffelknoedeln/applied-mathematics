def lambdaFunctions(point1, point2, a, modulo):
    if point1 != point2:
        for i in range(modulo):
            if ((int(point2[1]) - int(point1[1])) % modulo) == ((int(point2[0]) - int(point1[0])) * i % modulo):
                return i
    else:
        for i in range(modulo):
            if (2 * int(point1[1]) * i) % modulo == (3 * int(point1[0])**2 + a) % modulo:
                return i

def pointsUpdate(point1, point2, i, modulo):
    x = (i**2 - int(point1[0]) - int(point2[0])) % modulo
    y = (i*(int(point1[0]) - x) - int(point1[1])) % modulo
    point1 = x, y
    return point1

def main():
    point1 = []
    point2 = []
    print('Let the elliptic curve equation be E:Y**2 = X**3 + AX + B.')
    print()
    x1 = int(input('What is the coordinate of x for point 1? '))
    y1 = int(input('What is the coordinate of y for point 1? '))
    point1 = x1, y1
    x2 = int(input('What is the coordinate of x for point 2? '))
    y2 = int(input('What is the coordinate of y for point 2? '))
    point2 = x2, y2
    a = int(input('What is the value of A? '))
    modulo = int(input('What is the modulo value? '))
    add = int(input('How many times do you want to iterate adding? '))

    for i in range(add-1):
        i = lambdaFunctions(point1, point2, a, modulo)
        point1 = pointsUpdate(point1, point2, i, modulo)
        print(point1)

main()
