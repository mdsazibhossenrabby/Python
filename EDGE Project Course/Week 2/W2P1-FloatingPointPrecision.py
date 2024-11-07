
import math
radius=7.5 #floating point
area=math.pi*(radius**2)
print(f"The Area (no round) is : {area}")
print(f"The Area (full round) is : {round(area)}")
print(f"The Area (in range round) is : {round(area,2)}")