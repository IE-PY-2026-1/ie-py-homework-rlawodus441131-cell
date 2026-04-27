# 파일이름 :"나만의 퀀트 전략 매니저: My Quant Log"
# 작 성 자 :60212481 김재연

print("--- [V1.0] My Quant Log: 신입 트레이더 등록 ---")
user_name = input("트레이더 이름을 입력하세요: ")
ticker = input("첫 매매 종목명을 입력하세요: ")
buy_price = float(input("매수 가격을 입력하세요: "))
sell_price = float(input("매도 가격을 입력하세요: "))
amount = int(input("매수 수량을 입력하세요: "))

# [V2.0 추가] 1차 데이터 리스트화
# 1차 과제에서 받은 데이터를 [종목, 매수가, 매도가, 수량] 형태의 리스트로 만듦
trade_log = [[ticker, buy_price, sell_price, amount]] 

# [V2.0 추가] 리스트 조작 연습
# 1. append() 사용: 추가적인 매매 기록 등록
print("\n--- [V2.0] 추가 매매 등록 ---")
new_ticker = input("추가할 종목명: ")
new_buy = float(input("매수 가격: "))
new_sell = float(input("매도 가격: "))
new_amount = int(input("수량: "))
trade_log.append([new_ticker, new_buy, new_sell, new_amount])

# 2. insert() 사용: 중요 기록 최상단 삽입 (예: 시장 지수)
trade_log.insert(0, ["KOSPI지수", 2500, 2600, 1])

# [V2.0 추가] 데이터 분석 및 조건문
print("\n--- [성과 분석 리포트] ---")
# 3. 리스트 복사 ([:] 슬라이싱 활용) - 원본 trade_log 보호
analysis_list = trade_log[:] 

for trade in analysis_list:
    name, buy, sell, amt = trade # 언패킹
    profit_rate = ((sell - buy) / buy) * 100
    
    # 4. 조건문 (if-elif-else) - 등급 판정
    if profit_rate >= 10:
        grade = "S"
    elif profit_rate >= 0:
        grade = "A"
    else:
        grade = "F"
        
    print(f"종목: {name:10} | 수익률: {profit_rate:6.2f}% | 등급: [{grade}]")