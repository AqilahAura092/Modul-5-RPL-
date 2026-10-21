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

    def create_buku(self, judul, penulis, tahun_terbit):
        cursor = self.db.cursor()
        query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
        cursor.execute(query, (judul, penulis, tahun_terbit))
        self.db.commit()
        cursor.close()
        return True

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        cursor = self.db.cursor()
        sql = "UPDATE buku SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
        val = (judul, penulis, tahun_terbit, id_buku)
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