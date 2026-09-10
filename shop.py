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