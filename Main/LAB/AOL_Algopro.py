import math 
import uuid 

def generate_short_uuid(length=6):
    return str(uuid.uuid4()).replace('-', '')[:length]

paket_vip = {
    1: 6000,
    2: 11000,
    4: 22000,
    8: 40000,
}
paket_regular = {
    1: 4000,
    2: 8000,
    4: 15000,
    8: 25000,
}
harga_paket_begadang = 30000

print("\nPilihan Tipe Paket:")
print("1. VIP")
print("2. Regular")
print("3. Paket Begadang")
pilihan_paket_input = input("Pilih Tipe Paket (1/2/3): ")

durasi_jam_dihitung = 0
tipe_paket_str = ""
user_id = "" 
user_password = "" 

if pilihan_paket_input == '1':
    tipe_paket_str = "VIP"
    print("\nDaftar Harga Paket VIP:")
    for jam, harga in paket_vip.items():
        print(f"- {jam} jam: Rp{harga:,}")
    try:
        durasi_input_str = input("Durasi Pemakaian ")
        durasi_float = float(durasi_input_str)
        if durasi_float < 0:
            print("Durasi tidak boleh negatif.") 
            exit()
        durasi_jam_dihitung = math.ceil(durasi_float) if durasi_float > 0 else 0
    except ValueError:
        print("Input durasi tidak valid. Harap masukkan angka.") 
        exit()
elif pilihan_paket_input == '2':
    tipe_paket_str = "Regular"
    print("\nDaftar Harga Paket Regular:")
    for jam, harga in paket_regular.items():
        print(f"- {jam} jam: Rp{harga:,}")
    try:
        durasi_input_str = input("Durasi Pemakaian : ")
        durasi_float = float(durasi_input_str)
        if durasi_float < 0:
            print()
            exit()
        durasi_jam_dihitung = math.ceil(durasi_float) if durasi_float > 0 else 0
    except ValueError:
        print("Input durasi tidak valid. Harap masukkan angka.")
        exit()
elif pilihan_paket_input == '3':
    tipe_paket_str = "Begadang"
    print(f"\nInfo Paket Begadang Rp{harga_paket_begadang:,}")
else:
    print("Pilihan paket tidak valid.")
    exit()

if tipe_paket_str: 
    user_id = generate_short_uuid()
    user_password = generate_short_uuid()

total_biaya = 0
keterangan_rincian_biaya = []

if tipe_paket_str == "Begadang":
    total_biaya = harga_paket_begadang
    keterangan_rincian_biaya.append(f"Paket Begadang (Fixed) - Rp{harga_paket_begadang:,}")
else:  
    paket_harga_terpilih = {}
    if tipe_paket_str == "VIP":
        paket_harga_terpilih = paket_vip
    else:  
        paket_harga_terpilih = paket_regular

    if durasi_jam_dihitung == 0:
        total_biaya = 0
        if tipe_paket_str: 
             keterangan_rincian_biaya.append("Tidak ada durasi pemakaian atau durasi 0 jam.")
    else:
        sisa_durasi_jam = int(durasi_jam_dihitung) 
        
        paket_tersortir = sorted(paket_harga_terpilih.items(), key=lambda item: item[0], reverse=True)
        
        if keterangan_rincian_biaya and keterangan_rincian_biaya[0] == "Tidak ada durasi pemakaian atau durasi 0 jam.":
             keterangan_rincian_biaya.clear()

        for jam_paket, harga_paket in paket_tersortir:
            while sisa_durasi_jam >= jam_paket:
                total_biaya += harga_paket
                sisa_durasi_jam -= jam_paket
                keterangan_rincian_biaya.append(f"1x Paket {jam_paket} jam - Rp{harga_paket:,}")
        
        if durasi_jam_dihitung > 0 and total_biaya == 0 and paket_harga_terpilih:
            jam_paket_terkecil = min(paket_harga_terpilih.keys())
            harga_paket_terkecil = paket_harga_terpilih[jam_paket_terkecil]
            total_biaya = harga_paket_terkecil
            if keterangan_rincian_biaya and keterangan_rincian_biaya[0] == "Tidak ada durasi pemakaian atau durasi 0 jam.":
                keterangan_rincian_biaya.pop(0)

            keterangan_rincian_biaya.append(
                f"Durasi {durasi_jam_dihitung} jam. Paket minimum {jam_paket_terkecil} jam diterapkan - Rp{harga_paket_terkecil:,}"
            )
        
        elif sisa_durasi_jam > 0 and paket_harga_terpilih:
            jam_paket_terkecil_untuk_sisa = min(paket_harga_terpilih.keys())
            harga_paket_terkecil_untuk_sisa = paket_harga_terpilih[jam_paket_terkecil_untuk_sisa]
            total_biaya += harga_paket_terkecil_untuk_sisa
            keterangan_rincian_biaya.append(
                f"Sisa durasi {sisa_durasi_jam} jam ({jam_paket_terkecil_untuk_sisa} jam) - Rp{harga_paket_terkecil_untuk_sisa:,}"
            )

print("\n=== Struk Billing Warnet Kaliki ===")

if user_id and user_password:
    print(f"ID Pengguna: {user_id}")
    print(f"Password: {user_password}")

print(f"Tipe Paket: {tipe_paket_str}")

if tipe_paket_str == "Begadang":
    print("Durasi: Paket Begadang (21:00 - 04:00)")
elif durasi_jam_dihitung > 0 :
    print(f"Durasi pemakaian: {int(durasi_jam_dihitung)} jam")
else: 
    if tipe_paket_str: 
        print("Durasi : 0 jam")

print("\nRincian Biaya:")
if keterangan_rincian_biaya:
    final_rincian = [item for item in keterangan_rincian_biaya if item != "Tidak ada durasi pemakaian atau durasi 0 jam." or len(keterangan_rincian_biaya) == 1]
    if not final_rincian and durasi_jam_dihitung == 0 and tipe_paket_str != "Begadang" and tipe_paket_str:
        print("- Tidak ada durasi pemaikaian atau durasi 0 jam.")
    for item in final_rincian:
        print(f"- {item}")
elif durasi_jam_dihitung == 0 and tipe_paket_str != "Begadang" and tipe_paket_str: 
     print("- Tidak ada durasi pemaikaian atau durasi 0 jam.")
elif not tipe_paket_str: 
    pass 
else:
    print("Silahkan ulangi dari awal")
if tipe_paket_str: 
    print(f"\nTotal Biaya: Rp{total_biaya:,}")