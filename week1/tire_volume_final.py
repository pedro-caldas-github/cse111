import math
import datetime

v = 0
x = datetime.date.today()

w = int(input("type the width of the tire(ex:205): "))
a = int(input("type the aspect ratio of the tire(ex:60): "))
d = int(input("type the diameter of the tire(ex:16): "))

v = math.pi*w**2*a*(w*a+2540*d)/10000000000

print(f"date:{x} - your tire volume is:{v:.2f}")

with open("volumes.txt", "a") as arquivo:
    arquivo.write(f"{x},{w},{a},{d},{v:.2f}\n")

print("This data was saved in volumes.txt")