import time
from a_star import a_star
from cozumkontrol import cozum_varmi, y_hucre_sayisi
import psutil
import os

#kullanılan bellek miktarının belirlenmesi
islem = psutil.Process(os.getpid())
bellek = islem.memory_info().rss
ana_bellek = bellek /2.**30 #yaklaşık 1.000.000.000
n=0
#İlk olarak yaptığım for döngülü işlemi tek satıra indirerek zamandan tasarruf ettim.
n=input("4x4 lük matrisi için satır sayınızı 4 olarak giriniz:")
kontrol=int(n)
#n=int(input("4x4 lük matrisi için satır sayınızı 4 olarak giriniz:"))
print("********--------*********---------*********--------*********")
print("Örnek Satır Girdi Şekli : 1 2 3 4")
print("********--------*********---------*********--------*********")
print("Kullanabileceğiniz Bir Örnek Matris:[[0 12 9 13], [15 11 10 14], [3 7 2 5], [4 8 6 1]]")
print("Kullanabileceğiniz Bir Örnek Matris:[[12 1 10 2], [7 11 4 14], [5 0 9 15], [8 13 6 3]]")
print("Kullanabileceğiniz Bir Örnek Matris:[[5 11 3 8], [13 2 6 7], [14 12 9 4], [10 1 0 15]]")
print("Kullanabileceğiniz Bir Örnek Matris:[[12 15 6 10], [4 9 5 8], [14 13 0 2], [1 7 11 3]]")
print("Kullanabileceğiniz Bir Örnek Matris:[[12 15 6 10], [4 9 5 8], [14 13 0 2], [1 7 11 3]]")
print("Kullanabileceğiniz Bir Örnek Matris:[[5 10 14 7], [8 3 6 1], [15 0 12 9], [2 11 4 13]]")
print("********--------*********---------*********--------*********")
#kullanıcıdan satırların alınması ve 4 değeri için kontrol sağlanması
if(kontrol==4):   
    satir1=[int(x) for x in input("1.satır için 4 değer giriniz: ").split()]
    satir2=[int(x) for x in input("2.satır için 4 değer giriniz: ").split()]
    satir3=[int(x) for x in input("3.satır için 4 değer giriniz: ").split()]
    satir4=[int(x) for x in input("4.satır için 4 değer giriniz: ").split()]
else:
    print("n sayısını 4 den fazla ya da az girmeyin.")

 

if __name__ == '__main__':
    baslangic_zaman = time.time()#baslangiç zamanı
    baslangic_durumu = [satir1, satir2, satir3, satir4]
    #son durumun bu olması gerekliliği
    son_durum = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    if cozum_varmi(str(baslangic_durumu)):
        print("********--------*********---------*********--------*********")
        print("Bu Matris Çözülebilir Ve Çözüm Aşağıda Verilmiştir.!")
        print("********--------*********---------*********--------*********")
        print("Hatalı Yerleştirilmiş Hücre Sayısı : ", y_hucre_sayisi(str(baslangic_durumu), son_durum))
        print("********--------*********---------*********--------*********")
        a_star(str(baslangic_durumu), son_durum)
        print("")
        print("İşlem İçin Toplam Harcanan Zaman :{:.2f} saniye".format(time.time() - baslangic_zaman))#son zamandan başlangıç zamanının çıkarımı
        print('Kullanılan Bellek:{:.2f}'.format(ana_bellek), ' MB')#islem süresince kullanılan bellek mb cinsinden
    else:
        print("Verilen Matris A* İle Çözülemez . Başka Bir Başlangıç Matrisi Tanımlayınız. !!!")
