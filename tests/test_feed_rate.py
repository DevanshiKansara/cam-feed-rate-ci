import pytest

from src.feed_rate import convert_feed_rate


def test_mm_to_inch_conversion():
    result = convert_feed_rate(25.4, "mm/min", "in/min")
    assert result == pytest.approx(1.0)


def test_inch_to_mm_conversion():
    result = convert_feed_rate(1.0, "in/min", "mm/min")
    assert result == pytest.approx(25.4)


def test_large_feed_rate_conversion():
    result = convert_feed_rate(100.0, "mm/min", "in/min")
    assert result == pytest.approx(3.937, abs=0.001)


def test_zero_feed_rate():
    result = convert_feed_rate(0, "mm/min", "in/min")
    assert result == 0


def test_negative_feed_rate_is_rejected():
    with pytest.raises(ValueError):
        convert_feed_rate(-10, "mm/min", "in/min")


def test_unsupported_unit_is_rejected():
    with pytest.raises(ValueError):
        convert_feed_rate(100, "rpm", "mm/min")