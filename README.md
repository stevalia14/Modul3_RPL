# Sistem Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Perpustakaan adalah aplikasi desktop berbasis Python yang dibangun dengan pola arsitektur **MVC (Model-View-Controller)**. Aplikasi ini digunakan petugas perpustakaan untuk login ke sistem dan mengelola data perpustakaan seperti data buku dan anggota.

Teknologi yang digunakan:

- Python sebagai bahasa pemrograman
- CustomTkinter untuk antarmuka (GUI)
- MySQL (melalui Laragon) sebagai basis data
- mysql-connector-python untuk koneksi ke database
- pytest untuk pengujian unit
- GitHub Actions untuk CI otomatis
- PyInstaller untuk pengemasan menjadi berkas .exe

Keamanan: password pengguna disimpan dalam bentuk hash SHA-256.

## 2. Struktur Direktori MVC

```
Modul3_RPL/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml     # Konfigurasi CI GitHub Actions
├── config/                     # Konfigurasi koneksi database
├── models/                     # MODEL: logika data dan akses database
├── views/                      # VIEW: tampilan antarmuka (CustomTkinter)
├── controllers/                # CONTROLLER: penghubung model dan view
├── tests/
│   ├── test_auth.py            # Pengujian hashing dan autentikasi
│   └── test_buku.py            # Pengujian fitur buku
├── main.py                     # Titik masuk aplikasi
├── requirements.txt            # Daftar dependensi
└── .gitignore
```

| Komponen | Folder | Peran |
|---|---|---|
| Model | models/ | Mengelola data dan berkomunikasi dengan database MySQL |
| View | views/ | Menampilkan antarmuka dan menerima input pengguna |
| Controller | controllers/ | Memproses input dari View, memanggil Model, lalu memperbarui View |

## 3. Panduan Instalasi dan Konfigurasi Database MySQL

### Prasyarat

- Python 3.11 atau lebih baru
- Git
- Laragon (sudah menyertakan MySQL)

### Instalasi Aplikasi

1. Clone repositori:
   ```bash
   git clone https://github.com/stevalia14/Modul3_RPL.git
   cd Modul3_RPL
   ```
2. Buat dan aktifkan virtual environment:
   ```powershell
   python -m venv env
   ./env/Scripts/activate
   ```
3. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   ```

### Konfigurasi Database MySQL

1. Buka Laragon, lalu klik **Start All** sampai MySQL menyala.
2. Buka terminal Laragon, lalu masuk ke MySQL:
   ```bash
   mysql -u root -p
   ```
3. Buat database bernama `perpustakaan`:
   ```sql
   CREATE DATABASE perpustakaan;
   USE perpustakaan;
   ```
4. Impor berkas .sql milik proyek (jika tersedia) agar tabel dan data awal terbentuk.
5. Pastikan pengaturan koneksi pada folder `config/` sesuai:

| Parameter | Nilai |
|---|---|
| host | localhost |
| user | root |
| password | (kosong, sesuai bawaan Laragon) |
| database | perpustakaan |

## 4. Cara Menjalankan Aplikasi

### Cara 1: Dari Kode Sumber

Pastikan MySQL di Laragon sudah menyala, lalu jalankan:

```bash
python main.py
```

### Cara 2: Dari Berkas .exe

1. Unduh AplikasiPerpustakaan.exe dari halaman Releases repositori ini.
2. Nyalakan MySQL di Laragon (Start All).
3. Klik dua kali AplikasiPerpustakaan.exe, lalu login.

### Menjalankan Pengujian

```bash
pytest -v
```

### Membuat Ulang Berkas .exe

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" main.py
```

Hasilnya ada di folder dist/.