x = 5.1
y = 5
print(x.as_integer_ratio())  # (2871044762448691, 562949953421312)
print(y.as_integer_ratio())  # (5, 1)
print(x.is_integer())  # False
print(y.is_integer())  # True
print(y.bit_length())  # 3

print(5 / 2)  # 2.5
print(5 // 2)  # 2

x = 1
y = 2
z = 3
print(x < y < z)  # True

print(40 + 3.14) # 43.14
print(int(3.1415)) # 3
print(float(3)) # 3.0

# 1 > '1'  TypeError
# 1 + '1'  TypeError