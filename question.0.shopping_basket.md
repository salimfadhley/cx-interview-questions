# Shopping Basket

## Requirements

You have been asked to implement a "shopping basket pricer" for a supermarket. 

This is a component which given a "basket" of products chosen by a customer, a "catalogue" of products available in a supermarket and a number of special offers on products will calculate the discounted price of the basket.

This is an important component of a shopping system. This component's responsibility is to calculate the correct final price of the items contained in the basket. You must design this component in such a way that it could be used by other developers. 

For any given basket, catalogue and offers your solution should return the sub-total, discount and total, all accurate to two decimal places. 

### Definitions

* **sub-total**: The undiscounted cost of items in a basket.
* **discount**: The amount of discount which must be applied to the subtotal in order to calculate the final price of the goods in the basket.
* **total**: The final price of goods in the basket once the discount has been applied. 
* **offers**: These are pricing rules which under some circumstances may cause one or more items in the basket to be discounted, and consequently change the final price of the basket.
* **catalogue**: The products currently sold by the supermarket. Every product has a name and a price.

### Behavior

* A basket can contain zero or more products. 
* An empty basket has a price of zero. 
* Baskets cannot have a negative price.
* The discount and therefore the total price is determined by the contents of the basket, the undiscounted price of the goods and the applicable offers.  
* As with all supermarkets, the prices of goods and the offers applicable to those goods may change from day to day.

Other considerations:
* We are only interested in the behavior of the shopping basket component. You do not need to build an API, web-interface or database. Try to stay focused on implementing the shopping basket, and especially the process by which we determine the total price of items in the basket.
* We expect that your solution can be implemented in without needing any 3rd-party libraries. If you do use a component which is not part of the standard library - please provide a mechanism for us to automatically install all project dependencies.
* Provide some documentation that will help us run your submission.
* You can assume all prices are in £GBP, no need to consider any other currencies.

### Catalogue

Use the following products and prices in your catalogue (you can represent this within your solution however you like):

The catalogue currentluy contains these items:

* **Baked Beans** £0.99
* **Biscuits** £1.20
* **Sardines** £1.89
* **Shampoo (Small)** £2.00
* **Shampoo (Medium)** £2.50
* **Shampoo (Large)** £3.50

### Offers

The supermarket currently has these offers:

* ***Baked Beans***: buy 2 get 1 free
* ***Sardines***: 25% discount

## Examples

Examples of what would be expected for a couple of different baskets...

### Basket 1

* Baked Beans x 4
* Biscuits x 1

Should give the results:

* sub-total: £5.16
* discount: £0.99
* total: £4.17

### Basket 2

* Baked Beans x 2
* Biscuits x 1
* Sardines x 2

Should give:

* sub-total: £6.96
* discount: £0.95
* total: £6.01

## Bonus Question 1

The supermarket wants to implement a new kind of offer: "Buy N of {X}, get the cheapest one for free", where N is a number of products that must be bought, and {X} is a subset of products from the catalogue that this offer is applicable to.

The supermarket is keen that the discounts should be applied fairly, so the rule must be interpreted to calculate the maximum possible discount given the set of applicable chosen products. This is complicated by the fact that a user may buy more than N products, or multiples of N applicable products.

## Bonus Question 2

Under some circumstances multiple discounts may be applicable to a single product.

For example:
* "Buy any 3 of Shampoo (Small), Shampoo (Medium) and Shampoo (Large), and you get the cheapest one for free.
* Shampoo Medium is 50% off

Make any changes to the shopping basket such that all rules are consistently applied

## Bonus Question 3

If you see any mistakes (typos, ambiguities) in this assignment, please feel free to make a pull request with those errors corrected.


