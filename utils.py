# =========================
# utils.py
# Modul Konversi Suhu
# =========================

def cf(c):
    """Celsius ke Fahrenheit"""
    return (c * 9/5) + 32

def ck(c):
    """Celsius ke Kelvin"""
    return c + 273.15

def fc(f):
    """Fahrenheit ke Celsius"""
    return (f - 32) * 5/9

def fk(f):
    """Fahrenheit ke Kelvin"""
    return (f - 32) * 5/9 + 273.15

def kc(k):
    """Kelvin ke Celsius"""
    return k - 273.15

def kf(k):
    """Kelvin ke Fahrenheit"""
    return (k - 273.15) * 9/5 + 32

def konversi_suhu(nilai, dari, ke):
    """
    Fungsi utama untuk konversi suhu.
    nilai: angka suhu
    dari : satuan asal ('c', 'f', 'k')
    ke   : satuan tujuan ('c', 'f', 'k')
    """
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan input
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid! Gunakan 'C', 'F', atau 'K'."

    # Validasi nilai suhu (Kelvin tidak boleh negatif)
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif!"

    # Jika sama, langsung kembalikan
    if dari == ke:
        return nilai

    # fungsi konversi
    konversi = {
        ("c", "f"): cf,
        ("c", "k"): ck,
        ("f", "c"): fc,
        ("f", "k"): fk,
        ("k", "c"): kc,
        ("k", "f"): kf,
    }

    fungsi = konversi.get((dari, ke))
    if fungsi:
        return fungsi(nilai)
    else:
        return "Error: Konversi tidak tersedia."
