from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass
    
    @abstractmethod
    def process(self, amount: float, details: dict) -> dict:
        pass

class CreditCardProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        return bool(details.get("card_number") and details.get("cvv"))

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid Details"}
        fee = amount * 0.029
        return {"success": True, "method": "credit_card", "amount": amount + fee, "fee": fee}

class BankTransferProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        return bool(details.get("iban"))

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid Details"}
        return {"success": True, "method": "bank_transfer", "amount": amount + 1.50, "fee": 1.50}

class PayPalProcessor(PaymentProcessor):
    def validate(self, details: dict) -> bool:
        email = details.get("email")
        return bool(email and "@" in email)

    def process(self, amount: float, details: dict) -> dict:
        if not self.validate(details):
            return {"success": False, "error": "Invalid Details"}
        fee = amount * 0.034 + 0.30
        return {"success": True, "method": "paypal", "amount": amount + fee, "fee": fee}

class PaymentFactory:
    def __init__(self):
        self._processors = {
            "credit_card": CreditCardProcessor,
            "bank_transfer": BankTransferProcessor,
            "paypal": PayPalProcessor
        }

    def get_processor(self, payment_type: str) -> PaymentProcessor:
        processor_class = self._processors.get(payment_type)
        if not processor_class:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()

if __name__ == "__main__":
    factory = PaymentFactory()
    processor = factory.get_processor("credit_card")
    result = processor.process(100.0, {"card_number": "1234567890123456", "cvv": "123"})
    print(result)\n