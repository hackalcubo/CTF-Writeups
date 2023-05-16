# Goldinospizza
<p align="center">
  <img src="Attachments/Description.png" />
</p>

## FLAG:
ptm{🍕 https://youtu.be/lpvT-Fciu-4 don't buy this crap, just make your own... https://www.giallozafferano.com/recipes/Pizza-Margherita.html 🍕}
#

## Solution
I downloaded the [source code](Attachments/goldinospizza.zip) provided by the challenge in the description and I found this python function quite interesting

```python
def order(data, ws, n):
    if "orders" not in data:
        raise AssertionError("NO 🍕 'orders' IN YOUR ORDER")
    if type(data["orders"]) is not list:
        raise AssertionError("NO 🍕 'orders' LIST IN YOUR ORDER")
    if n + len(data["orders"]) > max_requests:
        return len(data["orders"]), None
    for item in data["orders"]:
        if type(item) is not dict:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 ORDERS IS NOT AN ORDER")
        if "product" not in item:
            db.session.rollback()
            raise AssertionError("NO 🍕 'product' IN ONE OF YOUR ORDERS")
        if type(item["product"]) is not int:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 'product' IDS IS NOT INT")
        if "quantity" not in item:
            db.session.rollback()
            raise AssertionError("NO 🍕 'quantity' IN ONE OF YOUR ORDERS")
        if type(item["quantity"]) is not int:
            db.session.rollback()
            raise AssertionError("ONE OF YOUR 🍕 'quantity' IS NOT INT")
        product = db.session.execute(db.select(Product).filter(
            Product.id == item["product"])).scalars().one_or_none()
        if product is None:
            db.session.rollback()
            raise AssertionError("WE DON'T SELL THAT 🍕")
        quantity = item["quantity"]
        current_user.balance -= product.price * quantity #analyzed point
        if current_user.balance < 0:
            db.session.rollback()
            raise AssertionError("NO 🍕 STEALING ALLOWED!")
        db.session.add(Order(
            user_id=current_user.id,
            product_id=product.id,
            product_quantity=quantity,
            product_price=product.price
        ))
        if product.id == 0 and quantity > 0:
            ws.send(
                f"WOW you are SO rich! Here's a little extra with your golden special 🍕: {os.environ['FLAG']}")
    db.session.add(current_user)
    db.session.commit()
    return len(data["orders"]), {"ok": True, "balance": current_user.balance, "orders": _orders()}
In the `main` we can see what we have to do to have the flag (that is loaded in the stack):
```

The purpose of the challenge is to buy the most expensive product (the golden pizza) to get the flag however we have a very limited budget in euros. After a careful analysis of the proposed source code I saw that the quantity of the ordered product is updated directly without doing any checking. This line of code (analyzed point) allows me to enter any negative quantity I like so that the multiplied signs give me a positive quantity. Since an update occurs by subtraction of the studied values, by entering a negative value in my turn I get a positive value ("-" multiplied by "-" makes "+"). I can insert a negative value like -2, and my balance will be upgraded with the new value that can be used to buy the flag.