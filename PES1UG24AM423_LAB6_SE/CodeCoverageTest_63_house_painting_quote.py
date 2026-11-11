
import pytest

from house_painting_quote import painting_quote, paint_litres, crew_days


# ---------------- PAINTING QUOTE TESTS ----------------

def test_distemper_interior():
    assert painting_quote("distemper", 500, 2, False) == 12000


def test_emulsion_interior():
    assert painting_quote("emulsion", 500, 2, False) == 20000


def test_enamel_exterior():
    assert painting_quote("enamel", 500, 2, True) == 32500


def test_unknown_paint():
    with pytest.raises(ValueError):
        painting_quote("unknown", 500, 2, False)


def test_invalid_area():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 0, 2, False)


def test_invalid_coats():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 500, 0, False)


def test_distemper_exterior():
    with pytest.raises(ValueError):
        painting_quote("distemper", 500, 2, True)


def test_minimum_cost():
    assert painting_quote("distemper", 10, 1, False) == 5000


def test_large_area_discount():
    assert painting_quote("emulsion", 2500, 2, False) == 90000


def test_exterior_cost_without_distemper():
    assert painting_quote("emulsion", 500, 1, True) == 12500


# ---------------- PAINT LITRES TESTS ----------------

def test_smooth_litres():
    assert paint_litres(200, 1, "smooth") == 2


def test_rough_litres():
    assert paint_litres(120, 1, "rough") == 2


def test_smooth_litres_rounding():
    assert paint_litres(101, 1, "smooth") == 2


def test_unknown_surface():
    with pytest.raises(ValueError):
        paint_litres(200, 1, "uneven")


# ---------------- CREW DAYS TESTS ----------------

def test_crew_days_exact():
    assert crew_days(800, 2, False) == 1


def test_crew_days_rounding():
    assert crew_days(801, 2, False) == 2


def test_crew_days_with_wallpaper_removal():
    assert crew_days(800, 2, True) == 3


def test_invalid_painters():
    with pytest.raises(ValueError):
        crew_days(800, 0, False)
