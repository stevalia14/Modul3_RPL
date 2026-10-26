import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Binding tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)

        # Saat baris tabel diklik, isi form dengan data baris tersebut
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def pilih_data(self, event):
        # Mengambil baris yang diklik, lalu menampilkannya di form
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return
        nilai = self.view.tabel.item(terpilih[0])['values']

        self.bersihkan_form()
        self.view.entry_judul.insert(0, nilai[1])
        self.view.entry_penulis.insert(0, nilai[2])
        self.view.entry_tahun.insert(0, nilai[3])

    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_data(self):
        # Ambil id_buku dari baris tabel yang dipilih
        terpilih = self.view.tabel.selection()
        if not terpilih:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return

        id_buku = self.view.tabel.item(terpilih[0])['values'][0]

        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            berhasil = self.model.hapus_buku(id_buku)
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def perbarui_data(self):
        # Ambil id_buku dari baris tabel yang dipilih
        terpilih = self.view.tabel.selection()
        if not terpilih:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin diperbarui!")
            return

        id_buku = self.view.tabel.item(terpilih[0])['values'][0]
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_buku(id_buku, judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def run(self):
        self.view.mainloop()