# Скорость в конце пути и путь, пройденный за время t с ускорением a  при v0=0.
print("Укажите время t: ")
t = float(input())
print("Укажите ускорение a: ")
a = float(input())
v = a * t
s = (a * pow(t, 2)) / 2
print("Скорость в конце пути", v, ", путь", s)
