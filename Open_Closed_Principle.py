# # Bad Example
# class DiscountCalculator:
#     def calculate(self, customer_type, amount):
#         if customer_type == "gold":
#             return amount * 0.8
#         elif customer_type == "silver":
#             return amount * 0.9

# Good Example (using inheritance)
class DiscountStrategy:
    def calculate(self, amount):
        return amount

class GoldDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.8

class SilverDiscount(DiscountStrategy):
    def calculate(self, amount):
        return amount * 0.9

def get_discount(strategy: DiscountStrategy, amount):
    return strategy.calculate(amount)

print(get_discount(GoldDiscount(), 100))
