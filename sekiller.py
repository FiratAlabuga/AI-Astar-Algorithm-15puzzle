def manhattan_mesafesi(durumilk, durumson):# manhattan mesafesinin hesaplanması
    durumilk = eval(durumilk)#parametre olarak gönderilen durumilk
    durumson = eval(durumson)#parametre olarak gönderilen durumson
    durumson_liste = []
    sonuc = 0

    for i in range(len(durumson)):
        for j in range(len(durumson)):
            if durumson[i][j] != 0:  # Hücre Boş İse Geç
                # Hedef durumu ve tam konumları (satır ve sütun değerleri)
                durumson_liste.append([[i, j], durumson[i][j]])

    for i in range(len(durumilk)):
        for j in range(len(durumilk)):
            if durumilk[i][j] != 0:  # Hücre Boş İse Geç
                for s in durumson_liste:
                    if s[1] == durumilk[i][j]:  # her bir değerin konumunu başlangıç ​​durumundan alın
                        satir = s[0][0]  # Satır değerleri
                        sutun = s[0][1]  # Sütun değerleri
                sonuc += abs(i - satir) + abs(j - sutun)  # Manhatten mesafesinin ayarlanması
    return sonuc


def hareket(matrix):
    secim_listesi = []
    matrix = eval(matrix)
    i = 0
    while 0 not in matrix[i]:
        i += 1
    j = matrix[i].index(0)

    if i > 0:
        # Yukarı hareket 
        # i = i - 1 bu işlemden itibaren yukarı hareket
        matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
        secim_listesi.append(str(matrix))
        matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
    if i < 3:
        # Aşağı hareket
        # i = i + 1 bu işlemden itibaren yukarı hareket
        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
        secim_listesi.append(str(matrix))
        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
    if j > 0:
        # Sola hareket
        # j = j - 1 bu işlemle soldan itibaren aşağıya
        matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
        secim_listesi.append(str(matrix))
        matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
    if j < 3:
        # Sağa hareket
        # j = j + 1 bu işlemden itibaren sağdan yukarıya 
        matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
        secim_listesi.append(str(matrix))
        matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
    return secim_listesi
