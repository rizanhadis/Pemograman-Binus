class Mahasiswa :
    def _init_(self,a,nim,kelas):
        self.nama = a # public
        self.__nim = nim # private
        self.__kelas = kelas # private
    # gather dan pake role
    def get_nim(self,role): # harus diikuti dengan return
        if role == "admin": 
            return self.__nim
        else:
            return "None"
    # setter
    def set_nim(self, nim):
        self.__nim = nim
    
    def makan(self,nama_makanan):
        print(f"{self.nama} sedang makan {nama_makanan}")

    def showinfo(self):
        print(f"nama: {self.nama}")
        print(f"nim: {self.nim}")
        print(f"kelas: {self.kelas}")
from exercise import Mahasiswa

mahasiswa_1 = Mahasiswa("Frans",123,4.0)
# mahasiswa_1.showinfo()
# print(mahasiswa_1.nama)
# print(mahasiswa_1.nim)
# print(mahasiswa_1.gpa)

# mahasiswa_1.gpa = 5.0 
# print(mahasiswa_1.gpa)
# mahasiswa_1.makan("ayam geprek")
# mahasiswa_2 = Mahasiswa("hadis", 2453, 4.5)
# mahasiswa_2.showinfo()
mahasiswa_1.set_nim(456)
print(mahasiswa_1.get_nim("users")) # bukan admin

print(mahasiswa_1.get_nim("admin")) # ini admin