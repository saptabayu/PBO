print("Konversi Suhu Reamur")

def get_celcius(suhu):
    C = (5/4) * float(suhu)
    return C

def get_fahrenheit(suhu):
    F = (9/4 * float(suhu)) + 32
    return F

def get_kelvin(suhu):
    K = (5/4 * float(suhu)) + 273
    return K

# Masukkan suhu dalam Reamur
suhu = input("Masukkan suhu dalam Reamur:")

# Menghitung hasil konversi
C = get_celcius(suhu)
F = get_fahrenheit(suhu)
K = get_kelvin(suhu)

# Menampilkan hasil
print(f"{suhu} Reamur sama dengan:")
print(f"{C} Celcius")
print(f"{F} Fahrenheit")
print(f"{K} Kelvin")
