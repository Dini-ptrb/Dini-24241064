# Meminta input dari pengguna dama Fahrenheit
fahrenheit = float(input("Masukkan temperatur dalam Fahrenheit"))

# Mengoversi Fahrenheit ke Celcius
celsius = (fahrenheit - 32) * 5/9

# Menampilkan hasil konversi
print(f"{fahrenheit} derajat Fahrenheit sama dengan {celsius:.2f} derajat celsius.")