# Homework 1

Преобразование строк матрицы, основанное на исключении неизвестных (приведении к треугольному виду), используется при вычислении определителя, поиска решений системы линейных алгебраических уравнений, нахождении обратной матрицы, вычислении ранга матрицы.

Разработайте приложение, в котором разработана функция, реализующая это преобразование. С помощью этой функции реализуйте методы:

* вычисления определителя квадратной матрицы
* нахождения обратной матрицы
* поиска единственного решения системы линейных алгебраических уравнений
* проверку совместности системы с помощью теоремы Кронекера-Капелли. 

Ваша программа на вход получает файл, в котором содержаться матрицы или системы (размерность, количество матриц или систем произвольно и не фиксировано). Элементы матриц записаны построчно.

Примерный формат входного файла:

```
A=(2 5 7; 6 3 4; 5 -2 -3)
%
A=(2 3 -1; 1 -2 1; 1 0 2)
B=(9 3 2)
%
```

Записи разделяются `%`. Если запись содержит только матрицу, то для этой матрицы, если это возможно, необходимо найти определитель, обратную матрицу, ранг матрицы. Если запись содержит матрицу и вектор свободных слагаемых, то данная запись соответствует СЛАУ. Для заданной системы необходимо проверить совместность, если решение единственно, найти это решение методом Гаусса.

Результатом работы вашей программы является файл, в котором для каждой записи из исходного файла приведен результат нахождения соответствующих задач.