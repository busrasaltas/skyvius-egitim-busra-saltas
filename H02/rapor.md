# Pixhawk → PX4 → MAVLink → QGC / MAVSDK


## 1. Kavram tablosu

| Kavram | Türü | Görevi |
|---|---|---|
| **Pixhawk** | Donanım | Sensörleri, işlemciyi ve motor/servo çıkışlarını taşıyan uçuş kontrol kartı. |
| **PX4** | Yazılım (otopilot firmware) | Pixhawk üzerinde çalışır; sensör verisinden konum/duruş kestirir, uçuş modlarını ve motor komutlarını üretir. ArduPilot aynı kartlar için alternatif firmware'dir. |
| **MAVLink** | Protokol | Araç ile yer tarafı arasında telemetri, komut ve parametre taşıyan hafif mesaj formatı. |
| **QGroundControl (QGC)** | Yer istasyonu uygulaması (yazılım) | MAVLink ile araca bağlanan, harita, kurulum ve izleme sunan insan arayüzü. |
| **MAVSDK** | Kütüphane | MAVLink'i kod yazarak kullanmayı sağlar (ör. Python/C++); araca komut gönderen script'ler yazılır. |

Akış: Pixhawk (donanım) üzerinde PX4 çalışır → PX4, MAVLink ile konuşur → karşı uçta ya QGC (kullanıcı arayüzü) ya da MAVSDK (kendi kodun) bulunur.

## 2. Mod karşılaştırması

| Mod | İşi | İhtiyaç duyduğu konum bilgisi |
|---|---|---|
| **PX4 Position** (Multicopter) | Sticklar ortadayken araç fren yapar, dengelenir ve rüzgâra karşı 3B uzayda konumunu korur. Pilot elle kumanda eder. | Global konum kestirimi gerekir; GPS veya uygun başka konum kaynağı sağlayabilir.|
| **ArduPilot Loiter** (Copter) | Mevcut konumu, yönü ve irtifayı korumaya çalışır; stick bırakılınca araç yavaşlayıp durur ve konumda kalır. | Normalde GPS ile geçerli konum gerekir; uygun GPS dışı konum kaynağı da kullanılabilir.|

Not: İki mod işlev olarak benzerdir (pilot kumandalı konum tutma), isimleri ve parametreleri farklıdır.

## 3. Kaynaklar

1. PX4 Guide, Position Mode (Multicopter): https://docs.px4.io/main/en/flight_modes_mc/position
2. ArduPilot Copter Documentation, Loiter Mode: https://ardupilot.org/copter/docs/loiter-mode.html

