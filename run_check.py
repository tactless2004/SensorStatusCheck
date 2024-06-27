#### Sensor Status Check
from colorama import Fore
from board import I2C
from adafruit_scd4x import SCD4X
from emoji import emojize


def SCD41_Check():
    try:
        i2c = I2C()
        co2_temp_humidity_sensor = SCD4X(i2c)
        co2, temp, humidity = (
            co2_temp_humidity_sensor.CO2,
            co2_temp_humidity_sensor.temperature,
            co2_temp_humidity_sensor.relative_humidity,
        )
        return (True, "SUCCESS")

    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    SCD41 = SCD41_Check()
    if not SCD41[0]:
        print(
            f"{emojize(string=':x:')}{Fore.RED}SCD41 Sensor failed check {Fore.RESET}\n * {SCD41[1]}"
        )
