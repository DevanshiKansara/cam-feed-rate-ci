def convert_feed_rate(value, from_unit, to_unit):
    """
    Convert feed rate between mm/min and in/min.
    """

    if value < 0:
        raise ValueError("Feed rate cannot be negative.")

    if from_unit == to_unit:
        return value

    if from_unit == "mm/min" and to_unit == "in/min":
        return value / 25.4

    if from_unit == "in/min" and to_unit == "mm/min":
        return value * 25.4

    raise ValueError("Unsupported unit.")
