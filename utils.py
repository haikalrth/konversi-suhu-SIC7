# utils.py
def konversi_suhu(nilai, dari, ke):
    """Mengembalikan HASIL sebagai float (bukan string)."""
    dari = dari.lower()
    ke = ke.lower()

    # Validasi satuan
    units = {"c", "f", "k"}
    if dari not in units or ke not in units:
        raise ValueError("Satuan tidak valid. Gunakan C, F, atau K.")

    # Validasi nilai (Kelvin tidak boleh negatif)
    if dari == "k" and nilai < 0:
        raise ValueError("Nilai Kelvin tidak boleh negatif.")

    # Jika satuan sama, kembalikan nilai apa adanya (float)
    if dari == ke:
        return float(nilai)

    # Konversi ke Celsius sebagai jembatan
    if dari == "c":
        c = float(nilai)
    elif dari == "f":
        c = (float(nilai) - 32.0) * 5.0 / 9.0
    else:  # dari == "k"
        c = float(nilai) - 273.15

    # Dari Celsius ke target
    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9.0 / 5.0) + 32.0
    else:  # ke == "k"
        return c + 273.15
