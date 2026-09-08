#deklarasi nilai variabel
KELVIN_OFFSET = 273.15

#input nilai suhu dalam celcius
suhu = input("masukkan suhu dalam celcius:")

#konversi suhu ke fahrenheit
fahrenheit = (9/5) * float(suhu) + 32

#konversi suhu ke kelvin
kelvin = float(suhu) + KELVIN_OFFSET

print(f"Konversi suhu ke dalam satuan fahrenheit = {fahrenheit:.2f}") 
print(f"Konversi suhu ke dalam satuan kelvin = {kelvin:.2f}") 
