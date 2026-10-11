#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
def lab_0():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    # Составим словарь словарей расстояний между ними
    # расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    calculate_distance(sites)
    # TODO здесь заполнение словаря
def calculate_distance(sites:dict):
    distances = {}
    for site_key,sites_values in sites.items():
        site_x = sites_values[0]
        site_y = sites_values[1]
        site_distances={}
        for other_site_key, other_site_value in sites.items():
            repeat_key = f"TO {other_site_key}"
            if site_key is other_site_key:
                continue
            else:
                other_site_x = other_site_value[0]
                other_site_y = other_site_value[1]
                distance = ((site_x - other_site_x) ** 2 + (site_y - other_site_y) ** 2) ** 0.5
            site_distances[f"TO {other_site_key}"] = distance
            distances[f"{site_key}"] =  site_distances
    else:
        for key,value in distances.items():
            print(key,value)
    
