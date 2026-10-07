# Instalasi library kanren (Jalankan di cell pertama)
# pip install kanren

# Import fungsi-fungsi dasar dari kanren
from kanren import Relation, facts, run, var, lall

# Mendefinisikan relasi bernama 'ayah'
ayah = Relation()

# Menambahkan Fakta (Knowledge Base)
# Format representasi: ("Nama Ayah", "Nama Anak")
facts(ayah, ("Joko", "Budi"),
            ("Joko", "Wawan"),
            ("Budi", "Andi"),
            ("Budi", "Siti"))

print("Fakta silsilah keluarga berhasil diinisialisasi pada sistem.")

# Inisialisasi variabel kosong (x dan y) untuk menampung hasil query
x = var()
y = var()

# Skenario A: Mencari anak dari entitas spesifik
anak_budi = run(0, x, ayah("Budi", x))
print("Anak dari Budi adalah:", anak_budi)

# Skenario B: Mencari ayah dari entitas spesifik
ayah_andi = run(0, x, ayah(x, "Andi"))
print("Ayah dari Andi adalah:", ayah_andi)

# Skenario C: Inferensi relasi bertingkat (Mencari kakek)
# Logika: x adalah kakek Andi JIKA x adalah ayah dari y, DAN y adalah ayah dari Andi
kakek_andi = run(0, x, lall(ayah(x, y), ayah(y, "Andi")))
print("Kakek dari Andi adalah:", kakek_andi)

# Mendefinisikan relasi baru untuk gejala medis
gejala = Relation()

# Memasukkan Fakta: Data observasi gejala pasien
facts(gejala, ("Andi", "demam"),
              ("Andi", "batuk"),
              ("Siti", "pusing"),
              ("Siti", "bersin"),
              ("Wawan", "demam"))

# Membangun Aturan (Rules) Diagnosa Penyakit
def diagnosis_flu(pasien):
    # Rule: JIKA pasien mengalami demam DAN batuk, MAKA diagnosis = Flu
    return lall(gejala(pasien, "demam"), gejala(pasien, "batuk"))

def diagnosis_pilek(pasien):
    # Rule: JIKA pasien mengalami pusing DAN bersin, MAKA diagnosis = Pilek
    return lall(gejala(pasien, "pusing"), gejala(pasien, "bersin"))

print("Aturan diagnosis sistem pakar berhasil dibuat.")

# Eksekusi Rule 1: Pencarian pasien terdiagnosis Flu
pasien_flu = run(0, x, diagnosis_flu(x))
print("Daftar pasien terdiagnosis Flu:", pasien_flu)

# Eksekusi Rule 2: Pencarian pasien terdiagnosis Pilek
pasien_pilek = run(0, x, diagnosis_pilek(x))
print("Daftar pasien terdiagnosis Pilek:", pasien_pilek)