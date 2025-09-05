# =========================
# utils.py
# Modul Konversi Suhu
# =========================

def konversi_suhu(nilai, dari, ke):
    """
    Fungsi konversi suhu
    nilai : angka suhu (float)
    dari  : satuan asal ("C", "F", "K")
    ke    : satuan tujuan ("C", "F", "K")
    return: hasil konversi (float) atau pesan error (str)
    """

    # case insensitive
    dari = dari.lower()
    ke = ke.lower()

    # validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid! Gunakan 'C', 'F', atau 'K'."

    # validasi suhu Kelvin
    if dari == "k" and nilai < 0:
        return "Error: Suhu Kelvin tidak boleh negatif!"

    # jika satuan sama
    if dari == ke:
        return nilai

    # konversi awal → ke Celsius
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        c = nilai - 273.15

    # dari Celsius → target
    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9/5) + 32
    elif ke == "k":
        return c + 273.15
