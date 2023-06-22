import wmi
from playsound import playsound
import time

def __main__():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")

    for _ in range(60):
        temperature_infos = w.Sensor()

        for sensor in temperature_infos:
            if sensor.SensorType == "Temperature" and sensor.Name in ["CPU Package", "GPU Core"]:
                    print(sensor.Name, sensor.Value)

                    if sensor.Value >= 80:
                        playsound('D:\\Python\\diploma_project_simple\\sounds\\beep.wav')
        time.sleep(5)           
if __name__ == "__main__":
    __main__()