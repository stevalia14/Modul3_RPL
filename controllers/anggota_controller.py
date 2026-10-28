import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for a in data_anggota:
            self.view.tabel.insert("", "end", values=(a['id_anggota'], a['nama'], a['alamat']))

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def pilih_data(self, event):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return
        nilai = self.view.tabel.item(terpilih[0])['values']

        self.bersihkan_form()
        self.view.entry_nama.insert(0, nilai[1])
        self.view.entry_alamat.insert(0, nilai[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_data(self):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return

        id_anggota = self.view.tabel.item(terpilih[0])['values'][0]

        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            berhasil = self.model.hapus_anggota(id_anggota)
            if berhasil:
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def perbarui_data(self):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin diperbarui!")
            return

        id_anggota = self.view.tabel.item(terpilih[0])['values'][0]
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_anggota(id_anggota, nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def run(self):
        self.view.mainloop()