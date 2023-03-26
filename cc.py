#!/usr/bin/env python3
"""
Число способов разменять сумму A с помощью N типов монет равняется

• числу способов разменять сумму A с помощью всех типов монет, кроме первого,
  плюс
• число способов разменять сумму A − D с использованием всех N типов монет,
  где D достоинство монет первого типа.

• Если A в точности равно 0, мы считаем, что имеем 1 способ размена.
• Если A меньше 0, мы считаем, что имеем 0 способов размена.
• Если N равно 0, мы считаем, что имеем 0 способов размена

Пример: 10 центов монетами 1 и 5

10/{1} + 5/{1, 5}
10/{} + 9/{1} + 5/{1} + 0/{1, 5}
0 + 9/{} + 8/{1} + 5/{} + 4/{1} + 1
0 + 0 + 8/{} + 8/{1} + 0 + 4/{} + 3/{1} + 1
0 + 0 + 0 + 8/{} + 7/{1} + 0 + 0 + 3/{} + 2/{1} + 1
0 + 0 + 0 + 0 + 7/{} + 6/{1} + 0 + 0 + 0 + 2/{} + 1/{1} + 1
0 + 0 + 0 + 0 + 0 + 6/{} + 5/{1} + 0 + 0 + 0 + 0 + 1/{} + 0/{1} + 1
0 + 0 + 0 + 0 + 0 + 0 + 5/{} + 4/{1} + 0 + 0 + 0 + 0  + 0 + 1 + 1
...
=> 3
"""

def first_denomination(kinds_of_coins):
    return {
        1: 1,
        2: 5,
        3: 10,
        4: 25,
        5: 50
    }[kinds_of_coins]


def cc(amount, kinds_of_coins):
    # base case
    if amount == 0:
        return 1
    if amount < 0 or kinds_of_coins == 0:
        return 0
    return (
        cc(amount, kinds_of_coins - 1) +
        cc(amount - first_denomination(kinds_of_coins), kinds_of_coins)
    )


def count_change(amount):
    return cc(amount, 5)


count_change(100)




### Tracing
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
