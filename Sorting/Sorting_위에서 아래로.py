# 수열에 속한 수의 개수 N이 주어질 때 수열을 내림차순으로 정렬하시오.

# 1 <= N <= 500

# 수의 범위는 1 이상 100,000 이하의 자연수이다.

array = []
n = int(input())

import time
start_time = time.time()

for i in range(n) :
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in range(len(array)) : 
    print(array[i], end=' ')
print()
end_time = time.time()
print("time:", end_time - start_time)
print()
