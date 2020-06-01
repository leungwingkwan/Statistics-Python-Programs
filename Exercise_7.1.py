

def main():

    a = [74.001, 74.005, 74.003, 74.001, 74.000, 73.998, 74.006, 74.002]
    print(a)

    avg_a = 0
    sum_a = 0
    n = 0
    for e in a:
        sum_a = sum_a + e
        n = n + 1
    
    avg_a = sum_a / n

    print('average = ', avg_a)

    var_a = 0
    
    for e in a:
        var_a = var_a + (e - avg_a) ** 2


    print('variant = ', var_a / n)
    print('s = ', var_a / (n - 1))


if __name__ == '__main__':
    main()