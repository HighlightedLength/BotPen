import math

def get_default(key, *args):
    for ob in args:
        if key in ob:
            return ob[key]

def get_attribute_names(obj):
    return [a for a in dir(obj) if not callable(getattr(obj,a))]

def has_keys(obj):
    return ('keys' in dir(obj) and callable(getattr(obj,'keys')))

def defaults(constructor = None, *args):
    result = constructor() if constructor else type(args[0])()

    result_attr_keys = get_attribute_names(result)
    result_is_dict = has_keys(result)

    for arg in args:
        #handle attributes
        for key in result_attr_keys:
            val = getattr(arg, key, None)
            if val:
                setattr(result, key, val)

        #handle dict key/values
        if result_is_dict and has_keys(arg):
            for arg_key in arg.keys():
                result[arg_key] = arg[arg_key]

    return result

def fill_in(*args):
    return defaults(constructor = lambda:args[0], *args[1:])

def normalize_radians(radians):
    revs = math.floor(radians/(math.pi*2))
    return radians - 2 * math.pi * revs

def normalize_degrees(degrees):
    degrees = math.floor(degrees/(360*2))
    return radians - 2 * math.pi * degrees
