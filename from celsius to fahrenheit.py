def Celsius(temp):
    """Convert degrees Celsius to degrees Fahrenheit"""
    return ((1.8 * temp)) + 32

def celsius_list(celsius_lst):
    """Convert a list of temperatures in degrees Celsius to
    degrees Fahrenheit"""
    for i in range(0, len(celsius_lst)):
        celsius_lst[i] = Celsius(celsius_lst[i])
    return celsius_lst

a = [-40, 0, -20]
print(celsius_list(a))
