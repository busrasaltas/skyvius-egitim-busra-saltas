# H01 Ana Görev Raporu: Quadcopter Bileşen Kartı

## 1. Yedi Bileşenin Görev, Enerji ve Veri Bağlantıları Tablosu

| Bileşen | Görevi | Enerji (Güç) Verdiği / Aldığı Parçalar | Veri Verdiği / Aldığı Parçalar |
| :--- | :--- | :--- | :--- |
| **Batarya (LiPo)** | Sistemin ana elektrik enerjisini sağlar. | **ESC**'lere yüksek akım verir; PDB/BEC üzerinden **Uçuş Kontrolcüsü** ve **Görev Bilgisayarına** regüle güç (5V) verir. | Akım/gerilim sensörü üzerinden **Uçuş Kontrolcüsüne** pil gerilim/akım verisi gönderir. |
| **ESC** | Uçuş kontrolcüsünden gelen düşük güçlü kontrol sinyallerini 3 fazlı akıma çevirerek motor devrini kontrol eder. | **Bataryadan** güç alır, **Motor/Pervane** grubuna güç verir (BEC varsa **Uçuş Kontrolcüsüne** 5V verebilir). | **Uçuş Kontrolcüsünden** PWM/DShot hız sinyali alır; destekliyorsa **Uçuş Kontrolcüsüne** RPM/sıcaklık verisi gönderir. |
| **Motor / Pervane** | Elektrik enerjisini dönme hareketine ve kaldırma/itki kuvvetine dönüştürür. | **ESC**'den 3 fazlı güç alır. | Veri göndermez veya almaz (mekanik itki üretir). |
| **Uçuş Kontrolcüsü** | Sensör verilerini (jiroskop, ivmeölçer vb.) okuyarak aracın dengesini sağlar ve motor/uçuş kontrolünü yönetir. | PDB/BEC'ten güç alır; **Alıcı** ve **Telemetri** modüllerine 5V güç verir. | **ESC**'lere motor sinyali gönderir; **Alıcı**'dan kumanda verisi alır; **Telemetri** ve **Görev Bilgisayarı** ile çift yönlü veri alışverişi yapar. |
| **Alıcı** | Yer kumandasından gelen kontrol sinyallerini alır. | **Uçuş Kontrolcüsünden** 5V güç alır. | **Uçuş Kontrolcüsüne** kumanda kontrol verisi gönderir (destekliyorsa temel telemetri geri döner). |
| **Telemetri** | İHA ile yer istasyonu arasında kablosuz veri iletişimi sağlar. | **Uçuş Kontrolcüsünden** 5V güç alır. | **Uçuş Kontrolcüsü** ile çift yönlü telemetri/komut verisi aktarır. |
| **Görev Bilgisayarı** | Görüntü işleme ve otonom görevler gibi yüksek işlem gücü gerektiren işlemleri yürütür. | Regüle güç hattından (5V) beslenir. | **Uçuş Kontrolcüsü** ile çift yönlü haberleşerek otonom komut/durum verisi paylaşır. |

## 2. Yararlanılan Video Bölümleri
* **B3:** Güç dağıtımı, batarya, ESC ve motor/pervane bileşenlerinin çalışma ve eşleşme mantığı[cite: 2].
* **B4:** Uçuş kontrolcüsü, alıcı ve telemetri bağlantıları ile kontrol/haberleşme hatları[cite: 2].
* **B5:** Görev bilgisayarı ve yüksek seviyeli otonom/veri işleme mimarisi[cite: 2].
