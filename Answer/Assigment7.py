#No 1
# angka_input = input().strip()
# daftar_angka = [int(angka) for angka in angka_input.split(',')]
# daftar_urut = sorted(daftar_angka)
# target = int(input())
# print(daftar_urut.index(target))


# No 2
# T = int(input("Masukkan berapa percobaan yang dilakukan: "))

# for case in range(1, T+1):
#     M = int(input("Masukkan jumlah katak pria: "))
#     F = int(input("Masukkan jumlah katak wanita: "))
#     total = M * F
#     if total % 2 == 0:
#         print(f"Case {case}: Frog Comeback Party!")
#     else:
#         print(f"Case {case}: Still needed more frogs…")
        
        
akun = {}
with open("/Users/huanxin/Pemograman Binus/Answer/account.txt") as file:
    for baris in file:
        baris = baris.strip() 
        if baris:  
            if '-' in baris:
                username, password = baris.split('-', 1)
                akun[username] = password

input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username in akun and akun[input_username] == input_password:
    print(f"Welcome {input_username}!")
else:
    print("Access denied!")