from collections import Counter
from dataclasses import dataclass, field
from typing import Callable, Iterator, Mapping, MutableMapping, Sequence, Set, Tuple


@dataclass
class Basket:
    contents: MutableMapping[str, int] = field(default_factory=Counter)

    def add(self, item_name: str, count: int = 1):
        self.contents[item_name] += count

    def __iter__(self) -> Iterator[str]:
        for item_name, count in self.contents.items():
            yield from [item_name] * count


@dataclass
class BasketPrice:
    sub_total: float
    discount: float

    def __iter__(self):
        yield self.sub_total
        yield self.discount
        yield self.sub_total - self.discount


Offer = Callable[[Basket, Mapping[str, float]], float]


def discounted_item(item_name: str, discount: float) -> Offer:
    def offer(basket: Basket, catalogue: Mapping[str, float]) -> float:
        return discount * basket.contents[item_name] * catalogue[item_name]

    return offer


def buy_x_get_y_free(item_name: str, x: int, y: int) -> Offer:
    def offer(basket: Basket, catalogue: Mapping[str, float]) -> float:
        return (basket.contents[item_name] // x) * catalogue[item_name] * y

    return offer


def cheapest_x_of_n_items_free(items: Set[str], n: int, x: int) -> float:
    def calculate_discount(sorted_items: Sequence[Tuple[float, str]]) -> float:
        if len(sorted_items) < n:
            return 0.0
        this_group: Sequence[Tuple[float, str]] = sorted_items[:n]
        next_group: Sequence[Tuple[float, str]] = sorted_items[n:]
        cheapest_x_items_of_this_group = this_group[-x:]

        this_group_discount: float = sum(g[0] for g in cheapest_x_items_of_this_group)

        return this_group_discount + calculate_discount(next_group)

    def offer(basket: Basket, catalogue: Mapping[str, float]) -> float:
        sorted_items = sorted(
            ((catalogue[i], i) for i in basket if i in items), reverse=True
        )
        return calculate_discount(sorted_items=sorted_items)

    return offer


@dataclass
class BuyXGetYFree:
    item_name: str
    x: int
    y: int


def price_basket(
    basket: Basket, catalogue: Mapping[str, float], offers: Sequence[Offer]
) -> BasketPrice:

    sub_total: float = sum(catalogue[i] * q for i, q in basket.contents.items())
    discounts = sum(o(basket, catalogue) for o in offers)

    return BasketPrice(sub_total, discounts)
