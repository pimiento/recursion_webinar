- [Что такое рекурсия?](#org881fa9b)
- [Правильная рекурсия](#orgeee7545)
- [Что такое стек вызовов?](#orgdd88ada)
- [Что такое стек вызовов?](#org1576f9f)
- [Почему рекурсия это плохо](#orga87ea64)
- [Recursion depth](#org52484e1)
- [Глубина рекурсии](#org22382d3)
- [Почему рекурсия это хорошо](#org821130e)
- [Варианты задач для рекурсии. Сортировка](#org7b410da)
- [Варианты задач для рекурсии. Графы](#orgabea9c4)
- [Варианты задач для рекурсии. Графы](#org51d8fcc)
- [Вариант задачи для рекурсии](#orgb5c8ab9)
- [решение на LISP](#org3135003)
- [трассировка](#org3047eca)
- [Хвостовая рекурсия](#org9736ed5)
- [Оптимизация хвостовой рекурсии и почему её нет в Python](#org3e563ea)
- [Пример когда рекурсия помогает](#orgcb7fac9)
- [Динамическое программирование](#org866a89b)
- [Динамическое программирование. Кэширование](#orgec07fc9)
- [Поиск приблизительно совпадающих строк](#org219a18d)
- [Рекурсивное решение](#org06effba)
- [Динамическое программирование в действии](#org77bbf42)
- [Дополнительная литература](#org19b00be)
- [Вопросы-ответы](#org3ec8414)



<a id="org881fa9b"></a>

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


<a id="orgeee7545"></a>

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


<a id="orgdd88ada"></a>

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


<a id="org1576f9f"></a>

# Что такое стек вызовов?

![img](/home/pimiento/yap/callstack.png)  


<a id="orga87ea64"></a>

# Почему рекурсия это плохо

-   стек вызовов растёт вместе с ростом глубины рекурсии
-   можно попасть в бесконечную рекурсию и истратить всю память на стек вызовов


<a id="org52484e1"></a>

# Recursion depth

```python
def inf_counter(x):
    print(x)
    return inf_counter(x+1)
inf_counter(0)
```


<a id="org22382d3"></a>

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


<a id="org821130e"></a>

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


<a id="org7b410da"></a>

# Варианты задач для рекурсии. Сортировка

```python

def sort_alg(L: List[int]]) -> List:
    if L:
        return (
            sort_alg(
        [e for e in L[1:] if e<L[0]]
            ) +
            L[0:1] +
            sort_alg(
        [e for e in L[1:] if e>=L[0]]
            )
        )
    return []

```


<a id="orgabea9c4"></a>

# Варианты задач для рекурсии. Графы

```python

fname = "graph.png"
G = (
    nx.internet_as_graphs
    .random_internet_as_graph(
        n=50, seed=42
    )
)

```

![img](graph.png)  


<a id="org51d8fcc"></a>

# Варианты задач для рекурсии. Графы

```python

def DFS(G, V, p=None):
    if p is None:
        p = []
    p += [V]
    for n in G[V]:
        if n not in p:
            p = DFS(G, n, p)
    return p

```


<a id="orgb5c8ab9"></a>

# Вариант задачи для рекурсии

Попробуйте реализовать решение <span class="underline"><span class="underline">[этой задачи](https://github.com/pimiento/recursion_webinar/blob/master/cc.py)</span></span> без использования рекурсии \Winkey[][green!60!white]  


<a id="org3135003"></a>

# решение на LISP

<span class="underline"><span class="underline">[count-change.lisp](https://gist.github.com/pimiento/05e2297358c65e2bf91eb71463747445)</span></span>  

![img](count-change-lisp.png)  


<a id="org3047eca"></a>

# трассировка

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


<a id="org9736ed5"></a>

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


<a id="org3e563ea"></a>

# Оптимизация хвостовой рекурсии и почему её нет в Python

-   Интерпретаторы/компиляторы могут оптимизировать хвостовую рекурсию (Tail Call Optimization) и не делать записей в стек вызовов, а подменять переменные в стеке вызовов, таким образом код получится равнозначным обычному циклу
-   <span class="underline"><span class="underline">[Почему TCO нет и не будет в Python](https://neopythonic.blogspot.com/2009/04/final-words-on-tail-calls.html)</span></span>


<a id="orgcb7fac9"></a>

# Пример когда рекурсия помогает

-   **Задача:** У вас есть вложенная структура данных и вы хотите просуммировать значения поля X во всех объектах этой структуры.
-   **Решение задачи:** <https://github.com/pimiento/recursion_webinar/blob/master/recursion_example.py>


<a id="org866a89b"></a>

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


<a id="orgec07fc9"></a>

# Динамическое программирование. Кэширование

```python
cache = {0: 1, 1: 1}

def fib(n):
    if n not in cache:
        cache[n] = \
            fib(n=n-1) + fib(n=n-2)
    return cache[n]

```

![img](cached_fibonacci.png)  


<a id="org219a18d"></a>

# Поиск приблизительно совпадающих строк

Возможные действия над строками, каждое действие будет иметь стоимость $1$  

-   ***замена*:** заменить один символ в строку A1 на символ из строки A2. ("мама" → "рама")
-   ***вставка*:** вставить один символ в строку A1 так чтобы она совпала с подстрокой A2. ("роза" → "проза")
-   ***удаление*:** удалить один символ в строке A1 так чтобы она совпала с подстрокой A2. ("гроза" → "роза")


<a id="org06effba"></a>

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


<a id="org77bbf42"></a>

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


<a id="org19b00be"></a>

# Дополнительная литература

-   [Графы для самых маленьких: DFS](https://habr.com/ru/post/200074/)
-   [SICP](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html)


<a id="org3ec8414"></a>

# Вопросы-ответы

![img](questions.jpg)
