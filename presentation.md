- [Что такое рекурсия?](#org6d25bf6)
- [Правильная рекурсия](#orge26fd72)
- [Что такое стек вызовов?](#orgbf61030)
- [Что такое стек вызовов?](#org0708316)
- [Почему рекурсия это плохо](#org908873b)
- [Recursion depth](#orgce9c267)
- [Глубина рекурсии](#orge71a9ff)
- [Почему рекурсия это хорошо](#org9631d6e)
- [Вариант задачи для рекурсии](#orgd5a89ec)
- [решение на LISP](#org314c90e)
- [трассирование](#org6fefa6a)
- [Хвостовая рекурсия](#org22a05b5)
- [Оптимизация хвостовой рекурсии и почему её нет в Python](#org18f7493)
- [Пример когда рекурсия помогает](#org6bd0b9a)
- [Динамическое программирование](#orgcb5d5f3)
- [Кэширование](#org0a276ac)
- [Поиск приблизительно совпадающих строк](#org4e01ad9)
- [Рекурсивное решение](#org7141a28)
- [Динамическое программирование в действии](#org664a1c9)
- [Дополнительная литература](#org173fde4)
- [Вопросы-ответы](#orgf396ae6)



<a id="org6d25bf6"></a>

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


<a id="orge26fd72"></a>

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


<a id="orgbf61030"></a>

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


<a id="org0708316"></a>

# Что такое стек вызовов?

![img](/home/pimiento/yap/callstack.png)  


<a id="org908873b"></a>

# Почему рекурсия это плохо

-   стек вызовов растёт вместе с ростом глубины рекурсии
-   можно попасть в бесконечную рекурсию и истратить всю память на стек вызовов


<a id="orgce9c267"></a>

# Recursion depth

```python
def inf_counter(x):
    print(x)
    return inf_counter(x+1)
inf_counter(0)
```


<a id="orge71a9ff"></a>

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


<a id="org9631d6e"></a>

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


<a id="orgd5a89ec"></a>

# Вариант задачи для рекурсии

Попробуйте реализовать решение <span class="underline"><span class="underline">[этой задачи](https://github.com/pimiento/recursion_webinar/blob/master/cc.py)</span></span> без использования рекурсии \Winkey[][green!60!white]  


<a id="org314c90e"></a>

# решение на LISP

<span class="underline"><span class="underline">[count-change.lisp](https://gist.github.com/pimiento/05e2297358c65e2bf91eb71463747445)</span></span>  

![img](count-change-lisp.png)  


<a id="org6fefa6a"></a>

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


<a id="org22a05b5"></a>

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


<a id="org18f7493"></a>

# Оптимизация хвостовой рекурсии и почему её нет в Python

-   Интерпретаторы/компиляторы могут оптимизировать хвостовую рекурсию (Tail Call Optimization) и не делать записей в стек вызовов, а подменять переменные в стеке вызовов, таким образом код получится равнозначным обычному циклу
-   <span class="underline"><span class="underline">[Почему TCO нет и не будет в Python](https://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html)</span></span>


<a id="org6bd0b9a"></a>

# Пример когда рекурсия помогает

-   **Задача:** У вас есть вложенная структура данных и вы хотите просуммировать значения поля X во всех объектах этой структуры.
-   **Решение задачи:** <https://github.com/pimiento/recursion_webinar/blob/master/recursion_example.py>


<a id="orgcb5d5f3"></a>

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


<a id="org0a276ac"></a>

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


<a id="org4e01ad9"></a>

# Поиск приблизительно совпадающих строк

Возможные действия над строками, каждое действие будет иметь стоимость $1$  

-   ***замена*:** заменить один символ в строку A1 на символ из строки A2. ("мама" → "рама")
-   ***вставка*:** вставить один символ в строку A1 так чтобы она совпала с подстрокой A2. ("роза" → "проза")
-   ***удаление*:** удалить один символ в строке A1 так чтобы она совпала с подстрокой A2. ("гроза" → "роза")


<a id="org7141a28"></a>

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


<a id="org664a1c9"></a>

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


<a id="org173fde4"></a>

# Дополнительная литература

-   [SICP](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html)


<a id="orgf396ae6"></a>

# Вопросы-ответы

![img](questions.jpg)
