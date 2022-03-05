- [Что такое рекурсия?](#org0f193e6)
- [Правильная рекурсия](#org9bd6384)
- [Что такое стек вызовов?](#org11be0ef)
- [Что такое стек вызовов?](#org45a10a4)
- [Почему рекурсия это плохо](#org8eb3f24)
- [Recursion depth](#org10d38da)
- [Глубина рекурсии](#org35bc8e2)
- [Почему рекурсия это хорошо](#org99bbca5)
- [Вариант задачи для рекурсии](#orga01172f)
- [Хвостовая рекурсия](#org6b4c978)
- [Оптимизация хвостовой рекурсии и почему её нет в Python](#org1a26463)
- [Пример когда рекурсия помогает](#orgbf8722f)
- [Дополнительная литература](#org3cfe77b)
- [Динамическое программирование](#org28173f2)
- [Кэширование](#org2e7ee6a)
- [Поиск приблизительно совпадающих строк](#org8dae530)
- [Рекурсивное решение](#orgde58890)
- [Динамическое программирование в действии](#orge0f0987)
- [Вопросы-ответы](#orgb593a5c)



<a id="org0f193e6"></a>

# Что такое рекурсия?

Приём в программировании, когда задача может быть разделена на несколько таких же, но проще, задач.

```python
def pow(x, n):
    # возведение числа в степень это
    # умножение числа на число
    # в степени n-1
    if n == 0:
        return 1
    return x * pow(x, n-1)
```


<a id="org9bd6384"></a>

# Правильная рекурсия

```python
def pow(x, n):
    # хорошо бы проверить,
    # что база достижима
    assert n >= 0
    # base case / база рекурсии
    if n == 0:
        return 1
    # recursive case / шаг рекурсии
    return x * pow(x, n-1)
```


<a id="org11be0ef"></a>

# Что такое стек вызовов?

```python
def foo(msg):
    print '{} foo'.format(msg)

def main():
    msg = 'hello'
    foo(msg)

if __name__ == '__main__':
    main()
```


<a id="org45a10a4"></a>

# Что такое стек вызовов?

![img](/home/pimiento/yap/callstack.png)


<a id="org8eb3f24"></a>

# Почему рекурсия это плохо

-   стек вызовов растёт вместе с ростом глубины рекурсии
-   можно попасть в бесконечную рекурсию и истратить всю память на стек вызовов


<a id="org10d38da"></a>

# Recursion depth

```python
def inf_counter(x):
    print(x)
    return inf_counter(x+1)
f(0)
```


<a id="org35bc8e2"></a>

# Глубина рекурсии

```python
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(
    sys.getrecursionlimit() + 234
)
print(sys.getrecursionlimit())
```

    1000
    1234


<a id="org99bbca5"></a>

# Почему рекурсия это хорошо

Помогает описать решение задачи понятным языком

```python
# n! = n * (n-1)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
```

    120


<a id="orga01172f"></a>

# Вариант задачи для рекурсии

Попробуйте реализовать решение <span class="underline"><span class="underline">[этой задачи](https://gist.github.com/pimiento/201225ad1a70432060531676dd3e6239)</span></span> без использования рекурсии \Winkey[][green!60!white]


<a id="org6b4c978"></a>

# Хвостовая рекурсия

Рекурсия, не требующая действий с возвращённым результатом из шага рекурсии.

```python
def factorial(n, collected=1):
    if n == 0:
        return collected
    return factorial(n-1, collected*n)

print(factorial(5))
```

    120


<a id="org1a26463"></a>

# Оптимизация хвостовой рекурсии и почему её нет в Python

-   Интерпретаторы/компиляторы могут оптимизировать хвостовую рекурсию (Tail Call Optimization) и не делать записей в стек вызовов, а подменять переменные в стеке вызовов, таким образом код получится равнозначным обычному циклу
-   <span class="underline"><span class="underline">[Почему TCO нет и не будет в Python](https://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html)</span></span>


<a id="orgbf8722f"></a>

# Пример когда рекурсия помогает

-   **Задача:** У вас есть вложенная структура данных и вы хотите просуммировать значения поля X во всех объектах этой структуры.
-   **Решение задачи:** <https://gist.github.com/pimiento/bc4d5800f66541cb59ea388c1c3c263c>


<a id="org3cfe77b"></a>

# Дополнительная литература

-   [SICP](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html)


<a id="org28173f2"></a>

# Динамическое программирование

```python

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n=n-1) + fib(n=n-2)

```

![img](fibonacci.png)


<a id="org2e7ee6a"></a>

# Кэширование

```python
cache = {0: 1, 1: 1}

def fib(n):
    if n not in cache:
        cache[n] = \
            fib(n=n-1) + fib(n=n-2)
    return cache[n]

```

![img](cached_fibonacci.png)


<a id="org8dae530"></a>

# Поиск приблизительно совпадающих строк

Возможные действия над строками, каждое действие будет иметь стоимость \(1\)

-   ***замена*:** заменить один символ в строку A1 на символ из строки A2. ("мама" → "рама")
-   ***вставка*:** вставить один символ в строку A1 так чтобы она совпала с подстрокой A2. ("роза" → "проза")
-   ***удаление*:** удалить один символ в строке A1 так чтобы она совпала с подстрокой A2. ("гроза" → "роза")


<a id="orgde58890"></a>

# Рекурсивное решение

```python
def lev(a: str, b: str) -> int:
    if not a: return len(b)
    if not b: return len(a)
    return min([
        lev(a[1:],b[1:])+(a[0]!=b[0]),
        lev(a[1:],b)+1,
        lev(a,b[1:])+1
    ])

print(lev("salt", "foobar"))
print(lev("halt", "salt"))
```

    - 6
    - 1


<a id="orge0f0987"></a>

# Динамическое программирование в действии

```python
def levenshtein(a: str, b: str, m: List[List[int]]) -> int:
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            m[i][j] = min(
                m[i-1][j-1] + (a[i] != b[j]),
                m[i][j-1] + 1,
                m[i-1][j] + 1
            )
    return m[len(a)-1][len(b)-1]
```


<a id="orgb593a5c"></a>

# Вопросы-ответы

![img](questions.jpg)
