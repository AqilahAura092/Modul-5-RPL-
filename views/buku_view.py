import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("880x480")

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORMULIR INPUT BUKU
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Komponen Input
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Judul Buku"
        )
        self.entry_judul.pack(pady=8, padx=15, fill="x")

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Nama Penulis"
        )
        self.entry_penulis.pack(pady=8, padx=15, fill="x")

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Tahun Terbit (Misal: 2024)"
        )
        self.entry_tahun.pack(pady=8, padx=15, fill="x")

        # Tombol Aksi (Simpan, Update, Delete)
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri, text="Simpan Data", fg_color="green"
        )
        self.btn_simpan.pack(pady=18, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(
            self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue"
        )
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(
            self.frame_kiri, text="Hapus Data (Delete)", fg_color="red"
        )
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # FRAME KANAN: TABEL DAFTAR BUKU
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Koleksi Buku - Aqilah Aura A_092",
            font=("Arial", 16, "bold"),
        ).pack(pady=15)

        # Komponen Tabel (Menyesuaikan dengan Model: id_buku, judul, penulis, tahun_terbit)
        kolom = ("id_buku", "judul", "penulis", "tahun_terbit")
        self.tabel = ttk.Treeview(
            self.frame_kanan, columns=kolom, show="headings", height=15
        )

        self.tabel.heading("id_buku", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun_terbit", text="Tahun")

        self.tabel.column("id_buku", width=40, anchor="center")
        self.tabel.column("judul", width=200, anchor="w")
        self.tabel.column("penulis", width=150, anchor="w")
        self.tabel.column("tahun_terbit", width=60, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()