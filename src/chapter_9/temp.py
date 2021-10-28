def f_to_kelvin(degrees_f):
    return 273.15 + (degrees_f - 32) * 5 / 9


def c_to_kelvin(degrees_c):
    return 273.15 + degrees_c


abs_temperature = f_to_kelvin
print(abs_temperature(32))

abs_temperature = c_to_kelvin
print(abs_temperature(0))

t = {'FtoK': f_to_kelvin, 'CtoK': c_to_kelvin}
print(t['FtoK'](32))
print(t['CtoK'](0))

t2 = {'FtoK': lambda deg_f: 273.15 + (deg_f - 32) * 5 / 9,
      'CtoK': lambda deg_c: 273.15 + deg_c}
print(t2['FtoK'](32))
print(t2['CtoK'](0))
