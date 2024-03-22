def is_integer(value):
    try:
        return int(value)
    except ValueError:
        return None