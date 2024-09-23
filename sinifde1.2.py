import math
print("Gorusdukleri zamani daxil edin")
t = int(input())
print("1 ci qatarin 2cinin basladigi yere catdigi zamani daxil edin")
t1 = int(input())

t2 = (t**2 // t1)
t3 = ((t**2 / t1)-(t**2 // t1))*60
t3 = math.ceil(t3)

print(t2, int(t3))
