print("Konversi Suhu Celcius")

def get_fahrenheit(suhu):
    F = (5/9 * float(suhu)) + 32
    return F

def get_reamur(suhu):
    R = (4/5 * float(suhu))
    return R

def get_kelvin(suhu):
    K = float(suhu) + 273
    return K

# Masukan suhu dalam Celcius
suhu = input("Masukkan suhu dalam Celcius:")

# Menghitung hasil konversi
F = get_fahrenheit(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

# Menampilkan hasil
print(f"{suhu} Celsius sama dengan:")
print(f"{F} Fahrenheit")
print(f"{R} Reamur")
print(f"{K} Kelvin")