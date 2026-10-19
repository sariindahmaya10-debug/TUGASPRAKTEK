tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
kehadiran = float(input("Kehadiran (%): "))

nilai_akhir = (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)

if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

print("Nilai Akhir:", nilai_akhir)
print("Status:", status)