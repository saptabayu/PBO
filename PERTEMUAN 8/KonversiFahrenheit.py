print("Konversi Suhu Fahrenheit")

# Entry
suhu = float(input("Masukkan suhu dalam Fahrenheit: "))

# rumus
C = (5/9 * (suhu - 32))
R = (4/9 * (suhu - 32))
K = (5/9 * (suhu - 32)) + 273

# output
print(f"{suhu} Fahrenheit sama dengan:")
print(f"{C} Celcius")
print(f"{R} Reamur")
print(f"{K} Kelvin")