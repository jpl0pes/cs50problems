from helpers import apology, login_required, lookup, usd

quote = "AAPL"
stockarr = lookup(quote)
cenas = "A share of {} ({}) costs {}.".format(stockarr["name"],stockarr["symbol"] , stockarr["price"])

if stockarr != None:
    print(cenas)
else:
    print("Symbol is wrong")



<header>
    <div class="alert alert-primary border text-center" role="alert">
        Bought!
    </div>
</header>


else:
        symbol = request.form.get("symbol")
        quantity = int(request.form.get("shares"))
        name = request.form.get("name")
        price =  lookup(symbol)["price"]
        total =

        ##Insert Transactions into Tx table
        db.execute (
            "INSERT INTO transactions (user_id, stock_symbol, stock_name, stock_price, stock_qty)\
            VALUES(:user_id, :stock_symbol, :stock_name, :stock_price, :stock_qty)",\
            user_id = session["user_id"], stock_symbol = symbol, stock_name = name, stock_price = price, stock_qty = - quantity
        )
