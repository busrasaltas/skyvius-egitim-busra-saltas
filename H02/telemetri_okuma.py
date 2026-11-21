
import asyncio

from mavsdk_grpc import System


async def main():

    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    print("Araç bekleniyor...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Bağlandı")
            break

    print("Global konum kestirimi bekleniyor...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("Global konum hazır")
            break

    sayac = 0
    async for pos in drone.telemetry.position():
        print(
            f"Enlem: {pos.latitude_deg:.6f}, "
            f"Boylam: {pos.longitude_deg:.6f}, "
            f"Göreli irtifa: {pos.relative_altitude_m:.1f} m"
        )
        sayac += 1
        if sayac == 5:
            break

if __name__ == "__main__":
    asyncio.run(main())
