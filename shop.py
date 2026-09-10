class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        """구매 금액의 5%를 포인트로 적립한다."""
        self.points += int(amount * 0.05)

    def get_discount_rate(self):
        """등급별 할인율을 반환한다."""
        if self.grade == "vip":
            return 0.10
        return 0.03

    def summary(self):
        # "[vip] 김서강 (포인트: 2,250)" 형식 문자열 반환
        return (f"[{self.grade}] {self.name} (포인트: {self.points:,.0f})")

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer     # Customer 인스턴스를 참조
        self.items = items           # [(상품명, 가격), ...] 튜플의 리스트

    def total_price(self):
        """주문 총액 (고객 등급 할인 적용)"""
        subtotal = sum(price for _, price in self.items)
        discount = self.customer.get_discount_rate()
        return int(subtotal * (1 - discount))

    # 상품 추가
    def add_item(self, name, price):
        self.items.append((name, price))

    # 결제 완료 시 customer.add_points()가 호출
    def pay(self): 
        self.customer.add_points(self.total_price())

"""검증 코드"""
# 파일 하단에 고객 2명(vip 1명, basic 1명)과 주문 3건을 생성
# 각 주문의 총액과 결제 후 고객별 포인트를 print로 출력
# 커밋 단위: Customer 완성 / Order 완성 / 검증 시나리오 완성 — 최소 3커밋.

c1 = Customer("김서강", "vip")
c2 = Customer("박강서")

order1 = Order("A-1001", c1, [("라떼", 5500), ("크루아상", 4200)])
order2 = Order("A-1002", c1, [("아메리카노", 3500), ("케이크", 8500)])
order3 = Order("A-1003", c2, [("스무디", 7000), ("쿠키", 3000)])

print(f"[주문 번호: {order1.order_id}] {order1.customer.name}님의 결제 금액: {order1.total_price():,}원")
print(f"[주문 번호: {order2.order_id}] {order2.customer.name}님의 결제 금액: {order2.total_price():,}원")
print(f"[주문 번호: {order3.order_id}] {order3.customer.name}님의 결제 금액: {order3.total_price():,}원")

order1.pay()
order2.pay()
order3.pay()

print(c1.summary())
print(c2.summary())