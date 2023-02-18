## N X M 크기의 맵이 주어지고 캐릭터는 동서남북 중 한 곳을 바라본다.

## 0은 육지이고, 1은 바다이다.

## 캐릭터는 아래의 메뉴얼을 따른다.

## 1. 현재 위치에서 왼쪽 방향부터 차례대로 갈 곳을 정한다.

## 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면

## 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 아니라면 왼쪽으로 회전만 한다.

## 3. 만약 네 방향 모두 가봤거나 바다로 되어 있다면 방향을 유지한 채로

## 한 칸 뒤로 가고 1단계로 돌아간다. 이 때 뒤 쪽 방향이 바다라면 움직임을 멈춘다.

aa

n, m = map(int, input().split())
a, b, d = map(int, input().split())

array = []
for i in range(n) :
    array.append(list(map(int, input().split())))

import time
start_time = time.time()

gps = [[0] * m for i in range(n)]
gps[a][b] = 1
cnt = 1
t = 0

steps = [(-1, 0),(0, 1),(1, 0),(0, -1)]

def turn_left() :
    global d
    d -= 1
    if d < 0 :
        d = 3

while True :
    turn_left()
    x = a + steps[d][0]
    y = b + steps[d][1]
    if gps[x][y] == 0 and array[x][y] == 0 :
        gps[x][y] = 1
        a = x
        b = y
        cnt += 1
        t = 0
        continue
    else :
        t += 1
        
    if t == 4 :
        x = a - steps[d][0]
        y = b - steps[d][1]
        if array[x][y] == 0 :
            a = x
            b = y
        else :
            break
        t = 0
        
print(cnt)
end_time = time.time()
print("time :", end_time - start_time)
print()
