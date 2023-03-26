def fahrenheit(celsius):
    """Convert degrees Celsius to degrees Fahrenheit"""
    return ((9 * celsius) / 5) + 32

def fahrenheit_list(celsius_lst):
    """Convert a list of temperatures in degrees Celsius to
    degrees Fahrenheit"""
    for i in range(0, len(celsius_lst)):
        celsius_lst[i] = fahrenheit(celsius_lst[i])
    return celsius_lst


a = [10, 15, 20]
b = fahrenheit_list(a)
print(b)