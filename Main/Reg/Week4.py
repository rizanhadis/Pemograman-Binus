# #Selection

# AdaApatuh = False
# AdaWitan = True
# AdaAja = True

# if AdaApatuh :
#     print("Pesen Kopikap satu")
# elif AdaWitan:
#     print("Bebas pilih") 
# elif AdaApatuh and AdaWitan:
#     print("Yang ada aja deh")
# else: 
#     print("Marimas aja")
    
    
# nested if

# x = int(input("masukan x: "))

# if x <= 95:
#     if x >= 95:
#         print("A+")
#     else:
#         print("A-")

# elif x >= 80:
#     print("B")
# elif x >= 70:
#     print("C")
# else:
#     print("D")

# Match

# match x:
#     case 1:
#         print("Ini nyatu")
#     case 2:
#         print("this is dua")
#     case 3:
#         print("ini tiga")
#     case _:
#         print("tidak ada")


x = int(input("Nilai X: ")) 
y = int(input("Nilai Y: "))

print("(",x,",",y,")",end="")
if(x>0 and y<0):
    print("Kuadran ke empat")
elif(x<0 and y>0):
    print("Kuadran ke dua")
elif(x>0 and y>0):
    print("Kuadran ke satu")
else:
    print("Kuadran ke tiga")