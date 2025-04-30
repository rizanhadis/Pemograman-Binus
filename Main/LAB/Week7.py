import Week7v2 as fg

# print(fg.tambah(1,2))
# print(fg.kurang(1,2)) 
# print(fg.kali(1,2))
# print(fg.bagi(1,2))


# try : 
#     ipt = ipt(input("Masukka angka :"))
#     print(ipt)
# except : 
#     print("Harus angka !!")
    
#     print("Haloo")



try :
    a = [0,1,2,3]
    print(a[5])
    
except IndexError:
    print("Yaudah gitu deh hasilnya")
    
    
    # import fungsi as fg

# print(fg.tambah(1,2))
# print(fg.kurang(1,2)) 

# try : 
#     ipt = int(input("masukkan angka : "))
#     print(ipt)
# except : 
#     print("Harus angka !!!!")

# print("halooo")

# lst = []
# print(lst)
# lst.append(input())
# print(lst)

#  Write
# file = open("hewan.txt", "w")

# file.write("ayam") # hanya 1 data
# file.writelines(["ikan\n", "sapi\n", "kerbau\n"]) # bisa beberapa data

# file.close()

# file = open("hewan.txt", "a")

# file.write("ayam") # hanya 1 data
# file.writelines(["ikan\n", "sapi\n", "kerbau\n"]) # bisa beberapa data

# file.close()

# read
file = open("hewan.txt", "r")
print(file.read())
print(file.readlines())
for line in file:
    print(line)


file.close()