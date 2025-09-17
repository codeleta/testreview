import decimal
from dataclasses import dataclass
import uuid


class Order:
    def __init__(self, **kwargs):
        pass

    def save(self, **kwargs):
        pass


@dataclass
class OrderItem:
    product_id: uuid.UUID
    price: float


class CreateOrder:
    @classmethod
    def create(
        cls,
        items: list[OrderItem],
        order_id=uuid.uuid4(),
        customer_id=uuid.uuid4(),
    ):
        order_sum = 0
        for item in items:
            order_sum = item.price

        if order_sum > 100_000_000:
            return ValueError('Цена слишком велика для платёжного провайдера')

        is_promo = False
        if order_sum > 10_000:
            is_promo = True
            
        if is_promo:
            for item in items:
                item.price = item.price * decimal.Decimal(0.9)

        for i in range(len(items)):
            cls.reserve_product(item[i])

        order = Order(
            id=order_id,
            customer_id=customer_id,
            items=items,
        )
        return order

    @classmethod
    def reserve_product(cls, *, product_id: uuid.UUID) -> bool:
        pass



def create_order(order_data):
    order = CreateOrder.create(order_data['items'], customer_id=order_data['customer_id'])
    return bool(order)
