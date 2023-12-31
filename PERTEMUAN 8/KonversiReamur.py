print("Konversi Suhu Reamur")

# Entry
suhu = input ("Masukan suhu dalam Reamur:")

# rumus
F = (9/4 * float(suhu)) + 32
C = (5/4 * float (suhu))
K = (5/4 * float (suhu)) + 273

#output
print(suhu + " Reamur sama dengan ")
print(str(F) + " Fahrenheit ")
print(str(C) + " Celcius ")
print(str(K) + " Kelvin ")