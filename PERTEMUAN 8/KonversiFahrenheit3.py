print("Konversi Suhu Fahrenheit")

def get_celcius(suhu):
    C = (5/9 * (float(suhu) - 32))
    return C

def get_reamur(suhu):
    R = (4/9 * (float(suhu) - 32))
    return R

def get_kelvin(suhu):
    K = (5/9 * (float(suhu) - 32)) + 273
    return K

# Masukkan suhu dalam Fahrenheit
suhu = input("Masukkan suhu dalam Fahrenheit:")

# Menghitung hasil konversi
C = get_celcius(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

# Menampilkan hasil
print(f"{suhu} Fahrenheit sama dengan:")
print(f"{C} Celcius")
print(f"{R} Reamur")
print(f"{K} Kelvin")