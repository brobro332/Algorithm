## 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때

## 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.

## 이때 행 위치는 1부터 8까지이고,

## 열 위치는 a부터 h까지이다.


a = input()

import time
start_time = time.time()

row = int(a[1])
column = int(ord(a[0]))-96

steps = [(1, 2),(-1, 2),(2, 1),(2, -1),(-2, 1),(-2, -1),(1, -2),(-1, -2)]

cnt = 0

for step in steps :
    next_r = row + step[0]
    next_c = column + step[1]

    if 1 <= next_r <= 8 and 1 <= next_c <= 8 :
        cnt += 1
print(cnt)
end_time = time.time()
print("time :", end_time - start_time)
print()
