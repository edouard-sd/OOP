from abc import ABC, abstractmethod

class OrderComponent(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass
    @abstractmethod
    def get_description(self) -> str:
        pass

class BaseOrder(OrderComponent):
    def __init__(self, base_price: float):
        self.base_price = base_price
    def get_cost(self) -> float:
        return self.base_price
    def get_description(self) -> str:
        return f"Base price: {self.base_price}€"

class OrderDecorator(OrderComponent):
    def __init__(self, order: OrderComponent):
        self.order = order
    def get_cost(self) -> float:
        return self.order.get_cost()
    def get_description(self) -> str:
        return self.order.get_description()

class ExpressShippingDecorator(OrderDecorator):
    def get_cost(self): return super().get_cost() + 15.00
    def get_description(self): return super().get_description() + "\nExpress shipping: +15.00€"

class InsuranceDecorator(OrderDecorator):
    def get_cost(self): return super().get_cost() + (super().get_cost() * 0.05)
    def get_description(self): return super().get_description() + "\nInsurance (5%): Added"

class GiftWrapDecorator(OrderDecorator):
    def get_cost(self): return super().get_cost() + 5.00
    def get_description(self): return super().get_description() + "\nGift wrap: +5.00€"

class DiscountDecorator(OrderDecorator):
    def __init__(self, order, percent):
        super().__init__(order)
        self.percent = percent
    def get_cost(self): return super().get_cost() - (super().get_cost() * (self.percent / 100))
    def get_description(self): return super().get_description() + f"\nDiscount ({self.percent}%): Added"

class PremiumMemberDecorator(OrderDecorator):
    def get_cost(self): return super().get_cost() - (super().get_cost() * 0.10)
    def get_description(self): return super().get_description() + "\nPremium member (10%): Added"

if __name__ == "__main__":
    order = BaseOrder(100.00)
    order = ExpressShippingDecorator(order)
    order = InsuranceDecorator(order)
    order = GiftWrapDecorator(order)
    order = DiscountDecorator(order, percent=15)
    order = PremiumMemberDecorator(order)

    print(order.get_description())
    print(f"Total: {order.get_cost()}€")\n