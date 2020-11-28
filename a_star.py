import pprint
from sekiller import manhattan_mesafesi, hareket


pp = pprint.PrettyPrinter(indent=4)


def a_star(basla, bitis):

    # Manhattan Mesafesini kullanan A - yıldız Algoritması

    basla = str(basla)
    liste_mesafe = [[manhattan_mesafesi(basla, bitis), basla]]#mesafe hesabının liste ile tutulması
    genisletilmis_dugum_listesi = []
    genisletilmis_dugum = 0
    # Yanlış yerleştirilmiş karelarin tüm kombinasyonları için işlemi tekrarlanması
    while liste_mesafe:
        i = 0
        for j in range(1, len(liste_mesafe)):
            if liste_mesafe[i][0] > liste_mesafe[j][0]:
                i = j
            # Yanlış yerleştirilmiş karolar için daha düşük Manhattan mesafesi değerleri (ideal hareketler)
        sekil_izlemi = liste_mesafe[i]
        liste_mesafe = liste_mesafe[:i] + liste_mesafe[i + 1:]
        bitis_dugum = sekil_izlemi[-1]
        if bitis_dugum == bitis:
            break
        if bitis_dugum not in genisletilmis_dugum_listesi:
            for izlence in hareket(bitis_dugum):
                if izlence not in genisletilmis_dugum_listesi:
                    # Matrisin tüm makul geçişlerini elde etmek
                    yeni_yol = [sekil_izlemi[0] + manhattan_mesafesi(izlence, bitis) - manhattan_mesafesi(bitis_dugum, bitis)]\
                        + sekil_izlemi[1:] + [izlence]
                    liste_mesafe.append(yeni_yol)
                    genisletilmis_dugum_listesi.append(bitis_dugum)
                genisletilmis_dugum = genisletilmis_dugum + 1

    sekil_izlemi_boyutu = len(sekil_izlemi)

    print("Matrisin Düzenlenmesi İçin Gerekli Adım Sayısı : ", sekil_izlemi_boyutu//4, 'adım.')
    pp.pprint(sekil_izlemi)