ListSiswa=[]
ListNilai=[]
a=0
while a == 0:
    print("Pilih Menu: ")
    print("1. Input Data Siswa")
    print("2. Input Nilai Siswa")
    print()
    
    pilih = int(input("Tentukan pilihan (1/2): "))
    if pilih ==1:
        s=0
        while s==0:
            nim = input()
            nama = input()
            tahun = input()
            ListSiswa.append([nim, nama, tahun])
            p1 = input("Input Data Siswa Lagi (Y/T): ")
            if p1=="T":
                s=1
    if pilih==2:
        n=0
        while n==0:
            nim = input()
            nilai = input()
            ListSiswa.append([nim, nilai])
            p2 = input("Input Data Siswa Lagi (Y/T): ")
            if p2=="T":
                n=1 
        
    a1 = input("Apakah Anda Selesai? (Y/T): ")
    if a1=="Y":
        a=1  
        
        