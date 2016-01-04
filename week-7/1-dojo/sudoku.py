def validate_array(array):
    size = len(array)
    try:
        validate_array_size(size)
        return sorted(array) == generate_valid_array(size)
    except TypeError:
        return False

def is_squared_number(number):
    return (number ** 0.5) % 1 != 0

def validate_array_size(size):
    if is_squared_number(size) or size==0:
        raise TypeError

def generate_valid_array(size):
    return list(range(1, size + 1))
