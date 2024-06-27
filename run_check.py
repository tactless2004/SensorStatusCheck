#### Sensor Status Check
from colorama import Fore
from board import I2C
from adafruit_scd4x import SCD4X


def start():
    try:
        i2c = I2C()
        co2_temp_humidity_sensor = SCD4X(i2c)
        co2, temp, humidity = (
            co2_temp_humidity_sensor.CO2,
            co2_temp_humidity_sensor.temperature,
            co2_temp_humidity_sensor.relative_humidity,
        )
        print(f"{Fore.GREEN}SUCCESS{Fore.RESET}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    start()
