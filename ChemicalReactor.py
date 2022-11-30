a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
t = float(input("t = "))
k1 = float(input("k1 = "))
k2 = float(input("k2 = "))
N = input("The range of the reactor : ")

# a = 100
# b = 50
# c = 0
# t = 0.1
# k1 = 0.008
# k2 = 0.002
for i in range(int(N)):
    print(a, b, c)
    a = a + (k2 * c - k1 * a * b) * t
    b = b + (k2 * c - k1 * a * b) * t
    c = c + (2 * k1 * a * b - k2 * c) * t
