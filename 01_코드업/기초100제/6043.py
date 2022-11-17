f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
f3 = f1/f2
print(format(f3, ".3f"))
print("{:.3f}".format(f3))
print('%.3f'%f3)