def y_hucre_sayisi(baslangic, son):#yanlış yerleştirilen hücre sayısını tespit etmek için gerekli fonksiyon/method
    baslangic = eval(str(baslangic))
    son = eval(son)
    yanlis_yerlestilen_hucre_listesi = []#yanlış yerleştirilen hücreleri tutan liste
    for i in range(len(baslangic)):
        for j in range(len(baslangic)):
            if baslangic[i][j] != son[i][j]:
                yanlis_yerlestilen_hucre_listesi.append(baslangic[i][j])#bu elemanların listeye eklenmesi
    return len(yanlis_yerlestilen_hucre_listesi) - 1  # Boş alan denk geldiğinden itibaren


def cozum_varmi(girilen_matris):
    girilen_matris = eval(girilen_matris)
    deger_sifir = -1
    sayac = 0
    matris_boyutu = len(girilen_matris)
    for m in range(matris_boyutu):
        for n in range(matris_boyutu):
            if girilen_matris[m][n] == 0:
                deger_sifir = m  # değer sıfır olduğundan satırın durumu
    dizi_don = [num for row in girilen_matris for num in row]  # Matrisi listeye dönüştürme işlemi
    # Matrisin çözülmesi için gerekli olan koşullar
    for a in range(len(dizi_don) - 1):
        for b in range(a+1, len(dizi_don)):
            if dizi_don[a] != 0 and dizi_don[b] != 0 and dizi_don[a] > dizi_don[b]:
                sayac += 1
    return (deger_sifir % 2 == 0 and sayac % 2 == 1) or (deger_sifir % 2 == 1 and sayac % 2 == 0)#çözüm kontrolünün sağlanması