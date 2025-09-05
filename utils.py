def konversi_suhu(nilai, dari, ke):
    # pastikan case insensitive
    dari = dari.lower()
    ke = ke.lower()

    # validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    # validasi nilai suhu (khusus Kelvin tidak boleh negatif)
    if dari == "k" and nilai < 0:
        return "Error: Nilai suhu dalam Kelvin tidak boleh negatif."

    # Jika satuan asal sama dengan tujuan
    if dari == ke:
        return f"{nilai}°{dari.upper()} = {nilai}°{ke.upper()}"

    # Konversi ke Celsius dulu sebagai jembatan
    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        c = nilai - 273.15

    # Dari Celsius ke target
    if ke == "c":
        hasil = c
    elif ke == "f":
        hasil = (c * 9/5) + 32
    elif ke == "k":
        hasil = c + 273.15

    return f"{nilai}°{dari.upper()} = {hasil:.2f}°{ke.upper()}"
