# N개의 원소로 구성된 두 배열을 최대 K번의 바꿔치기 연산을 수행하여

# 배열 A의 모든 원소의 합이 최대가 되도록 하여 출력하시오.

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

import time
start_time = time.time()

a.sort()
b.sort(reverse=True)

for i in range(k) :
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else :
        break
print(sum(a))
end_time = time.time()
print("time:", end_time - start_time)
print()
