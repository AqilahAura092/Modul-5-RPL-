from unittest.mock import MagicMock, patch
from models.buku_model import BukuModel

@patch('models.buku_model.Database')
def test_create_buku_berhasil(mock_database):
    # Mengatur mock koneksi dan cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_database.return_value.get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    model = BukuModel()
    
    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)
    
    # Memverifikasi hasil
    assert hasil is True
    mock_cursor.execute.assert_called_once()

@patch('models.buku_model.Database')
def test_get_all_buku_berhasil(mock_database):
    # Mengatur mock koneksi dan cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_database.return_value.get_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor
    
    # Menyiapkan data dummy tiruan untuk fetchall
    mock_cursor.fetchall.return_value = [(1, "Buku Testing", "Penulis QA", 2026)]
    
    model = BukuModel()
    
    # Melakukan eksekusi fungsi
    hasil = model.get_all_buku()
    
    # Memverifikasi hasil
    assert len(hasil) > 0
    mock_cursor.execute.assert_called_once()