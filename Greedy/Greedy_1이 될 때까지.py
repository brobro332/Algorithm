## K가 주어질 때 N이 될 때까지 1번 혹은 2번의 과정을

## 수행해야하는 횟수의 최솟값을 출력하라.

## 1. N에서 1을 뺀다.

## 2. N을 K로 나눈다. 단 두 번째 연산은 N이 K로 나누어떨어질 때만 가능하다.

n, k = map(int, input().split())

cnt = 0

​

import time

start_time = time.time()

​

while n != 1 :

    if n%k == 0 :

        n = n//k

        cnt += 1

    else :

        n -= 1

        cnt += 1

​

print(cnt)

end_time = time.time()

print("time :", end_time - start_time)

print()

​
