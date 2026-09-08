BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

#input data
nama = input("nama")
nilai_tugas = float(input("Nilai tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))
nilai_akhir = (
nilai_tugas * BOBOT_TUGAS
+ nilai_uts * BOBOT_UTS
+ nilai_uas * BOBOT_UAS
)

#tampilkan hasil
print(f"Nilai akhir = {nilai_akhir:.2f}")
print ("nilai tugas")
print ("nilai uts")
print (f"nilai uas = {nilai_uas:.2f}")

