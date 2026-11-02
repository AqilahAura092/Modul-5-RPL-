# Sistem Manajemen Perpustakaan (MVC Python)

## 1. Deskripsi Singkat Aplikasi
Aplikasi desktop manajemen perpustakaan berbasis Python menggunakan arsitektur Model-View-Controller (MVC)[cite: 5], antarmuka CustomTkinter[cite: 6], dan database MySQL[cite: 6].

## 2. Struktur Direktori MVC
- `config/` : Konfigurasi koneksi database
- `controllers/` : Logika pengontrol alur aplikasi
- `models/` : Logika data dan interaksi database
- `views/` : Antarmuka pengguna
- `tests/` : Pengujian otomatis (pytest)

## 3. Panduan Instalasi & Konfigurasi Database MySQL
1. Nyalakan modul MySQL melalui Laragon[cite: 4, 10].
2. Buat database baru sesuai konfigurasi proyek.
3. Buat dan aktifkan *virtual environment*, lalu instal dependensi:
   ```bash
   pip install -r requirements.txt