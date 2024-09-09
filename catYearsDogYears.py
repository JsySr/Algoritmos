def calculate_pet_ages(humanYears):
    # Calcular los años de los gatos y los perros
    if humanYears == 1:
        catYears = dogYears = 15
    elif humanYears == 2:
        catYears = dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso:
humanYears = int(input("Dame los años humanos: "))

ages = calculate_pet_ages(humanYears)

# Imprime las edades formateadas
print(f"Un animal con {ages[0]} años humanos tendría: ")
print(f"- {ages[1]} años de gato ")
print(f"- {ages[2]} años de perro ")

# Imprime el tipo de dato devuelto por la función
print(f"El tipo de dato devuelto es {type(ages)}")
