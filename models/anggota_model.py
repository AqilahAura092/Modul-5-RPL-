import mysql.connector

class AnggotaModel:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="perpustakaan"
        )

    def create_anggota(self, nama, alamat):
        cursor = self.db.cursor()
        query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
        cursor.execute(query, (nama, alamat))
        self.db.commit()
        cursor.close()

    def get_all_anggota(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM anggota")
        result = cursor.fetchall()
        cursor.close()
        return result