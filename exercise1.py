def cel_to_fahr(celsius):
    fahrenhite = float (celsius) * 9
    return  (fahrenhite / 5) + 32
celsius = input("Enter the temparature in celsius: ")
print("%.2f" % cel_to_fahr(celsius))


def fahr_to_cel(fahr):
    celcius =  (float(fahr) - 32) * 5
    return  (celcius / 9)
fahr = input("Enter the temparature in Fahrenheit: ")
print("%.2f" % fahr_to_cel(fahr))
