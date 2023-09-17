def oblicz_bmi(masa, wzrost):
    # Obliczamy BMI jako masa / (wzrost w metrach)^2
    bmi = masa / (wzrost ** 2)
    return bmi

def interpretuj_bmi(bmi):
    if bmi < 16:
        return "Wygłodzenie"
    elif 16 <= bmi < 16.9:
        return "Wychudzenie"
    elif 17 <= bmi < 18.4:
        return "Niedowaga"
    elif 18.5 <= bmi < 24.9:
        return "Prawidłowa waga"
    elif 25 <= bmi < 29.9:
        return "Nadwaga"
    elif 30 <= bmi < 34.9:
        return "I stopień otyłości"
    elif 35 <= bmi < 39.9:
        return "II stopień otyłości (otyłość kliniczna)"
    else:
        return "III stopień otyłości (otyłość skrajna)"

# Pobieramy dane od użytkownika
masa = float(input("Podaj swoją masę ciała (w kilogramach): "))
wzrost = float(input("Podaj swój wzrost (w metrach): "))

# Obliczamy BMI
bmi = oblicz_bmi(masa, wzrost)

# Interpretujemy wynik
interpretacja = interpretuj_bmi(bmi)

# Wyświetlamy wynik
print(f"Twoje BMI wynosi: {bmi}")
print(f"Interpretacja BMI: {interpretacja}")
