from config.database import Database

class BukuModel:
    def __init__(self):
        db_instance = Database()
        self.db = db_instance.get_connection()

    def get_all_buku(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM buku ORDER BY id_buku ASC")
        result = cursor.fetchall()
        cursor.close()
        return result

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        cursor = self.db.cursor()
        # Mengubah data ID 4 (atau data yang ingin di-update) menjadi ID 10
        sql = "UPDATE buku SET id_buku = %s, judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = 4"
        val = (id_buku, judul, penulis, tahun_terbit)
        cursor.execute(sql, val)
        self.db.commit()
        cursor.close()

    def delete_buku(self, id_buku):
        cursor = self.db.cursor()
        sql = "DELETE FROM buku WHERE id_buku = %s"
        val = (id_buku,)
        cursor.execute(sql, val)
        self.db.commit()
        cursor.close()