def result_calculator(data, multiplier):
    impact = {}
    #  number of infected people in days from now
    reported_cases = data.get('reportedCases')
    impact['currentlyInfected'] = reported_cases * multiplier
    total_numbe_of_days = data['timeToElapse']

    periods_multplier = {'weeks': 7, 'months': 30}
    if data['periodType'] in periods_multplier.keys():
        total_numbe_of_days = data['timeToElapse'] * periods_multplier[
            data['periodType']]

    number_of_doubles = total_numbe_of_days // 3
    impact['infectionsByRequestedTime'] = impact[
        'currentlyInfected'] * (2**number_of_doubles)

    #  Challenge 2
    #  estimated severe positive cases that require hospitalization to recover.
    impact['severeCasesByRequestedTime'] = int(
      impact['infectionsByRequestedTime'] * 0.15
    )
    #  available hospital beds for severe positive patients
    available_beds = (
      data['totalHospitalBeds'] * 0.35
    )
    impact['hospitalBedsByRequestedTime'] = int(
        available_beds - impact['severeCasesByRequestedTime']
    )

    # Challenge 3
    # number of severe positive cases that will require ICU care.
    impact['casesForICUByRequestedTime'] = int(
      impact['infectionsByRequestedTime'] * 0.05
    )
    # number of severe positive cases that will require ventilators.
    impact['casesForVentilatorsByRequestedTime'] = int(
      impact['infectionsByRequestedTime'] * 0.02
    )
    # money the economy is likely to lose daily
    impact['dollarsInFlight'] = float(int((
        impact['infectionsByRequestedTime'] * 0.65 * 1.5
    ) / 30))

    return impact
