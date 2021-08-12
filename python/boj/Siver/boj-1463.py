n = int(input())
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0 for _ in range(n+1)]

for i in range(2, n+1):
    # 현재 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

   # 현재 수에서 2로 나누어 떨어지는 경우
    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    # 현재 수에서 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)

print(d[n])