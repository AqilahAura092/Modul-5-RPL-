# Instalasi library kanren (Jalankan di cell pertama)
#pip install kanren

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

# Skenario C: Inferensi relasi bertingkat (Mencari Kakek)
# Logika: x adalah kakek Andi JIKA x adalah ayah dari y, DAN y adalah ayah dari Andi
kakek_andi = run(0, x, ayah(x, y), ayah(y, "Andi"))
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

print("Aturan diagnosis sistem pakar berhasil dimuat.")

# Eksekusi Rule 1: Pencarian pasien terdiagnosis Flu
pasien_flu = run(0, x, diagnosis_flu(x))
print("Daftar pasien terdiagnosis Flu:", pasien_flu)

# Eksekusi Rule 2: Pencarian pasien terdiagnosis Pilek
pasien_pilek = run(0, x, diagnosis_pilek(x))
print("Daftar pasien terdiagnosis Pilek:", pasien_pilek)

# =========================================================
# 1. FUNGSI KEANGGOTAAN (MEMBERSHIP FUNCTION)
# =========================================================

def segitiga(x, a, b, c):
    if x <= a or x >= c: return 0
    elif a < x <= b: return (x - a) / (b - a)
    elif b < x < c: return (c - x) / (c - b)

def bahu_kiri(x, a, b):
    if x <= a: return 1
    elif a < x < b: return (b - x) / (b - a)
    else: return 0

def bahu_kanan(x, a, b):
    if x >= b: return 1
    elif a < x < b: return (x - a) / (b - a)
    else: return 0

# Fuzzifikasi Banyaknya Pakaian (0 - 100)
def fuzzifikasi_pakaian(x):
    sedikit = bahu_kiri(x, 40, 80)
    banyak = bahu_kanan(x, 40, 80)
    return sedikit, banyak

# Fuzzifikasi Tingkat Kekotoran (0 - 100)
def fuzzifikasi_kekotoran(x):
    rendah = bahu_kiri(x, 40, 50)
    sedang = segitiga(x, 40, 50, 60)
    tinggi = bahu_kanan(x, 50, 60)
    return rendah, sedang, tinggi

# ============================================
# 2. INFERENSI (RULE BASE - SUGENO)
# ============================================

def inferensi_sugeno(pakaian, kekotoran):
    # Dapatkan derajat keanggotaan
    p_sedikit, p_banyak = fuzzifikasi_pakaian(pakaian)
    k_rendah, k_sedang, k_tinggi = fuzzifikasi_kekotoran(kekotoran)

    # Langsung mengembalikan list berisi tuple (alpha, z) beserta keterangan aturannya
    return [
        # [R1] Jika pakaian SEDIKIT dan kekotoran RENDAH, putaran = 500
        (min(p_sedikit, k_rendah), 500),

        # [R2] Jika pakaian SEDIKIT dan kekotoran SEDANG, putaran = 10 * kekotoran + 100
        (min(p_sedikit, k_sedang), (10 * kekotoran) + 100),

        # [R3] Jika pakaian SEDIKIT dan kekotoran TINGGI, putaran = 10 * kekotoran + 200
        (min(p_sedikit, k_tinggi), (10 * kekotoran) + 200),

        # [R4] Jika pakaian BANYAK dan kekotoran RENDAH, putaran = 5 * pakaian + 2 * kekotoran
        (min(p_banyak, k_rendah), (5 * pakaian) + (2 * kekotoran)),

        # [R5] Jika pakaian BANYAK dan kekotoran SEDANG, putaran = 5 * pakaian + 4 * kekotoran + 100
        (min(p_banyak, k_sedang), (5 * pakaian) + (4 * kekotoran) + 100),

        # [R6] Jika pakaian BANYAK dan kekotoran TINGGI, putaran = 5 * pakaian + 5 * kekotoran + 300
        (min(p_banyak, k_tinggi), (5 * pakaian) + (5 * kekotoran) + 300)
    ]

# ============================================
# 3. DEFUZZIFIKASI (WEIGHTED AVERAGE)
# ============================================

def defuzzifikasi_sugeno(aturan):
    pembilang = sum(alpha * z for alpha, z in aturan)
    penyebut = sum(alpha for alpha, z in aturan)

    if penyebut == 0:
        return 0
    return pembilang / penyebut

# ============================================
# 4. PROSES UTAMA (TESTING KASUS)
# ============================================

# Input sesuai dokumen studi kasus
input_pakaian = 50
input_kekotoran = 58

print("=== SISTEM FUZZY MESIN CUCI (SUGENO) ===")
print(f"Banyaknya Pakaian : {input_pakaian}")
print(f"Tingkat Kekotoran : {input_kekotoran}")

# Proses perhitungan
aturan_fuzzy = inferensi_sugeno(input_pakaian, input_kekotoran)
hasil_rpm = defuzzifikasi_sugeno(aturan_fuzzy)

print(f"\nKecepatan Putaran Mesin: {round(hasil_rpm, 2)} rpm")
print(f"DurasiPencucian         : {round(hasil_rpm)} rpm")