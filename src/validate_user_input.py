def get_region_data(data):
    """
    Takes in data and returns all the allowed fields
    in a dict format
    """
    data = {
        "region": data.get('region'),
        "periodType": data.get('periodType'),
        "timeToElapse": data.get('timeToElapse'),
        "reportedCases": data.get('reportedCases'),
        "population": data.get('population'),
        "totalHospitalBeds": data.get('totalHospitalBeds')
    }
    return data


def validate_input_data(data):
    """
    Takes in user input data
    Checks if all the keys are provided
    Raise key error if a key is missing
    Returns a validated data in a dict format
    """
    cleaned_data = {}
    for key in data:
        if data[key] is None:
            assert False, key + ' key is missing'
        else:
            cleaned_data[key] = data[key]
    return cleaned_data


def validate_input_type(data):
    """
    Takes in data
    Checks if data types provided are correct
    Asserts false with wrong data type
    """
    types = {
        "region": dict,
        "periodType": str,
        "timeToElapse": int,
        "reportedCases": int,
        "population": int,
        "totalHospitalBeds": int
    }
    for k, v in data.items():
        if not isinstance(v, types[k]):
            assert False, f'{k} must be a {types[k].__name__} value'
