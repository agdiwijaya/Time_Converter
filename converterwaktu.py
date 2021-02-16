def timeConverter(seconds):
    try:
        detik = int(seconds)
        if detik > 359999:
            return "Invalid input: angka yang dimasukkan terlalu besar"
        elif detik < 0:
            return "Invalid input: tidak menerima angka negatif"
        else:
            jam, detik =  detik // 3600, detik % 3600
            menit, detik = detik // 60, detik % 60
            return "Konversi : " "%02d" % jam, ":" "%02d" % menit, ":" "%02d" % detik
            
    except: 
        return "Invalid Input: hanya menerima angka"

seconds = input("Masukkan detik: ")
print(timeConverter(seconds))

