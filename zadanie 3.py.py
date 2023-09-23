# Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
# Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
# Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty
# pozycyjne, niebędące słowami kluczowymi podczas wywoływania funkcji, w krotkę.

# Напишите функцию переменной-параметра, которая выводит значения параметров на экран.
# Затем измените функцию, чтобы найти и вернуть максимальное значение.
# Подсказка: используйте параметр *args, который объединяет любые дополнительные (избыточные) аргументы.
# позиционные, неключевые слова при вызове функции, в кортеж.

def funckcja(*argumenty):
    print(argumenty)
    for x in (argumenty):
        print(x)
    print()
funckcja(12, 123, 412, "asdasd", 123.45, [12, 56])
funckcja(56, "wertsd")
funckcja()

