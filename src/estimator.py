from .calculate import result_calculator


def estimator(data):
    output = {
      'data': data,
      'impact': result_calculator(data, 10),
      'severeImpact': result_calculator(data, 50)
    }

    return output
