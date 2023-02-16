## N X M 형태로 놓인 숫자 카드에서

## 뽑을 행을 먼저 고르고,

## 그 중 가장 낮은 카드가 본인의 카드가 된다.

## 카드의 숫자가 상대보다 높아야 게임에 승리할 수 있다. 

n, m = map(int, input().split())
for i in range(n) :
    data = list(map(int, input().split()))
result = 0
min_value = 10001    

import time
start_time = time.time()

for i in data :
    min_value = min(data)
        
print(min_value)

end_time = time.time()
print("time :", end_time - start_time)
print()
