# [3차 과제] My Quant Log - V2.0
# 파일이름 : main.py
# 작성자 : 김재연
trade_history = [['시장지수', 2500, 2600, 1]]  #초기 데이터
total_sum = 0.0  # 총 투자 누적액 (전역변수)
#매매 기록 입력(global사용)
def input_trade():
    global trade_history, total_sum  # 전역변수 수정을 위해 global 선언
    print('\n--- 매매 기록을 입력하시오 ---')
    ticker = input('종목 : ')
    buy = float(input('매수가 : '))
    sell = float(input('매도가 : '))
    amount = float(input('수량 : '))
 
    trade_history.append([ticker, buy, sell, amount])
    total_sum += buy * amount  # 복합 대입 연산자
 
    # 최근 이슈 종목을 리스트 맨 앞에 삽입
    trade_history.insert(0, ['최근 이슈 종목', 1000, 1500, 10])
 
    # 리스트가 5개 초과하면 가장 오래된 항목 제거
    if len(trade_history) > 5:
        trade_history.pop()
 
    print('✅ 입력이 완료되었습니다!')
# 매매 기록 조회
def show_traders():
    print('/n---📋 전체 매매 기록 조회 ---')
    if len(trade_history) == 0:
        print('기록이 없습니다.')
        return
    print(f"{'번호' :<5} {'종목':<12} {'매수가':<10} {'매도가':<10} {'수량':<6} ")
    print('-' * 50)
    for i, trade in enumerate(trade_history):
        name, buy, sell, amount = trade
        print(f"{i+1:<5} {name:<12} {buy:<10.0f} {sell:<10.0f} {amount:<6.0f}")
# 수익률 계산 후 반환
def calc_profit_rate(buy, sell):
    if buy == 0:
        return 0.0  
    profit_rate = ((sell - buy) / buy) * 100
    return profit_rate 
#등급 및 칭호 판정
def get_grade(profit_rate, invest_amount):
    if profit_rate >= 20 and invest_amount >= 100000:
        grade = 'S'
        title = '시장의 지배자 (고액 거물)'
    elif profit_rate >= 20:
        grade = 'S'
        title = '전설의 트레이더'
    elif profit_rate >= 10:
        grade = 'A'
        title = '전문 트레이더'
    elif profit_rate >= 0:
        grade = 'B'
        title = '안정적 트레이더'
    else:
        grade = 'F'
        title = '위험한 투자자'
    return grade, title  #튜플로 반환
#수익률 분석 및 리포트 출력
def show_analysis():
    print('\n--- 📊 수익률 분석 리포트 ---')
    analysis_data = trade_history[:]  # 데이터 복사 (원본 보호)
 
    for trade in analysis_data:
        name, buy, sell, amount = trade
 
        profit_rate = calc_profit_rate(buy, sell) 
        invest_amount = buy * amount
 
        grade, title = get_grade(profit_rate, invest_amount) 
 
        print(f"종목: {name:10} | 수익률: {profit_rate:6.2f}% | 등급: [{grade}] | 칭호: {title}")
 
    print(f'\n총 투자 누적액: {total_sum:,.0f}원')
#메인 로직(whie True - 무한 루프)
print('===================================')
print('   ---My Quant Log : 매매 데이터 분석기---')
print('===================================')
 
while True:
    print('\n======= 📌 메인 메뉴 =======')
    print('1. 매매 기록 입력')
    print('2. 전체 기록 조회')
    print('3. 수익률 분석')
    print('4. 종료')
    print('============================')
 
    choice = input('메뉴를 선택하세요 (1~4): ')
 
    if choice == '1':
        input_trade()       # 함수 호출
    elif choice == '2':
        show_trades()       # 함수 호출
    elif choice == '3':
        show_analysis()     # 함수 호출
    elif choice == '4':
        print('\n👋 프로그램을 종료합니다. 성공적인 투자 되세요!')
        break               # 종료 메뉴 선택 시 break
    else:
        print('⚠️ 1~4 중에서 선택해 주세요.')