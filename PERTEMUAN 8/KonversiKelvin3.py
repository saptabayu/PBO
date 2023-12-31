print("Konversi Suhu Kelvin")

def get_celcius(suhu):
    C = float(suhu) - 273
    return C

def get_fahrenheit(suhu):
    F = (9/5 * (float(suhu) - 273)) + 32
    return F

def get_reamur(suhu):
    R = (4/5 * (float(suhu) - 273))
    return R

# Masukkan suhu dalam Kelvin
suhu = input("Masukkan suhu dalam Kelvin:")

# Menghitung hasil konversi
C = get_celcius(suhu)
F = get_fahrenheit(suhu)
R = get_reamur(suhu)

# Menampilkan hasil
print(f"{suhu} Kelvin sama dengan:")
print(f"{C} Celcius")
print(f"{F} Fahrenheit")
print(f"{R} Reamur")