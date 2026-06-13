# [4차 과제] My Quant Log - V3.0
# 파일이름 : main.py
# 작성자 : 김재연

# 전역변수 선언 (이중 리스트 구조)
trade_history = [['시장지수', 2500, 2600, 1]]  # 이중 리스트 (2D List)
total_sum = 0.0


# =============================================
# 함수 정의
# =============================================

# 함수 1: 매매 기록 입력 (global + try-except 1번째)
def input_trade():
    global trade_history, total_sum
    print('\n--- 매매 기록을 입력하시오 ---')
    ticker = input('종목 : ')

    try:                                         # 예외처리 1: 숫자 입력 오류
        buy = float(input('매수가 : '))
        sell = float(input('매도가 : '))
        amount = float(input('수량 : '))
    except ValueError:
        print('⚠️ 숫자를 입력해야 합니다! 다시 시도해주세요.')
        return  

    trade_history.append([ticker, buy, sell, amount])  # 이중 리스트에 append로 누적
    total_sum += buy * amount

    trade_history.insert(0, ['최근 이슈 종목', 1000, 1500, 10])

    if len(trade_history) > 5:
        trade_history.pop()

    print('✅ 입력이 완료되었습니다!')


# 함수 2: 전체 기록 조회 (이중 순회 출력)
def show_trades():
    print('\n--- 📋 전체 매매 기록 조회 ---')
    if len(trade_history) == 0:
        print('기록이 없습니다.')
        return
    print(f"{'번호':<5} {'종목':<12} {'매수가':<10} {'매도가':<10} {'수량':<6}")
    print('-' * 50)
    for i in range(len(trade_history)):          # 중첩 for문 + 리스트 인덱싱
        trade = trade_history[i]
        for j in range(len(trade)):              # 이중 순회
            if j == 0:
                print(f"{i+1:<5} ", end='')
                print(f"{trade[j]:<12}", end='')
            elif j == 1 or j == 2:
                print(f"{trade[j]:<10.0f}", end='')
            else:
                print(f"{trade[j]:<6.0f}")


# 함수 3: 수익률 계산 (매개변수 + return)
def calc_profit_rate(buy, sell):
    if buy == 0:
        return 0.0
    profit_rate = ((sell - buy) / buy) * 100
    return profit_rate


# 함수 4: 등급 및 칭호 판정 (매개변수 + return)
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
    return grade, title


# 함수 5: 수익률 분석 리포트
def show_analysis():
    print('\n--- 📊 수익률 분석 리포트 ---')
    analysis_data = trade_history[:]

    for trade in analysis_data:
        name, buy, sell, amount = trade
        profit_rate = calc_profit_rate(buy, sell)
        invest_amount = buy * amount
        grade, title = get_grade(profit_rate, invest_amount)
        print(f"종목: {name:10} | 수익률: {profit_rate:6.2f}% | 등급: [{grade}] | 칭호: {title}")

    print(f'\n총 투자 누적액: {total_sum:,.0f}원')


# 함수 6: 파일 저장 (with open + try-except 2번째)
def save_to_file():
    try:                                         # 예외처리 2: 파일 저장 오류
        with open('trade_history.csv', 'w', encoding='utf-8') as f:
            f.write('번호,종목,매수가,매도가,수량\n')
            for i in range(len(trade_history)):
                trade = trade_history[i]
                f.write(f"{i+1},{trade[0]},{trade[1]},{trade[2]},{trade[3]}\n")
        print('✅ trade_history.csv 파일로 저장되었습니다!')
    except Exception as e:
        print(f'⚠️ 파일 저장 중 오류가 발생했습니다: {e}')


# 함수 7: 파일 불러오기 (try-except FileNotFoundError)
def load_from_file():
    global trade_history
    try:                                         # 예외처리 3: 파일 없을 때
        with open('trade_history.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            trade_history = []
            for line in lines[1:]:               # 헤더 제외
                parts = line.strip().split(',')
                name = parts[1]
                buy = float(parts[2])
                sell = float(parts[3])
                amount = float(parts[4])
                trade_history.append([name, buy, sell, amount])
        print('✅ 파일에서 데이터를 불러왔습니다!')
    except FileNotFoundError:
        print('⚠️ 저장된 파일이 없습니다. 기본 데이터를 사용합니다.')


# 메인 로직 - while 무한루프 + 메뉴
print('===================================')
print('   ---My Quant Log : 매매 데이터 분석기 V3.0---')
print('===================================')

while True:
    print('\n======= 📌 메인 메뉴 =======')
    print('1. 매매 기록 입력')
    print('2. 전체 기록 조회')
    print('3. 수익률 분석')
    print('4. 파일 저장')
    print('5. 파일 불러오기')
    print('6. 종료')
    print('============================')

    choice = input('메뉴를 선택하세요 (1~6): ')

    if choice == '1':
        input_trade()
    elif choice == '2':
        show_trades()
    elif choice == '3':
        show_analysis()
    elif choice == '4':
        save_to_file()
    elif choice == '5':
        load_from_file()
    elif choice == '6':
        save_to_file()       # 종료 전 자동 저장
        print('\n👋 프로그램을 종료합니다. 성공적인 투자 되세요!')
        break
    else:
        print('⚠️ 1~6 중에서 선택해 주세요.')