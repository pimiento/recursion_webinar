- [Что такое рекурсия?](#org78a0f29)
- [Правильная рекурсия](#org1973c12)
- [Что такое стек вызовов?](#org5af9cc9)
- [Что такое стек вызовов?](#orgcf60ef7)
- [Почему рекурсия это плохо](#orgdcea742)
- [Recursion depth](#org2fc2a6a)
- [Глубина рекурсии](#orgfc92033)
- [Почему рекурсия это хорошо](#orgf200652)
- [Вариант задачи для рекурсии](#org14a814e)
- [решение на LISP](#org01330b7)
- [трассирование](#orgc1f1bcc)
- [Хвостовая рекурсия](#orgc33da5c)
- [Оптимизация хвостовой рекурсии и почему её нет в Python](#org72f4b55)
- [Пример когда рекурсия помогает](#org35b494c)
- [Динамическое программирование](#orgf68f666)
- [Кэширование](#org93bc601)
- [Поиск приблизительно совпадающих строк](#org92203e3)
- [Рекурсивное решение](#org114f1a3)
- [Динамическое программирование в действии](#org37b4715)
- [Дополнительная литература](#orgdbf646a)
- [Вопросы-ответы](#orgfecba0c)



<a id="org78a0f29"></a>

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


<a id="org1973c12"></a>

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


<a id="org5af9cc9"></a>

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


<a id="orgcf60ef7"></a>

# Что такое стек вызовов?

![img](/home/pimiento/yap/callstack.png)  


<a id="orgdcea742"></a>

# Почему рекурсия это плохо

-   стек вызовов растёт вместе с ростом глубины рекурсии
-   можно попасть в бесконечную рекурсию и истратить всю память на стек вызовов


<a id="org2fc2a6a"></a>

# Recursion depth

```python
def inf_counter(x):
    print(x)
    return inf_counter(x+1)
inf_counter(0)
```


<a id="orgfc92033"></a>

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


<a id="orgf200652"></a>

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


<a id="org14a814e"></a>

# Вариант задачи для рекурсии

Попробуйте реализовать решение <span class="underline"><span class="underline">[этой задачи](https://github.com/pimiento/recursion_webinar/blob/master/cc.py)</span></span> без использования рекурсии \Winkey[][green!60!white]  


<a id="org01330b7"></a>

# решение на LISP

<span class="underline"><span class="underline">[count-change.lisp](https://gist.github.com/pimiento/05e2297358c65e2bf91eb71463747445)</span></span>  

![img](count-change-lisp.png)  


<a id="orgc1f1bcc"></a>

# трассирование

```python

def trace(f):
  indent = 0
  def g(*args, **kwargs):
    nonlocal indent
    print('|  ' * indent + '|--',
          f.__name__, *args, **kwargs)
    indent += 1
    value = f(*args, **kwargs)
    print('|  ' * indent + '|--',
          'return', repr(value))
    indent -= 1
    return value
  return g
cc = trace(cc)
count_change(10)
```


<a id="orgc33da5c"></a>

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


<a id="org72f4b55"></a>

# Оптимизация хвостовой рекурсии и почему её нет в Python

-   Интерпретаторы/компиляторы могут оптимизировать хвостовую рекурсию (Tail Call Optimization) и не делать записей в стек вызовов, а подменять переменные в стеке вызовов, таким образом код получится равнозначным обычному циклу
-   <span class="underline"><span class="underline">[Почему TCO нет и не будет в Python](https://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html)</span></span>


<a id="org35b494c"></a>

# Пример когда рекурсия помогает

-   **Задача:** У вас есть вложенная структура данных и вы хотите просуммировать значения поля X во всех объектах этой структуры.
-   **Решение задачи:** <https://github.com/pimiento/recursion_webinar/blob/master/recursion_example.py>


<a id="orgf68f666"></a>

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


<a id="org93bc601"></a>

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


<a id="org92203e3"></a>

# Поиск приблизительно совпадающих строк

Возможные действия над строками, каждое действие будет иметь стоимость $1$  

-   ***замена*:** заменить один символ в строку A1 на символ из строки A2. ("мама" → "рама")
-   ***вставка*:** вставить один символ в строку A1 так чтобы она совпала с подстрокой A2. ("роза" → "проза")
-   ***удаление*:** удалить один символ в строке A1 так чтобы она совпала с подстрокой A2. ("гроза" → "роза")


<a id="org114f1a3"></a>

# Рекурсивное решение

```python
def lev(a: str, b: str) -> int:
    if not a: return len(b)
    if not b: return len(a)
    return min([
        lev(a[1:],b[1:])+(a[0]!=b[0]),
        lev(a,b[1:])+1,
        lev(a[1:],b)+1
    ])

print(lev("salt", "foobar"))
print(lev("halt", "salt"))
```

    - 6
    - 1


<a id="org37b4715"></a>

# Динамическое программирование в действии

```python
def levenshtein(
    a: str, b: str, m: List[List[int]]
) -> int:
  for i in range(1, len(a)):
    for j in range(1, len(b)):
      m[i][j] = min(
        m[i-1][j-1] + (a[i] != b[j]),
        m[i][j-1] + 1,
        m[i-1][j] + 1
      )
  return m[len(a)-1][len(b)-1]
```


<a id="orgdbf646a"></a>

# Дополнительная литература

-   [SICP](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html)


<a id="orgfecba0c"></a>

# Вопросы-ответы

![img](questions.jpg)
