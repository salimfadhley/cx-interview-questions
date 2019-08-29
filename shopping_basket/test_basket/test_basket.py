from basket.basket import (
    Basket,
    buy_x_get_y_free,
    cheapest_x_of_n_items_free,
    discounted_item,
    price_basket,
)


def test_price_empty_basket():
    b = Basket()
    c = {}
    o = {}

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 0
    assert discount == 0
    assert total == 0


def test_price_basket_with_single_item():
    b = Basket()
    b.add(item_name="peas")
    c = {"peas": 2.01}
    o = {}

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 2.01
    assert discount == 0
    assert total == 2.01


def test_price_basket_with_two_identical_items():
    b = Basket()
    b.add(item_name="peas", count=2)
    c = {"peas": 2.01}
    o = {}

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 4.02
    assert discount == 0
    assert total == 4.02


def test_price_basket_with_a_single_discunted_item():
    b = Basket()
    b.add(item_name="peas", count=1)
    c = {"peas": 2.02}
    o = [discounted_item("peas", 0.5)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 2.02
    assert discount == 1.01
    assert total == 1.01


def test_price_basket_with_a_single_discunted_item_and_one_not():
    b = Basket()
    b.add(item_name="peas", count=1)
    b.add(item_name="pickle", count=1)
    c = {"peas": 2.02, "pickle": 4.00}
    o = [discounted_item("peas", 0.5)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 6.02
    assert discount == 1.01
    assert total == 5.01


def test_price_basket_buy_three_get_one_free_not_applicable():
    b = Basket()
    b.add(item_name="peas", count=2)
    c = {"peas": 2.02, "pickle": 4.00}
    o = [buy_x_get_y_free("peas", x=3, y=1)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 4.04
    assert discount == 0
    assert total == 4.04


def test_price_basket_buy_three_get_one_free_applicable():
    b = Basket()
    b.add(item_name="peas", count=3)
    c = {"peas": 2.0}
    o = [buy_x_get_y_free("peas", x=3, y=1)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 6.0
    assert discount == 2.0
    assert total == 4.0


def test_price_basket_buy_three_get_one_free_applicable_twice():
    b = Basket()
    b.add(item_name="peas", count=6)
    c = {"peas": 2.0}
    o = [buy_x_get_y_free("peas", x=3, y=1)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 12.0
    assert discount == 4.0
    assert total == 8.0


def test_price_basket_buy_three_get_one_free_applicable_twice_with_one_extra():
    b = Basket()
    b.add(item_name="peas", count=7)
    c = {"peas": 2.0}
    o = [buy_x_get_y_free("peas", x=3, y=1)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 14.0
    assert discount == 4.0
    assert total == 10.0


def test_price_basket_cheapest_of_n_feee_0():
    b = Basket()
    b.add(item_name="peas", count=2)
    b.add(item_name="shampoo", count=1)
    c = {"peas": 2.0, "shampoo": 1.50}
    o = [cheapest_x_of_n_items_free(items={"peas", "shampoo"}, n=3, x=1)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 5.50
    assert discount == 1.50
    assert total == 4.0


def test_price_basket_cheapest_of_n_feee_with_extra_items():
    b = Basket()
    b.add(item_name="peas", count=3)
    b.add(item_name="shampoo", count=1)
    c = {"peas": 2.0, "shampoo": 1.50}
    o = [cheapest_x_of_n_items_free(items={"peas", "shampoo"}, n=3, x=1)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 7.50
    assert discount == 2.00


def test_price_basket_cheapest_of_n_feee_with_two_qalifying_groups():
    b = Basket()
    b.add(item_name="peas", count=3)
    b.add(item_name="shampoo", count=3)
    c = {"peas": 2.0, "shampoo": 1.50}
    o = [cheapest_x_of_n_items_free(items={"peas", "shampoo"}, n=3, x=1)]

    sub_total, discount, total = price_basket(basket=b, catalogue=c, offers=o)

    assert sub_total == 10.50
    assert discount == 3.50
