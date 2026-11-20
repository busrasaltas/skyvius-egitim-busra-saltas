# Seçmeli Görev (Deneme 1): Kamera Ekli Bileşen Kartı

## Eklenen Bileşen: Kamera
* **Görevi:** Uçuş sırasında ortamdan görüntü yakalamak.
* **Güç Bağlantısı:** **Görev Bilgisayarı** (veya regüle 5V hattı) üzerinden beslenir.
* **Veri Bağlantısı (Görüntü Hangi Bilgisayara Gider?):** Kamera görüntüsü **Görev Bilgisayarına** (CSI / USB hattı üzerinden) gider. Uçuş kontrolcüsü gerçek zamanlı denge ve motor komutlarına odaklanır; yüksek bant genişliği gerektiren video verisi görev bilgisayarı tarafından işlenir ve gereken otonom komutlar görev bilgisayarından uçuş kontrolcüsüne iletilir.
