'''
<풀이 메모>
아예 못품 ㅎㅎ...
고민해봤는데 감이 도저히 안왔음

<답안 메모>
뒤쪽 날짜부터 거꾸로 확인하는 방식으로 접근하여 해결하는 DP 아이디어

1일 차에 상담을 진행하는 경우, 최대 이익은 '1일차의 상담 금액 + 4일부터의 상담 금액'이 된다.
이러한 원리를 이용하여 뒤쪽부터 계산한다.

뒤쪽부터 매 상담에 대하여
'현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤(dp[t[i] + i]])을 계산하면 된다.'
이후에 계산된 각각의 값 중에서 최댓값을 출력하면 된다.

'dp[i] = i번째 날부터 마지막 날까지 낼 수 있는 최대이익'이라고 하면
점화식은 dp[i] = max(p[i] + dp[t[i] + i], max_value)가 된다.
이때 max_value는 뒤에서부터 계산할 때, 현재까지의 최대 상담 금액에 해당하는 변수이다.

<Answer>
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
'''