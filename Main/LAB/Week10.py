list1 = [1, 8, 9, 5, 'Hello']
print (list1)


list1.append(1)
print(list1)

#Nambah data di tengah
list1.insert(2, 7)
print(list1)

#Untuk ngambil karakter data
print(list1[2])

#Untuk ganti data
list1[6] = 'hello'
print(list1)

#Hapus data
list1.remove('hello')
print(list1)

list1.pop(0)
print(list1)

del list1[2]
print(list1)

if "Hello world!" not in list1 :
    print('Hello world tidak ada')
else :
    print('Hello world ada')

for i in range(len(list1)):
    if list1[i] == 'hello world':
        print(list1[i])
        
    if str(list1[i]).startswith('h'):
        print(list1[i])
        
        
        
listAngka = [0,9,8,1,2,9,3,4]
target = 9
listIndeks = [ ]

for i in range(len(listAngka)):
    if listAngka[i] == target:
        listIndeks.append(i)
print(listIndeks)





Listnama = [['Abel', 30, 82,], ['Zita', 28,70], ['John', 29, 100]]
nama = sorted (Listnama, key = lambda x : x[0])
print(nama)
angkatan = sorted (Listnama, key = lambda x : x[1])
print(angkatan)
nilai = sorted (Listnama, key = lambda x : x[2])
print(nilai)


