import psutil 
import os 
print(psutil.cpu_percent(interval=1))
battery = psutil.sensors_battery()
print(f"Battery: {battery.percent}%")
print(f"Time left: {battery.secsleft}")
