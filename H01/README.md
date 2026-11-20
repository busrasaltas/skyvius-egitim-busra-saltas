# H01 – İHA Temel Bileşenleri ve Sistem Mimarisi

## Ne Yapıldı?
Bu modülde bir Quadcopter platformunu oluşturan 7 temel bileşenin (Batarya, ESC, Motor/Pervane, Uçuş Kontrolcüsü, Alıcı, Telemetri ve Görev Bilgisayarı) görevleri, aralarındaki güç ve veri bağlantıları incelendi. Seçmeli görev kapsamında ise sisteme kamera eklenerek görüntü akışının hangi bilgisayara gittiği şema ve açıklamayla gösterildi.

## Klasör Yapısı ve Kullanım
* `rapor.md`: 7 bileşenin görev tablosu, güç/veri bağlantıları ve yararlanılan B3–B5 video bölümleri.
* `iha_bilesen_blok_semasi.png`: Güç ve veri hatlarının ayrı çizgilerle gösterildiği 7 bileşenli sistem kartı.
* `secmeli-deneme-1/kamera-ekli-kart.md`: Kamera modülünün görevini, güç beslemesini ve görüntünün Görev Bilgisayarına aktarılma nedenini açıklayan doküman.
* `secmeli-deneme-1/iha_kamera_blok_semasi.png`: Kamera eklenmiş ve görüntü hattının işaretlendiği sistem kartı.

## Temel Bulgular
* Güç aktarımı ile veri ve kontrol bağlantılarının farklı görevleri olduğunu öğrendim. Batarya ve ESC motorlara güç sağlarken, kontrol ve veri hatları sistemdeki bileşenlerin iletişimini sağlıyor
* Kamera görüntüsü uçuş kontrolcüsüne değil, doğrudan Görev Bilgisayarına gönderilir; uçuş kontrolcüsü denge/motor kontrolünden ve görev bilgisayarından gelen otonom komutların uygulanmasından sorumludur.
