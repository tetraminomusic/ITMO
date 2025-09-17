

def matrix_mult(A, B):
    return [[A[0][0]*B[0][0] + A[0][1]*B[1][0], 
            A[0][0]*B[0][1] + A[0][1]*B[1][1]], #умножение матриц
           [A[1][0]*B[0][0] + A[1][1]*B[1][0], 
            A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

def matrix_power(matrix, power):
    result = [[1, 0], [0, 1]]
    while power:
        if power % 2 != 0:
            result = matrix_mult(result, matrix)
        matrix = matrix_mult(matrix, matrix)
        power //= 2
    return result

def fib_matrix(n):
    if n <= 1:
        return n
    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n - 1)
    return result[0][0]


s_fib = input("Введите число в системе счисления Цекендорфа: ")
if (s_fib.replace('0', '').replace('1', '') == "" and "11" not in s_fib and "1" in s_fib):
    s_fib = s_fib.lstrip("0")[::-1]
    s_10 = 0
    for i in range(0, len(s_fib)):
        if s_fib[i] == "1":
            s_10+=fib_matrix(i+2)   
    print(f"Введённое число в 10-й системе счисления равняется: {s_10}") 
else: print("Ошибка: некорректный ввод числа")