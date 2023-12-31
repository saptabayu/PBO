print("Konversi Suhu Kelvin")

# Entry
suhu = float(input("Masukkan suhu dalam Kelvin: "))

# rumus
F = (9/5 * (suhu - 273)) + 32
C = suhu - 273
R = (4/5 * (suhu - 273))

# output
print(f"{suhu} Kelvin sama dengan:")
print(f"{F} Fahrenheit")
print(f"{C} Celcius")
print(f"{R} Reamur")
