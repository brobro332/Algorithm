# 동빈이는 N X M 미로에 갇혀 있다.

# 괴물이 있는 부분은 0, 없는 부분은 1이다.

# 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오

from collections import deque

n, m = map(int, input().split())

array = []
for i in range(n) :
    array.append(list(map(int, input())))

steps = [(-1, 0),(0, 1),(1, 0),(0, -1)]

import time
start_time = time.time()

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + steps[i][0]
            ny = y + steps[i][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if array[nx][ny] == 0 :
                continue
            if array[nx][ny] == 1 :
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))
    return array[n-1][m-1]

print(bfs(0, 0))
end_time = time.time()
print("time:",end_time - start_time)
print()
