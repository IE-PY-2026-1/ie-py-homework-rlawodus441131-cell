# 파일이름 :"나만의 퀀트 전략 매니저: My Quant Log"
# 작 성 자 :60212481 김재연

print("--- [Version 1] My Quant Log: 신입 트레이더 등록 ---")

# 1. 정보 입력받기 (문자열, 정수, 실수 혼합)
user_name = input("트레이더 이름을 입력하세요: ")
ticker = input("첫 매매 종목명을 입력하세요: ")
buy_price = float(input("매수 가격을 입력하세요: "))
sell_price = float(input("매도 가격을 입력하세요: "))
amount = int(input("매수 수량을 입력하세요: "))

# 2. 산술 연산
total_invest = buy_price * amount
total_revenue = sell_price * amount
profit_loss = total_revenue - total_invest
#매매 수익
profit_rate = (profit_loss / total_invest) * 100
#매매 수익률(백분율)

# 3. 결과 출력 (f-string 활용)
print(f"\n[{user_name}님의 첫 매매 보고서]")
print(f"종목: {ticker}")
print(f"총 투자금: {total_invest:,.0f}원")
print(f"최종 수익: {profit_loss:,.0f}원")
print(f"수익률: {profit_rate:.2f}%")
