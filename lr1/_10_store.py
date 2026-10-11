#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    # Есть словарь кодов товаров
def lab_10():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }
    # Есть словарь списков количества товаров на складе.
    # Каждый товар может лежать в нескольких местах (партиях) с разной ценой.

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }







    # Рассчитать на какую сумму лежит каждого товара на складе
    # и вывести в формате
    #   <товар> - <кол-во> шт, стоимость <сумма> руб

    # Пример:
    #   Лампа - 27 шт, стоимость 1134 руб

    # TODO здесь ваш код

    for product_name,product_code in goods.items():
        product_value_sum = sum(item["quantity"]*item["price"] for item in store[f"{product_code}"])
        product_quantity = sum(item["quantity"] for item in store[f"{product_code}"])
        print(f"{product_name} - {product_quantity} шт, стоимость {product_value_sum} руб")
