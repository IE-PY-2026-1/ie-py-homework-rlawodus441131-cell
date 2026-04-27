#[2차 과제] My Quant Log
print('---My Quant Log : 매매 데이터 분석기---')

trade_history = [['시장지수', 2500, 2600, 1]]
total_sum = 0.0 # 복합 데이터 연산자 변수

print('\n--- 최근 매매 기록을 3건 입력하시오 ---')
for i in range(3):
    print(f'{i+1}번째 기록 : ')
    ticker = input('종목 : ')
    buy = float(input('매수가 : '))
    sell = float(input('매도가 : '))
    amount = float(input('수량 : '))

    trade_history.append([ticker, buy, sell, amount])
    total_sum += (buy * amount) #복합 대입 연산자
trade_history.insert(0, ['최근 이슈 종목', 1000, 1500, 10])
if len(trade_history) > 5:
    trade_history.pop()

print('\n---수익률 분석 리포트 ---')
analysis_data = trade_history[:] # 데이터 복사(공유 X)

for trade in analysis_data:
    name, buy, sell, amount = trade

    if buy == 0:
        continue #매수가가 만약 0일경우 다시 입력 하게 하기 위함
    profit_rate = ((sell - buy) / buy ) * 100
    invest_amount = buy * amount

    if profit_rate >= 20 or invest_amount >= 100000:
        grade = 'S'
        title = '시장의 지배자'
    elif profit_rate >= 20 or profit_rate < 0:
        if not (profit_rate < 0):
            grade = 'S'
            title = '전설의 트레이더'
        else:
            grade = 'F'
            title = '위험한 투자자'
    elif profit_rate >= 10:
        grade = 'A'
        title = '전물 트레이더'
    else:
        grade = 'B'
        title = '안정적 트레이더'

    print(f"종목: {name:10} | 수익률: {profit_rate:6.2f}% | 등급: [{grade}] | 칭호: {title}")
print(f"\n총 투자 누적액: {total_sum:,.0f}원")
    