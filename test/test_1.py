from src.day_1 import compare_lists, generate_similarity_score, get_lists


def test_part_1():
    assert compare_lists(*get_lists()) == 2264607


def test_part_2():
    assert generate_similarity_score(*get_lists()) == 19457120
