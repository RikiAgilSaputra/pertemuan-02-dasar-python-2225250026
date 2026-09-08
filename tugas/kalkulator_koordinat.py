#input koordinat titik A dan titik B
print("KALKULATOR KOORDINAT DUA TITIK")
x_titik_A = float(input("masukkan koordinat x (absis)untuk koordinat titik A:"))
y_titik_A = float(input("masukkan koordinat y (ordinat)untuk koordinat titik A:"))
x_titik_B = float(input("masukkan koordinat x (absis)untuk koordinat titik B:"))
y_titik_B = float(input("masukkan koordinat y (ordinat)untuk koordinat titik B:"))

#hitung perubahan koordinat, jarak, dan titik tengah
dx = x_titik_B - x_titik_A
dy = y_titik_B - y_titik_A
Jarak_A_dan_B = ((dx**2) + (dy**2))**0.5
Titik_tengah = ((x_titik_A + x_titik_B) / 2, (y_titik_A + y_titik_B) / 2)

#tampilkan hasil
print("================================")
print("KALKULATOR KOORDINAT DUA TITIK")
print(f"x titik A: {x_titik_A}")
print(f"y titik A: {y_titik_A}")
print(f"x titik B: {x_titik_B}")
print(f"y titik B: {y_titik_B}")
print()
print(f"Titik A= ({x_titik_A}, {y_titik_A})")
print(f"Titik B= ({x_titik_B}, {y_titik_B})")
print(f"Perubahan = dx= {dx}, dy= {dy}")
print(f"Jarak A ke B = {Jarak_A_dan_B:.2f}")
print(f"Titik tengah= {Titik_tengah}")
print("================================")


