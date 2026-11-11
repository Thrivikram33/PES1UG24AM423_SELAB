
import pytest

from house_painting_quote import painting_quote, paint_litres, crew_days


# ---------------- PAINTING QUOTE BRANCH TESTS ----------------

def test_unknown_paint():
    with pytest.raises(ValueError):
        painting_quote("unknown", 500, 2, False)


def test_valid_paint():
    assert painting_quote("emulsion", 500, 2, False) == 20000


def test_invalid_area():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 0, 2, False)


def test_invalid_coats():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 500, 0, False)


def test_valid_area_and_coats():
    assert painting_quote("emulsion", 500, 2, False) == 20000


def test_distemper_exterior():
    with pytest.raises(ValueError):
        painting_quote("distemper", 500, 2, True)


def test_exterior_non_distemper():
    assert painting_quote("emulsion", 500, 1, True) == 12500


def test_interior():
    assert painting_quote("emulsion", 500, 1, False) == 10000


def test_large_area_discount():
    assert painting_quote("emulsion", 2500, 2, False) == 90000


def test_small_area_no_discount():
    assert painting_quote("emulsion", 500, 2, False) == 20000


def test_minimum_cost():
    assert painting_quote("distemper", 10, 1, False) == 5000


def test_cost_above_minimum():
    assert painting_quote("emulsion", 500, 1, False) == 10000


# ---------------- PAINT LITRES BRANCH TESTS ----------------

def test_smooth_surface():
    assert paint_litres(200, 1, "smooth") == 2


def test_rough_surface():
    assert paint_litres(120, 1, "rough") == 2


def test_unknown_surface():
    with pytest.raises(ValueError):
        paint_litres(200, 1, "unknown")


def test_exact_coverage():
    assert paint_litres(200, 1, "smooth") == 2


def test_remaining_coverage():
    assert paint_litres(201, 1, "smooth") == 3


# ---------------- CREW DAYS BRANCH TESTS ----------------

def test_invalid_painters():
    with pytest.raises(ValueError):
        crew_days(800, 0, False)


def test_valid_painters():
    assert crew_days(800, 2, False) == 1


def test_exact_workload():
    assert crew_days(800, 2, False) == 1


def test_remaining_workload():
    assert crew_days(801, 2, False) == 2


def test_wallpaper_removal():
    assert crew_days(800, 2, True) == 3


def test_no_wallpaper_removal():
    assert crew_days(800, 2, False) == 1
