# N X M 크기의 얼음 틀이 있다.

# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.

# 이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를

# 구하는 프로그램을 작성하시오.

n, m = map(int, input().split())

array = []
for i in range(n) :
    array.append(list(map(int, input())))

import time
start_time = time.time()
    
def dfs(x, y) :
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    if array[x][y] == 0 :
        array[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result += 1
print(result)
end_time = time.time()
print("time:", end_time - start_time)
print()
