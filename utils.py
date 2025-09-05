def konversi_suhu(nilai, dari, ke):
    dari = dari.upper()
    ke = ke.upper()

    # Validasi satuan
    if dari not in ["C", "F", "K"] or ke not in ["C", "F", "K"]:
        raise ValueError("Satuan tidak valid. Gunakan C, F, atau K.")

    # Validasi nilai suhu
    if dari == "K" and nilai < 0:
        raise ValueError("Nilai Kelvin tidak boleh negatif.")

    # Jika satuan asal dan tujuan sama
    if dari == ke:
        return round(nilai, 1)

    # Konversi ke Celsius dulu
    if dari == "C":
        celsius = nilai
    elif dari == "F":
        celsius = (nilai - 32) * 5 / 9
    elif dari == "K":
        celsius = nilai - 273.15

    # Konversi dari Celsius ke satuan tujuan
    if ke == "C":
        return round(celsius, 1)
    elif ke == "F":
        return round((celsius * 9 / 5) + 32, 1)
    elif ke == "K":
        return round(celsius + 273.15, 1)
