#Nama   : Jasmine Sarah Maqnolia
#NIM    : 20051397078
#Kelas  : 2020B
#Prodi  : Manajemen Informatika

def tabung():
    tinggi=int(input("Masukan Tinggi : "))
    jari=int(input("Masukan Jari-jari Lingkaran : "))
    phi=22/7
    volume=int((phi*(jari*jari))*tinggi)
    print("Volume Tabung : ", volume)
    return volume

def balok():
    p = float(input("Panjang="))
    l = float(input("Lebar="))
    t = float(input("Tinggi="))
    volume=p*l*t
    print("Volume Balok : ", volume)
    return volume

def prismasegitiga():
    tinggi_prisma = int(input("Tinggi Prisma : "))
    alas_segitiga = int(input("Alas Segitiga : "))
    tinggi_segitiga = int(input("Tinggi Segitiga : "))
    volume = ( 1/2 * alas_segitiga * tinggi_segitiga ) * tinggi_prisma
    print("Volume Prisma Segitiga : ", volume)
    return volume

while True:
    print("MENGHITUNG VOLUME")
    print("Pilih:")
    print("1. Mencari Volume Tabung")
    print("2. Mencari Volume Balok")
    print("3. Mencari Volume Prisma Segitiga")
    print("4. Tutup")
    option = input("Option 1-4 : ")
    if option == "1":
        print("Anda Pilih Menu 1")
        tabung()
    elif option == "2":
        print("Anda Pilih Menu 2")
        balok()
    elif option == "3":
        print("Anda Pilih Menu 2")
        prismasegitiga()
    elif option == "4":
        break
    else:
        print("Input Anda salah coba ulang lagi!!!")
