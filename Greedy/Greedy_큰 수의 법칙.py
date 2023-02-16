## 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수는 만드는 법칙이다.

## 배열의 크기 N, 숫자가 더해지는 횟수 M, 반복 횟수 K

## 2, 4, 5로 이루어진 배열이 있을 때 M이 6이고 K가 2라고 가정하면

## 5 + 5 + 4 + 5 + 5 +4 = 28이 도출된다.

import time

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()

data.sort()

first = data[n-1]
second = data[n-2]
result = 0

while m != 0 :
    for i in range(k) :
        result += first
        m -= 1
        if m == 0 :
            break;
    result += second
    m -= 1

print(result)
end_time = time.time()
print("time :", end_time - start_time)
print()
