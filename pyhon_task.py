import math

# 1: Kullanıcıdan string al ve karakter sayısını bul
user_input = input("Bir string giriniz: ")
print(f"Girdiğiniz stringin karakter sayısı: {len(user_input)}")

# 2: Vize-final ortalaması hesaplama
def ortalama_hesapla(vize, final):
    return vize * 0.4 + final * 0.6

def ders_gecme_kontrolu():
    ders = input("\nDers adını giriniz: ")
    vize = float(input(f"{ders} dersi için vize notunu giriniz: "))
    final = float(input(f"{ders} dersi için final notunu giriniz: "))
    ort = ortalama_hesapla(vize, final)
    print(f"{ders} ortalamanız: {ort}")
    if ort >= 50:
        print("Dersi geçtiniz.")
    else:
        print("Dersi geçemediniz.")

ders_gecme_kontrolu()

# 3: 0'dan kullanıcı girişine kadar çift sayılar
sayi = int(input("\nBir sayı giriniz: "))
cift_sayilar = [i for i in range(0, sayi + 1) if i % 2 == 0]
print(f"0'dan {sayi}'ye kadar olan çift sayılar: {cift_sayilar}")

# 4: Log(x, y) hesaplama




while True:
    x = float(input("Taban (x): "))
    y = float(input("Sayı (y): "))

    if x > 0 and x != 1 and y > 0:
        sonuc = math.log(y, x)
        print(f"log_{x}({y}) = {sonuc}")
    else:
        print("Geçersiz değerler! (x > 0, x ≠ 1, y > 0)")

    devam = input("Devam edilsin mi? (e/h): ")
    if devam.lower() != 'e':
        break


# 5: Filament hesabı
def filament_hesapla(uzunluk, genislik, yukseklik, doluluk_orani):
    hacim = uzunluk * genislik * yukseklik  # cm^3
    filament = hacim * doluluk_orani * 1.24  # g
    return filament

print("\n3B yazıcı için kutu baskı hesaplama:")
u = float(input("Uzunluğu (cm): "))
g = float(input("Genişliği (cm): "))
y = float(input("Yüksekliği (cm): "))

filament_15 = filament_hesapla(u, g, y, 0.15)
filament_40 = filament_hesapla(u, g, y, 0.40)

print(f"%15 dolulukla gerekli filament: {filament_15:.2f} g")
print(f"%40 dolulukla gerekli filament: {filament_40:.2f} g")

# 6: Drone batarya ile mesafe tahmini
batarya = float(input("\nDrone'un batarya kapasitesi (mAh): "))
tuketim = float(input("1 km başına enerji tüketimi (mAh): "))

mesafe = batarya / tuketim
alt_sinir = mesafe * 0.9
ust_sinir = mesafe * 1.1

print(f"Drone'un tahmini uçuş menzili: {alt_sinir:.2f} km ile {ust_sinir:.2f} km arası")
