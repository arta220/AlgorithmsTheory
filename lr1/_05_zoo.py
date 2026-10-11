#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def lab_5():
    # Есть список животных в зоопарке
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    # Посадите медведя (bear) между львом и кенгуру
    # и выведите список на консоль
    # TODO здесь ваш код
    zoo.insert(1, 'bear')

    # Добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark']
    # и выведите список на консоль
    # TODO здесь ваш код
    zoo = zoo+birds
    print(zoo)
    # Уберите слона (elephant) из зоопарка
    # и выведите список на консоль
    # TODO здесь ваш код
    zoo.remove('elephant')
    print(zoo)
    # Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
    # TODO здесь ваш код
    print(zoo.index('lion')+1, zoo.index('lark')+1)
