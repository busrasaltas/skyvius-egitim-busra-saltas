# H03 · Kurulum günlüğü

- Yöntem: WSL2
- Ubuntu sürümü: 22.04

## Hatalar ve çözümler

--Arka plandaki yoğun sistem yükü nedeniyle gerçek zamanlı saat senkronizasyonu (`timesync`) ve
ivmeölçer sensörü (`Accelerometer sensor #0 failure: Timeout`) zaman aşımı hataları oluştu; QGroundControl üzerinde telemetri ve rota verileri saptı.

--Arka planda çalışan gereksiz uygulamalar ve açık simülasyon pencereleri kapatıldı. 
Sonra Gazebo, PX4 ve QGroundControl yeniden başlatılarak sorunsuz bağlantı sağlandı.

## Başlatma Komutu

cd ~/PX4-Autopilot
make px4_sitl gz_x500
