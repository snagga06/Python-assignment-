def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return round(value, 2)

    # Convert to Celsius
    if from_unit == 'fahrenheit':
        value = (value - 32) * 5 / 9
    elif from_unit == 'kelvin':
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == 'fahrenheit':
        value = value * 9 / 5 + 32
    elif to_unit == 'kelvin':
        value = value + 273.15

    return round(value, 2)
