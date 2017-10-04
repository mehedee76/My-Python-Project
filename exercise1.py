def cel_to_fahr(celsius):
    fahrenhite = float (celsius) * 32
    return  fahrenhite
celsius = input("Enter the temparature in celsius: ")
print(cel_to_fahr(celsius) + 'f')
