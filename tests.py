import pytest


def calculate_distance(sites: dict) -> dict:
    distances = {}
    for site_key, site_values in sites.items():
        site_x, site_y = site_values[0], site_values[1]
        site_distances = {}
        for other_site_key, other_site_value in sites.items():
            if site_key == other_site_key:
                continue
            other_site_x, other_site_y = other_site_value[0], other_site_value[1]
            distance = ((site_x - other_site_x) ** 2 + (site_y - other_site_y) ** 2) ** 0.5
            site_distances[f"TO {other_site_key}"] = distance
        distances[site_key] = site_distances
    return distances


def is_point_inside_circle(point: tuple, radius: float) -> bool:
    distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
    return radius >= distance


#Тесты для функции calculate_distance

def test_calculate_distance_basic():

    sites = {'A': (0, 0), 'B': (3, 4)}
    res = calculate_distance(sites)
    assert res['A']['TO B'] == pytest.approx(5.0)
    assert res['B']['TO A'] == pytest.approx(5.0)


def test_calculate_distance_three_points():

    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }
    res = calculate_distance(sites)
    assert 'Moscow' in res
    assert 'TO London' in res['Moscow']
    assert 'TO Paris' in res['Moscow']
    assert 'TO Moscow' not in res['Moscow']


def test_calculate_distance_same_coordinates():

    sites = {'Point1': (10, 10), 'Point2': (10, 10)}
    res = calculate_distance(sites)
    assert res['Point1']['TO Point2'] == 0.0


def test_calculate_distance_negative_coordinates():

    sites = {'Start': (-1, -1), 'End': (-4, -5)}
    res = calculate_distance(sites)
    assert res['Start']['TO End'] == pytest.approx(5.0)


def test_calculate_distance_empty_dict():

    sites = {}
    res = calculate_distance(sites)
    assert res == {}



def test_point_strictly_inside_circle():

    assert is_point_inside_circle((10, 10), 42) is True


def test_point_outside_circle():
    assert is_point_inside_circle((40, 40), 42) is False


def test_point_on_circle_boundary():

    assert is_point_inside_circle((3, 4), 5.0) is True


def test_point_at_origin():

    assert is_point_inside_circle((0, 0), 10) is True


def test_point_zero_radius():

    assert is_point_inside_circle((0, 0), 0) is True
    assert is_point_inside_circle((1, 1), 0) is False