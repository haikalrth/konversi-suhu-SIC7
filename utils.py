# utils.py
# Modul Konversi Suhu

def cf(c):
    """Celsius ke Fahrenheit"""
    return (c * 9.0/5.0) + 32.0

def ck(c):
    """Celsius ke Kelvin"""
    return c + 273.15

def fc(f):
    """Fahrenheit ke Celsius"""
    return (f - 32.0) * 5.0/9.0

def fk(f):
    """Fahrenheit ke Kelvin"""
    return (f - 32.0) * 5.0/9.0 + 273.15

def kc(k):
    """Kelvin ke Celsius"""
    return k - 273.15

def kf(k):
    """Kelvin ke Fahrenheit"""
    return (k - 273.15) * 9.0/5.0 + 32.0

def konversi_suhu(nilai, dari, ke):
    """
    Fungsi utama untuk konversi suhu.
    nilai: angka suhu (int/float)
    dari : satuan asal ('c', 'f', 'k')
    ke   : satuan tujuan ('c', 'f', 'k')

    Mengembalikan:
      - float : hasil konversi (apabila sukses)
      - str   : pesan error (apabila invalid)
    """
    # normalisasi
    if not isinstance(dari, str) or not isinstance(ke, str):
        return "Error: Satuan harus berupa string 'C', 'F', atau 'K'."

    dari = dari.lower().strip()
    ke = ke.lower().strip()

    # validasi satuan
    if dari not in {"c", "f", "k"} or ke not in {"c", "f", "k"}:
        return "Error: Satuan tidak valid! Gunakan 'C', 'F', atau 'K'."

    # validasi nilai (Kelvin tidak boleh negatif jika inputnya Kelvin)
    try:
        nilai_f = float(nilai)
    except (ValueError, TypeError):
        return "Error: Nilai suhu harus berupa angka."

    if dari == "k" and nilai_f < 0.0:
        return "Error: Suhu Kelvin tidak boleh negatif!"

    # jika sama, kembalikan nilai sebagai float
    if dari == ke:
        return float(nilai_f)

    # mapping konversi
    konversi = {
        ("c", "f"): cf,
        ("c", "k"): ck,
        ("f", "c"): fc,
        ("f", "k"): fk,
        ("k", "c"): kc,
        ("k", "f"): kf,
    }

    fungsi = konversi.get((dari, ke))
    if fungsi is None:
        return "Error: Konversi tidak tersedia."
    else:
        # jalankan fungsi konversi dan kembalikan float
        return float(fungsi(nilai_f))
