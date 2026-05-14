#method tambah mahasiswa
#lihat_mahasiswa
#hapus mahasiswa

class MahasiswaManager:
    def __init__(self):
        self.list_mahasiswa = []
        
    def tambah_mahasiswa(self):
        nama = input("Masukkan nama mahasiswa : ")
        umur = int(input("Masukkan umur anda : "))
        jurusan = input("Masukkan jurusan anda : ")
        
        mahasiswa_baru = Mahasiswa(nama, umur, jurusan)
        self.list_mahasiswa.append(mahasiswa_baru)
        print("Data mahasiswa berhasil ditambahkan")
        
    def lihat_mahasiswa(self):
        if self.list_mahasiswa == []:
            print("Data Mahasiswa masih kosong")
        
        for mahasiswa in self.list_mahasiswa:
            print(mahasiswa.nama)
            print(mahasiswa.umur)
            print(mahasiswa.jurusan)
            
    def update_mahasiswa(self):
        nama_mahasiswa = input("Masukkan nama mahasiswa yang ingin diupdate : ")
        
        ditemukan = False
        
        for mahasiswa in self.list_mahasiswa:
            if nama_mahasiswa == mahasiswa.nama:
                ditemukan = True
                print("\n === Pilih Perubahan === ")
                print("1. Rubah Nama ")
                print("2. Rubah Umur ")
                print("3. Rubah Jurusan ")
                print("4. Exit ")
                
                pilihan = int(input("Masukkan pilihan : "))
                
                if pilihan == 1:
                    nama_baru = input("Masukkan nama mahasiswa yang baru : ")
                    mahasiswa.nama = nama_baru
                    print("Data berhasil dirubah")
                elif pilihan == 2:
                    umur_baru = int(input("Masukkan umur yang baru : "))
                    mahasiswa.umur = umur_baru
                    print("Data berhasil dirubah")
                elif pilihan == 3:
                    jurusan_baru = input("Masukkan jurusan baru : ")
                    mahasiswa.jurusan = jurusan_baru
                    print("Data berhasil dirubah")
                elif pilihan == 4:
                    break
            
        if ditemukan == False:
            print("Nama mahasiswa tidak ditemukan")
        
    def hapus_mahasiswa(self):
        hapus_mahasiswa = input("Masukkan nama mahasiswa yang ingin dihapus : ")
        
        ditemukan = False
        
        for mahasiswa in self.list_mahasiswa:
            if hapus_mahasiswa == mahasiswa.nama:
                self.list_mahasiswa.remove(mahasiswa)
                ditemukan = True
                print("Data mahasiswa berhasil dihapus")
            
        if ditemukan == False:
            print("Data Mahasiswa tidak ditemukan")
            

class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan


manager = MahasiswaManager()

while True :
    print("\n === Menu Mahasiswa ===")
    print(" 1. Tambah Mahasiswa ")
    print(" 2. Lihat Mahasiswa ")
    print(" 3. Update Mahasiswa ")
    print(" 4. Hapus Mahasiswa ")
    print(" 5. Exit ")
    
    pilihan = int(input("Masukkan pilihan anda : "))
    
    if pilihan == 1:
        manager.tambah_mahasiswa()
    elif pilihan == 2:
        manager.lihat_mahasiswa()
    elif pilihan == 3:
        manager.update_mahasiswa()
    elif pilihan == 4:
        manager.hapus_mahasiswa()
    elif pilihan == 5:
        break