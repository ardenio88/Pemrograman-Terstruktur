Nilaibhsindo = input("Nilai Bahasa Indonesia:")
Nilaiipa = input("Nilai IPA:")
Nilaimat = input("Nilai Matematika:")
StatusKelulusan = "n"
if (int(Nilaibhsindo) >= 0) and (int(Nilaiipa) >= 0) and (int(Nilaimat) >= 0):
    if (int(Nilaibhsindo) < 60) or (int(Nilaiipa) < 60) or (int(Nilaimat) < 70):
        StatusKelulusan = "x"
    else:
        StatusKelulusan = "y"
if StatusKelulusan == "x":
    print("Status Kelulusan = TIDAK LULUS")
    print("Sebab:")
    if (int(Nilaibhsindo) < 60):
        print("Nilai Bahasa Indonesia kurang dari 60")
    if (int(Nilaiipa) < 60):
        print("Nilai IPA kurang dari 60")
    if (int(Nilaimat) < 70):
        print("Nilai Matematika kurang dari 70")
elif StatusKelulusan == "y":
    print("Status Kelulusan = LULUS")
elif StatusKelulusan == "n":
    print("Maaf input ada yang tidak valid")
    