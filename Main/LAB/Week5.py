# List = [1, 2, "hai", True, False, 1.5]
# print(List)

list = [5, 6, 8, 9 ,6, 2]
print(list)
list.append(1)
print(list)

#Nambah data di tengah
list.insert(2, 7)
print(list)

#Untuk ngambil karakter data
print(list[2])

#Untuk ganti data
list[6] = 'hello'
print(list)

#Hapus data
list.remove('hello')
print(list)

del list[2]
print(list)