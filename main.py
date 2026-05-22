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