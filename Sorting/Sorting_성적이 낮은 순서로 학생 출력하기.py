# N명의 학생 정보가 있다. 

# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순으로 학생 이름을

# 출력하시오.

# 1 <= N <= 100,000

array = []
n = int(input())

for i in range(n) :
    a = input().split()
    array.append((a[0], a[1]))

import time
start_time = time.time()

array = sorted(array, key=lambda name : name[1])

for name in array :
    print(name[0], end=' ')
print()
end_time = time.time()
print("time:",end_time - start_time)
print()
