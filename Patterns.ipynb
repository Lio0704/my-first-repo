from abc import ABC, abstractmethod


# Abstract base class
class PaymentProcessor(ABC):

    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def calculate_fee(self, amount: float) -> float:
        pass

    def process(self, amount: float, details: dict) -> dict:
        validation_error = self.validate(details)
        if validation_error:
            return {"success": False, "error": validation_error}

        fee = self.calculate_fee(amount)
        total = amount + fee
        return {"success": True, "method": self.name, "amount": total, "fee": fee}


# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    name = "credit_card"

    def validate(self, details: dict):
        card_number = details.get("card_number")
        cvv = details.get("cvv")

        if not card_number or len(card_number) != 16:
            return "Invalid card number"
        if not cvv or len(cvv) != 3:
            return "Invalid CVV"
        return None

    def calculate_fee(self, amount: float) -> float:
        return amount * 0.029


class BankTransferProcessor(PaymentProcessor):
    name = "bank_transfer"

    def validate(self, details: dict):
        iban = details.get("iban")

        if not iban or len(iban) < 15:
            return "Invalid IBAN"
        return None

    def calculate_fee(self, amount: float) -> float:
        return 1.50


class PayPalProcessor(PaymentProcessor):
    name = "paypal"

    def validate(self, details: dict):
        email = details.get("email")

        if not email or "@" not in email:
            return "Invalid PayPal email"
        return None

    def calculate_fee(self, amount: float) -> float:
        return amount * 0.034 + 0.30


# Factory
class PaymentFactory:
    _processors = {
        "credit_card": CreditCardProcessor,
        "bank_transfer": BankTransferProcessor,
        "paypal": PayPalProcessor,
    }

    @classmethod
    def get_processor(cls, payment_type: str) -> PaymentProcessor:
        processor_class = cls._processors.get(payment_type)
        if not processor_class:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()

    @classmethod
    def register_processor(cls, payment_type: str, processor_class):
        cls._processors[payment_type] = processor_class


# Usage
if __name__ == "__main__":
    factory = PaymentFactory()

    # Credit card
    processor = factory.get_processor("credit_card")
    result = processor.process(100.0, {"card_number": "1234567890123456", "cvv": "123"})
    print(result)

    # Bank transfer
    processor = factory.get_processor("bank_transfer")
    result = processor.process(100.0, {"iban": "FR7630006000011234567890189"})
    print(result)

    # PayPal
    processor = factory.get_processor("paypal")
    result = processor.process(100.0, {"email": "user@example.com"})
    print(result)

from abc import ABC, abstractmethod


# Abstract base class
class PaymentProcessor(ABC):

    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def calculate_fee(self, amount: float) -> float:
        pass

    def process(self, amount: float, details: dict) -> dict:
        validation_error = self.validate(details)
        if validation_error:
            return {"success": False, "error": validation_error}

        fee = self.calculate_fee(amount)
        total = amount + fee
        return {"success": True, "method": self.name, "amount": total, "fee": fee}


# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    name = "credit_card"

    def validate(self, details: dict):
        card_number = details.get("card_number")
        cvv = details.get("cvv")

        if not card_number or len(card_number) != 16:
            return "Invalid card number"
        if not cvv or len(cvv) != 3:
            return "Invalid CVV"
        return None

    def calculate_fee(self, amount: float) -> float:
        return amount * 0.029


class BankTransferProcessor(PaymentProcessor):
    name = "bank_transfer"

    def validate(self, details: dict):
        iban = details.get("iban")

        if not iban or len(iban) < 15:
            return "Invalid IBAN"
        return None

    def calculate_fee(self, amount: float) -> float:
        return 1.50


class PayPalProcessor(PaymentProcessor):
    name = "paypal"

    def validate(self, details: dict):
        email = details.get("email")

        if not email or "@" not in email:
            return "Invalid PayPal email"
        return None

    def calculate_fee(self, amount: float) -> float:
        return amount * 0.034 + 0.30


# Factory
class PaymentFactory:
    _processors = {
        "credit_card": CreditCardProcessor,
        "bank_transfer": BankTransferProcessor,
        "paypal": PayPalProcessor,
    }

    @classmethod
    def get_processor(cls, payment_type: str) -> PaymentProcessor:
        processor_class = cls._processors.get(payment_type)
        if not processor_class:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()

    @classmethod
    def register_processor(cls, payment_type: str, processor_class):
        cls._processors[payment_type] = processor_class


# Usage
if __name__ == "__main__":
    factory = PaymentFactory()

    # Credit card
    processor = factory.get_processor("credit_card")
    result = processor.process(100.0, {"card_number": "1234567890123456", "cvv": "123"})
    print(result)

    # Bank transfer
    processor = factory.get_processor("bank_transfer")
    result = processor.process(100.0, {"iban": "FR7630006000011234567890189"})
    print(result)

    # PayPal
    processor = factory.get_processor("paypal")
    result = processor.process(100.0, {"email": "user@example.com"})
    print(result)


from abc import ABC, abstractmethod


# Abstract base class
class PaymentProcessor(ABC):

    @abstractmethod
    def validate(self, details: dict) -> bool:
        pass

    @abstractmethod
    def calculate_fee(self, amount: float) -> float:
        pass

    def process(self, amount: float, details: dict) -> dict:
        validation_error = self.validate(details)
        if validation_error:
            return {"success": False, "error": validation_error}

        fee = self.calculate_fee(amount)
        total = amount + fee
        return {"success": True, "method": self.name, "amount": total, "fee": fee}


# Concrete implementations
class CreditCardProcessor(PaymentProcessor):
    name = "credit_card"

    def validate(self, details: dict):
        card_number = details.get("card_number")
        cvv = details.get("cvv")

        if not card_number or len(card_number) != 16:
            return "Invalid card number"
        if not cvv or len(cvv) != 3:
            return "Invalid CVV"
        return None

    def calculate_fee(self, amount: float) -> float:
        return amount * 0.029


class BankTransferProcessor(PaymentProcessor):
    name = "bank_transfer"

    def validate(self, details: dict):
        iban = details.get("iban")

        if not iban or len(iban) < 15:
            return "Invalid IBAN"
        return None

    def calculate_fee(self, amount: float) -> float:
        return 1.50


class PayPalProcessor(PaymentProcessor):
    name = "paypal"

    def validate(self, details: dict):
        email = details.get("email")

        if not email or "@" not in email:
            return "Invalid PayPal email"
        return None

    def calculate_fee(self, amount: float) -> float:
        return amount * 0.034 + 0.30


# Factory
class PaymentFactory:
    _processors = {
        "credit_card": CreditCardProcessor,
        "bank_transfer": BankTransferProcessor,
        "paypal": PayPalProcessor,
    }

    @classmethod
    def get_processor(cls, payment_type: str) -> PaymentProcessor:
        processor_class = cls._processors.get(payment_type)
        if not processor_class:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()

    @classmethod
    def register_processor(cls, payment_type: str, processor_class):
        cls._processors[payment_type] = processor_class


# Usage
if __name__ == "__main__":
    factory = PaymentFactory()

    # Credit card
    processor = factory.get_processor("credit_card")
    result = processor.process(100.0, {"card_number": "1234567890123456", "cvv": "123"})
    print(result)

    # Bank transfer
    processor = factory.get_processor("bank_transfer")
    result = processor.process(100.0, {"iban": "FR7630006000011234567890189"})
    print(result)

    # PayPal
    processor = factory.get_processor("paypal")
    result = processor.process(100.0, {"email": "user@example.com"})
    print(result)
