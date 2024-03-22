def is_integer(value):
    '''
    Used to evaluate in preprocessing if an ID is instance of int.
    '''
    try:
        return int(value)
    except ValueError:
        return None