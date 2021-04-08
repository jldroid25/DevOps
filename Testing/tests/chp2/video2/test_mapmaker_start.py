from scripts.chp2.video2.mapmaker_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Den Haag", 14.7167, 17.4672)
    assert p1.get_lat_long() == (14.7167, 17.4672)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("London UK", 12.11386, -555.08269)
    assert str(exp.value) == 'Invalid Latitude, Longitude combination'

    with pytest.raises(ValueError) as exp:
        Point(5, 12.11386, -55.08269)
    assert str(exp.value) == 'City name provided must be a string'
