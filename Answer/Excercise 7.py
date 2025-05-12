# #No 1
# class Student:
#     def __init__(self, nama, kelas, nim):
#         self.nama = nama
#         self.kelas = kelas
#         self.nim = nim

# # Input data
# input1 = ["Mahasiswa1", "LT18", "255870"]
# input2 = ["Quatre", "LB77", "287719"]

# # Membuat objek
# student1 = Student(input1[0], input1[1], input1[2])
# student2 = Student(input2[0], input2[1], input2[2])


# # No 2
# class Staff:
#     def __init__(self, nama, id_staff, divisi):
#         self.nama = nama
#         self.id = id_staff
#         self.divisi = divisi
#     def printData(self):
#         print(f"Nama: {self.nama} ID: {self.id} Divisi: {self.divisi}")

# input1 = "Henry ST001 RnD".split()
# input2 = "Judith ST022 HRD".split()

# staff1 = Staff(input1[0], input1[1], input1[2])
# staff1.printData()

# staff2 = Staff(input2[0], input2[1], input2[2])
# staff2.printData()


#No 3
class Counter:
    def __init__(self, goal):
        self.goal = goal
        self.num = 0
    def count(self):
        if self.num < self.goal:
            self.num += 1
            print(f"Counter is at {self.num}")
        else:
            print("Counter has reached its goal!")

goal = int(input("Masukkan goal: "))
iterations = int(input("Masukkan jumlah iterasi: "))

counter = Counter(goal)
for _ in range(iterations):
    counter.count()