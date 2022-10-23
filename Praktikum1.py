"""
[ Praktikum 1 Komputasi Numerik C Kelompok 09 ( Implementasi Metode Bolzano ) ]
Anggota :
- Alfa Fakhrur Rizal Zaini / 5025211214
- Andhika Lingga Mariano / 5025211161
- Kevin Nathanael Halim / 5025211140

Penjelasan Singkat :
Merupakan implementasi kode dari aproksimasi pencarian akar dari suatu persamaan dengan menggunakan metode Bolzano,
dapat menampilkan grafik yang akan menunjukkan proses pengambilan titik hingga mencapai akar yang sesuai.

Cara Penggunaaan :
- Memasukkan nilai Error Toleransi yang diinginkan pada variabel maxError
- Memasukkan persamaan fungsi ke dalam fungsi lambda y
- Melakukan run pada program dan mengisikan Batas Atas serta Batas Bawah awal untuk memulai pencarian
- Tiap iterasi pun akan ditampilkan beserta dengan grafik dan jawaban akhirnya
"""

#Mengimport library yang diperlukan
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#Variabel Awal
print('Silahkan masukkan Batas Bawah awal yang diinginkan : ')
left = int(input())
print('Silahkan masukkan Batas Atas awal yang diinginkan : ')
right = int(input())
print(f"\nBatas Awal :")
print(f"xBawah = {left}, xAtas = {right}\n")

#Variabel Error
maxError = 0.00001

#Variabel Kalkulasi Error
rError = 1

#Variabel Pembantu Iterasi
iter = 1
midPoint = 1
mid = 0

#Persamaan Fungsi ( y = x3 – 3x + 1 )
y = lambda x: pow(x, 3) - (3 * x) + 1

xPoint = np.array([left, right])
yPoint = np.array([])

#Iterasi selama Error Relatif masih di atas Error Toleransi yang dicari
while rError > maxError :
    fLow = y(left)
    mid = (left + right) / 2
    fMid = y(mid)

    if fLow * fMid < 0 :
        # Akar berada di antara left dan mid
        right = mid
    elif fLow * fMid > 0 :
        #Akar berada di antara mid dan right
        left = mid
    else :
        #Akar tepat ditemukan
        xPoint = np.concatenate((xPoint, [mid]))
        aError = abs(midPoint - mid)
        rError = aError / midPoint
        print(f"Iterasi ke-{iter} : xBawah = {left}, xAtas = {right}, f(xBawah) = {fLow:.10f}, f(xAtas) = {fMid:.10f}, Ea = {aError:.10f}, Er = {rError:.1-f}%")
        break

    #Menambahkan titik baru
    xPoint = np.concatenate((xPoint, [mid]))

    #Menghitung Error yang baru
    aError = abs(midPoint - mid)
    rError = aError/midPoint
    midPoint = mid
    if midPoint == 0 :
        #Mengganti nilai midPoint dengan 0.1 agar bisa dilakukan pembagian bila nilainya 0
        midPoint = 0.1

    #Mengeluarkan detail iterasi
    print(f"Iterasi ke-{iter} : xBawah = {left}, xAtas = {right}, f(xBawah) = {fLow:.10f}, f(xAtas) = {fMid:.10f}, Ea = {aError:.10f}, Er = {rError:.10f}%")
    iter += 1

final = y(mid)
if final > maxError :
    #Batas Atas awal terlalu tinggi sehingga tidak tercapai akar yang sesuai
    print("Batas Atas awal terlalu tinggi, silahkan coba diturunkan atau bila sudah terlalu dekat dengan Batas Bawah awal maka bisa diturunkan keduanya..")

elif final < (-1*maxError) :
    #Batas Bawah awal terlalu tinggi sehingga tidak tercapai akar yang sesuai
    print("Batas Bawah awal terlalu rendah, silahkan coba dinaikkan atau bila sudah terlalu dekat dengan Batas Atas awal maka bisa dinaikkan keduanya..")

else :
    #Mengeluarkan akar akhir yang sesuai
    print("\nJawab :")
    print("xFinal = " + str(mid) + f" | f(xFinal) = {final:.10f}")

    #Mencari nilai x dan y terendah untuk membuat range papan grafik
    xPointSorted = np.sort(xPoint)
    minY = 10000000000
    maxY = 0
    for xN in xPointSorted :
        ytemp = y(xN)
        yPoint = np.concatenate((yPoint, [ytemp]))
        if ytemp > maxY :
            maxY = ytemp
        if ytemp < minY :
            minY = ytemp

    #Membuat range limit papan grafik
    fig, ax = plt.subplots()
    ax.set_xlim(xPointSorted[0] - abs(xPointSorted[0]*0.2), xPointSorted[len(xPointSorted) - 1] + (xPointSorted[len(xPointSorted) - 1]*0.1))
    ax.set_ylim(minY - 0.5, maxY + (maxY*0.1))

    #Menjalankan animasi pembuatan grafik Bolzano
    fflag = False
    def animation_fr(i) :
        global fflag
        if fflag :
            plt.plot(mid, final, marker='*', color="yellow")
            return

        if i == len(xPoint) - 1 :
            plt.plot(mid, final, marker='*')
            plt.plot(xPointSorted, yPoint, color="blue")
            fflag = True

        plt.plot(xPoint[int(i)], y(xPoint[int(i)]), marker='o')

    animation = FuncAnimation(fig, func=animation_fr, frames=np.arange(0, len(xPoint), 1), interval=500)
    plt.show()
