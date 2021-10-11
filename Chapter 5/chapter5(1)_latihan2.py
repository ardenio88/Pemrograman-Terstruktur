Nilaibhsindo = input("Nilai Bahasa Indonesia:")
Nilaiipa = input("Nilai IPA:")
Nilaimat = input("Nilai Matematika:")
if (int(Nilaibhsindo) >= 0) and (int(Nilaiipa) >= 0) and (int(Nilaimat) >= 0):
    if (int(Nilaibhsindo) < 60) or (int(Nilaiipa) < 60) or (int(Nilaimat) < 70):
        print("Status Kelulusan: TIDAK LULUS")
    else:
        print("Status Kelulusan: LULUS")
else:
    print("Maaf input ada yang tidak valid")