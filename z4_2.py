matrix = []

def main():
    # ввод матрицы
    print("Вводим матрицу")
    try:
        print("Введите количество строк:")
        strcount = int(input())
        print("Введите количество столбцов:")
        colcount = int(input())
        print("Будет введена матрица размерностью ", strcount, " строк на ", colcount, " столбцов.")
        print("Запрос в формате [ строка ] [ столбец ]")
        for i in range(colcount):
            a = []
            for f in range(strcount):
                print("Ввод элемента [", i + 1, "] [", f + 1, "]")
                a.append(int(input()))
            matrix.append(a)
    except ValueError:
        print("Ошибка ввода")
        return None

    print("Матрица введена:")
    printmatrix(colcount, strcount)

    sorted_by_columns(colcount, strcount)

    print("Результат:")
    printmatrix(colcount, strcount)


# выводим массив
def printmatrix(colcount, strcount):
    for i in range(colcount):
        for j in range(strcount):
            print(matrix[i][j], end=" ")
        print()

# сортировка
def sorted_by_columns(colcount, strcount):
    global matrix
    res = [[0] * strcount for _ in range(colcount)]
    for col in range(strcount):
        values = [r[col] for r in matrix]
        values.sort(reverse=True)
        for row in range(colcount):
            res[row][col] = values.pop()
    matrix = res


main()
