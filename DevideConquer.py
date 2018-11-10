# 분할정복 가장 가까운 점들 사이의 거리 구하는 Algorithm
import matplotlib.pyplot as plt


def distance(a, b, c, d):
    result = pow((pow(c - a, 2) + pow(d - b, 2)), 0.5)
    return result


def searching(alist):
    min = distance(alist[0][1], alist[0][2],
                   alist[1][1], alist[1][2])
    for i in range(1, len(alist)):
        if min > distance(alist[i - 1][1], alist[i - 1][2],
                          alist[i][1], alist[i][2]):
            min = distance(alist[i - 1][1], alist[i - 1][2],
                           alist[i][1], alist[i][2])
    return min


def minimum(a, b):
    if a > b:
        return b
    else:
        return a


def mid_search(minusy, plus, min):
    for i in range(len(plus)):
        if (plus[i][1] < min) and ((plus[i][2] < minusy + min) or (plus[i][2] > minusy - min)):
            return plus[i]
        else:
            return min


data_tuples = [('A', -8, 5),
                  ('B', -5, -3),
                  ('C', 1, 3),
                  ('D', 3, -6),
                  ('E', 6, 0),
                  ('F', 8, 8),
                  ('G', -1, 3)]
kbs = [(-8, -5, 1, 3, 6, 8, -1)]
mbc = [(5, -3, 3, -6, 0, 8, 3)]

list = sorted(data_tuples, key=lambda vertices: vertices[1])

plus = []
minus = []
for i in range(0, len(list)):
    if list[i][1] >= 0:
        plus.append(list[i])
    else:
        minus.append(list[i])
print(plus)
print(minus)
a = searching(plus)
b = searching(minus)
print("Left : ", a)
print("Right : ", b)
mini = minimum(a, b)
minim = []
for i in range(len(minus)):
    c = int(minus[i][2])
    minim = mid_search(c, plus, mini)
for i in range(0, len(minus)):
    if distance(minus[i][1], minus[i][2], minim[1], minim[2]) < mini:
        print("minimum value : ", distance(minus[i][1], minus[i][2], minim[1], minim[2]))

plt.figure()
plt.axvline(x=0, color='b', linestyle='-', linewidth=3)
plt.scatter(kbs, mbc)
plt.show()