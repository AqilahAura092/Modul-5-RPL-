import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()
    
    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.db = MagicMock()
    mock_cursor = MagicMock()
    model.db.cursor.return_value = mock_cursor
    
    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)
    
    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.db.commit.assert_called_once()

def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()
    
    # Memanipulasi (Mock) koneksi database
    model.db = MagicMock()
    mock_cursor = MagicMock()
    model.db.cursor.return_value = mock_cursor
    
    # Menyiapkan data dummy tiruan untuk fetchall
    mock_cursor.fetchall.return_value = [(1, "Buku Testing", "Penulis QA", 2026)]
    
    # Melakukan eksekusi fungsi
    hasil = model.get_all_buku()
    
    # Memverifikasi hasil
    assert len(hasil) > 0
    mock_cursor.execute.assert_called_once()