import random
import time
import threading

# Karakter sınıfı
class Karakter:
    @staticmethod
    def metaverse_hoşgeldiniz():
        """Metaverse evrenine hoş geldiniz mesajı gösterir."""
        print("Metaverse evrenine hoş geldiniz!")

    def __init__(self):  
        self._guc = 0
        self._aclik = 0
        self._susuzluk = 0
        self._para = 0
        self._kimlik = 0
        self._uyuyor = False

    def karakter_yarat(self):
        """Karakter için rastgele başlangıç değerleri oluşturur."""
        self._guc = random.randint(0, 100)
        self._aclik = random.randint(0, 100)
        self._susuzluk = random.randint(0, 100)
        self._para = random.randint(0, 1000)
        self._kimlik = random.randint(10000, 99999)

    def karakter_goster(self):
        """Karakterin mevcut özelliklerini ekrana yazdırır."""
        print(f"Güç: {self._guc}, Açlık: {self._aclik}, Susuzluk: {self._susuzluk}, Para: {self._para}, Kimlik: {self._kimlik}")

    def karakter_besle(self):
        """Karakterin açlık seviyesini artırır."""
        self._uyuyor = False
        self._aclik = min(self._aclik + 5, 100)  # Maksimum 100 ile sınırlandırıldı
        self.karakter_goster()
        self._uyuyor = True

    def karakter_su_ver(self):
        """Karakterin susuzluk seviyesini artırır."""
        self._uyuyor = False
        self._susuzluk = min(self._susuzluk + 10, 100)  # Maksimum 100 ile sınırlandırıldı
        self.karakter_goster()
        self._uyuyor = True

    def hareket(self, yon):
        """Karakterin yön hareketlerini ekrana yazdırır."""
        hareketler = {
            'w': f"{self._kimlik} karakteri ileri gidiyor",
            's': f"{self._kimlik} karakteri geri gidiyor",
            'a': f"{self._kimlik} karakteri sola gidiyor",
            'd': f"{self._kimlik} karakteri sağa gidiyor",
            'e': f"{self._kimlik} karakteri sağ ileri gidiyor",
            'q': f"{self._kimlik} karakteri sol ileri gidiyor"
        }
        print(hareketler.get(yon, "Geçersiz hareket"))

    def hareketi_aktifleştir(self):
        """Karakterin hareket fonksiyonlarını kullanıcı girişine göre çalıştırır."""
        print("Hareket fonksiyonlarını aktifleştirdiniz...")
        while True:
            print("İleri gitmek için 'w', geri gitmek için 's', sağa gitmek için 'd', sola gitmek için 'a', sağ ileri için 'e', sol ileri için 'q', çıkış için 'x'")
            secim = input()
            self._uyuyor = False
            if secim == 'x':
                print("Hareket fonksiyonlarını kapattınız...")
                self._uyuyor = True
                break
            self.hareket(secim)
    def para_gonder(self, alici, miktar):
        """Başka bir karaktere para gönderir."""
        self._uyuyor = False
        if miktar > 0 and self._para >= miktar:
            self._para -= miktar
            alici._para += miktar
            print(f"{self._kimlik} karakterinden {alici.kimlik} karakterine {miktar} para gönderildi.")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")
        self._uyuyor = True


# Savaşçı sınıfı (Karakter'den miras alır)
class Savasci(Karakter):
    def __init__(self):
        super().__init__()
        self._silah = "Kılıç"

    def karakter_goster(self):
        super().karakter_goster()
        print(f"Silah: {self._silah}")

# Büyücü sınıfı (Karakter'den miras alır)
class Buyucu(Karakter):
    def __init__(self):
        super().__init__()
        self._buyu_gucu = random.randint(50, 100)

    def karakter_goster(self):
        super().karakter_goster()
        print(f"Büyü Gücü: {self._buyu_gucu}")

# Okçu sınıfı (Karakter'den miras alır)
class Okcu(Karakter):
    def __init__(self):
        super().__init__()
        self._hassasiyet = random.randint(50, 100)

    def karakter_goster(self):
        super().karakter_goster()
        print(f"Hassasiyet: {self._hassasiyet}")


    @property             #bir sınıfın özelliklerini bir metodun davranışıyla birleştirerek kapsülleme sağlar
    def kimlik(self):
        return self._kimlik

    @property
    def para(self):
        return self._para

    @para.setter
    def para(self, miktar):
        self._para = miktar

    def para_gonder(self, alici, miktar):
        """Başka bir karaktere para gönderir."""
        self._uyuyor = False
        if miktar > 0 and self._para >= miktar:
            self._para -= miktar
            alici._para += miktar
            print(f"{self._kimlik} karakterinden {alici.kimlik} karakterine {miktar} para gönderildi.")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")
        self._uyuyor = True

    def __eq__(self, other):              # iki nesnenin eşit olup olmadığını kontrol etmek için kullanılır.
        return self._guc == other._guc

    def __gt__(self, other):              # bir nesnenin başka bir nesneden büyük olup olmadığını kontrol eder.
        return self._guc > other._guc

    def __lt__(self, other):              # bir nesnenin başka bir nesneden küçük olup olmadığını kontrol eder.
        return self._guc < other._guc

    def uyku_kontrol(self):
        """Karakterin uyku durumunu kontrol eder."""
        while True:
            time.sleep(120)
            if not self._uyuyor:
                self._uyuyor = True
                print(f"{self._kimlik} karakteri uyuyor...")

    def aclik_susuzluk_azalt(self):
        """Belirli aralıklarla açlık ve susuzluk seviyelerini azaltır."""
        while True:
            time.sleep(12)
            if self._aclik > 0:
                self._aclik -= 1
            if self._susuzluk > 0:
                self._susuzluk -= 1

    def init(self):
        """Açlık, susuzluk ve uyku kontrollerini başlatır."""
        threading.Thread(target=self.aclik_susuzluk_azalt, daemon=True).start()
        threading.Thread(target=self.uyku_kontrol, daemon=True).start()


karakterler = []  # Karakterlerin tutulduğu liste

def karakter_bul(kimlik):
    """Kimlik numarasına göre karakteri bulur."""
    for karakter in karakterler:
        if karakter._kimlik == kimlik:
            return karakter
    return None

def karakter_islemleri(secilen_karakter):
    """Seçilen karakter üzerinde işlemleri yönetir."""
    while True:
        print("1. Karakteri besle")
        print("2. Karaktere su ver")
        print("3. Hareket fonksiyonlarını aktifleştir")
        print("4. Para gönder")
        print("5. Güç karşılaştırma")
        print("6. Karakter bilgilerini göster")
        print("7. Ana menüye dön")
        print("Q. Çıkış")
        secim = input()

        if secim == '1':
            secilen_karakter.karakter_besle()
        elif secim == '2':
            secilen_karakter.karakter_su_ver()
        elif secim == '3':
            secilen_karakter.hareketi_aktifleştir()
        elif secim == '4':
            alici_kimlik = int(input("Alıcı kimlik numarasını giriniz: "))
            miktar = int(input("Gönderilecek miktarı giriniz: "))
            alici_karakter = karakter_bul(alici_kimlik)
            if alici_karakter:
                secilen_karakter.para_gonder(alici_karakter, miktar)
            else:
                print("Geçersiz alıcı kimlik numarası.")
        elif secim == '5':
            karsilastirma_kimlik = int(input("Karşılaştırmak istediğiniz karakterin kimlik numarasını giriniz: "))
            karsilastirma_karakter = karakter_bul(karsilastirma_kimlik)
            if karsilastirma_karakter:
                if secilen_karakter == karsilastirma_karakter:
                    print("Karakterlerin gücü eşit.")
                elif secilen_karakter > karsilastirma_karakter:
                    print(f"{secilen_karakter._kimlik} karakteri daha güçlü.")
                else:
                    print(f"{karsilastirma_karakter._kimlik} karakteri daha güçlü.")
            else:
                print("Geçersiz karşılaştırma kimlik numarası.")
        elif secim == '6':
            secilen_karakter.karakter_goster()
        elif secim == '7':
            print("Ana menüye dönülüyor...")
            break
        elif secim.lower() == 'q':
            print("Program sonlandırılıyor...")
            exit(0)
        else:
            print("Geçersiz seçim.")

def main():
    """Ana program akışı."""
    # Metaverse evrenine hoşgeldiniz mesajını göster
    Karakter.metaverse_hoşgeldiniz()

    # Yeni karakterler oluştur ve listeye ekle
    savasci = Savasci()
    savasci.karakter_yarat()  # Özellikleri rastgele oluştur
    karakterler.append(savasci)  # Karakteri listeye ekle

    buyucu = Buyucu()
    buyucu.karakter_yarat()  # Özellikleri rastgele oluştur
    karakterler.append(buyucu)  # Karakteri listeye ekle

    okcu = Okcu()
    okcu.karakter_yarat()  # Özellikleri rastgele oluştur
    karakterler.append(okcu)  # Karakteri listeye ekle

    # Karakterlerin bilgilerini göster
    for karakter in karakterler:
        karakter.karakter_goster()
        print("-" * 30)

    while True:
        print("Lütfen bir karakter seçiniz: ")
        for index, karakter in enumerate(karakterler):
            print(f"{index + 1}. {type(karakter).__name__} (Kimlik: {karakter._kimlik})")
        print("Q. Çıkış")
        secim = input()

        if secim.isdigit() and 1 <= int(secim) <= len(karakterler):
            secilen_karakter = karakterler[int(secim) - 1]
            karakter_islemleri(secilen_karakter)
        elif secim.lower() == 'q':
            print("Program sonlandırılıyor...")
            exit(0)
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__": 
    main()
    