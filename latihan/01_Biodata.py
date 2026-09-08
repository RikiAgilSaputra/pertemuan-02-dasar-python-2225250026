# input data biodata
TAHUN_SEKARANG = 2026
nama = input ("Nama:")
nim = input ("NIM:")
kelas = input ("kelas:")
tahun_lahir = int(input("Tahun Lahir:"))

#fungsi perhitungan umur
umur = TAHUN_SEKARANG-tahun_lahir
print()

#tampilka hasil biodata
print (f"Nama: {nama}")
print (f"NIM: {nim}")
print (f"kelas: {kelas}")
print (f"Umur: {umur}")

#Umur merupakan perkiraan
#karena umur dihitun berdasarkan data statistik rata-rata
#bukan kepastian mutlak untuk setiap individu
