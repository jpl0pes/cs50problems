import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
##if not os.environ.get("API_KEY"):
    ##raise RuntimeError("API_KEY not set")

alert = "buy"

@app.route("/", methods=["GET","POST"])
@login_required
def index():
    """Show portfolio of stocks"""

    if request.method == "GET":
        portfolio_list= []

        ##Get all the Symbols and Names
        symbols_list = db.execute("SELECT DISTINCT(stock_symbol) FROM transactions WHERE user_id = :user_id",\
        user_id = session["user_id"])
        ##print(symbols_list)
        ##print(session["user_id"])
        ##print(len(symbols_list))

        ##Define total portfolio variable
        total_portfolio = 0

        ##Get quantity for each symbol and price
        for i in range(len(symbols_list)):

            ##get name
            list_name = db.execute("SELECT DISTINCT(stock_name) as 'name' FROM transactions WHERE user_id = :user_id AND stock_symbol = :stock_symbol",\
            user_id = session["user_id"], stock_symbol = symbols_list[i]["stock_symbol"])
            name = list_name[0]["name"]
            ##print(name, i)

            ##get quantity
            list_shares = db.execute("SELECT sum(stock_qty) as 'quantity' FROM transactions WHERE user_id = :user_id AND stock_symbol = :stock_symbol",\
            user_id = session["user_id"], stock_symbol = symbols_list[i]["stock_symbol"])
            shares = list_shares[0]["quantity"]

            ##get prices & Total
            price = lookup(symbols_list[i]["stock_symbol"])["price"]
            total = price * shares
            total_portfolio = total_portfolio + total

            ##put in list
            if shares != 0:
                portfolio_list.append( {
                    "symbol": symbols_list[i]["stock_symbol"],
                    "name": name,
                    "shares": shares,
                    "price": usd(price),
                    "total": usd(total)
            }
            )

        cash = db.execute("SELECT cash FROM users WHERE id= :id", id = session["user_id"])[0]["cash"]
        total_portfolio = total_portfolio + cash

        ##print(cash)
        ##print(portfolio_list)
        ##print(total_portfolio)
        return render_template("index.html",portfolio_list = portfolio_list, cash = usd(cash), total_portfolio = usd(total_portfolio))


        ##Update Users Table
        db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash = cash + total, user_id = session["user_id"])
        flash("Sold!")
        return redirect("/")

        ##return apology("TODO INDEX")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide valid symbol", 403)
        # Ensure quantity was submitted
        elif not request.form.get("quantity"):
            return apology("must provide valid number of shares", 403)


        ##get symbol and lookup on the API
        symbol = request.form.get("symbol")
        stockarr = lookup(symbol)

        ##hanlde if lookup return none
        if stockarr == None:
            return apology("Invalid Symbol of Stock")

        ##Check how much is the purchase
        quantity = float(request.form.get("quantity"))
        price = float(stockarr["price"])
        total = price * quantity
        name = stockarr["name"]

        ##Check if the user has enought cash
        tmplist = db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])
        user_cash = tmplist[0]["cash"]

        if user_cash > total:
            ##Insert Transactions into Tx table
            db.execute (
                "INSERT INTO transactions (user_id, stock_symbol, stock_name, stock_price, stock_qty)\
                VALUES(:user_id, :stock_symbol, :stock_name, :stock_price, :stock_qty)",\
                user_id = session["user_id"], stock_symbol = symbol, stock_name = name, stock_price = price, stock_qty = quantity
            )

            ##Update Users Table
            db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash = user_cash - total, user_id = session["user_id"])

            ##Need to add the alert that is bought!
            flash("Bought!")
            return redirect("/")

        else:
            return apology("Not enough $$$")

    ##return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    transaction_list = db.execute("SELECT stock_symbol, stock_qty, stock_price, timestamp FROM transactions WHERE user_id = :user_id",\
    user_id = session["user_id"])
    ##print(transaction_list)
    return render_template("history.html", transaction_list = transaction_list)



    ##return apology("TODO History PAge")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
        ##if len(rows) != 1 or rows[0]["hash"] != request.form.get("password"):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:

        ##get symbol and lookup on the API
        symbol = request.form.get("symbol")
        stockarr = lookup(symbol)

        ##hanlde if lookup return none
        if stockarr == None:
            return apology("Invalid Symbol of Stock")

        ##Need to update the page to disappear the form and only have a sentence
        ## "A share of NAME (STOCK SYMBOL) costs PRICE"
        quote = "A share of {} ({}) costs ${}.".format(stockarr["name"],stockarr["symbol"] , stockarr["price"])
        return render_template("quoted.html", quote = quote)

    ##return apology("TODO QUOTE PAGE")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",username=request.form.get("username"))

        # Ensure username does not exist
        if len(rows) != 0:
            return apology("username already exists", 403)

        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :password)", username=username, password=password)

        # Remember which user has logged in
        rows = db.execute("SELECT * FROM users WHERE username = :username",username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    ##return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        return render_template("sell.html")
    else:
         # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide valid symbol", 403)
        # Ensure quantity was submitted
        elif not request.form.get("quantity"):
            return apology("must provide valid number of shares", 403)


        ##get symbol and lookup on the API
        symbol = request.form.get("symbol")
        stockarr = lookup(symbol)

        ##hanlde if lookup return none
        if stockarr == None:
            return apology("Invalid Symbol of Stock")

        ##Check how much is the purchase
        quantity = float(request.form.get("quantity"))
        price = float(stockarr["price"])
        total = price * quantity
        name = stockarr["name"]

        ##Check if user has enough shares:
        tmpshares_list = db.execute("SELECT sum(stock_qty) as 'current_shares' FROM transactions WHERE user_id = :user_id AND stock_symbol= :stock_symbol",\
        user_id = session["user_id"], stock_symbol = symbol)
        current_shares = tmpshares_list[0]["current_shares"]
        ##print(tmpshares_list)
        ##print(current_shares)

        ##Fetch User Cash
        tmplist = db.execute("SELECT cash FROM users WHERE id = ?",session["user_id"])
        user_cash = tmplist[0]["cash"]

        if quantity <= current_shares:
            ##Insert Transactions into Tx table
            db.execute (
                "INSERT INTO transactions (user_id, stock_symbol, stock_name, stock_price, stock_qty)\
                VALUES(:user_id, :stock_symbol, :stock_name, :stock_price, :stock_qty)",\
                user_id = session["user_id"], stock_symbol = symbol, stock_name = name, stock_price = price, stock_qty = - quantity
            )


            ##Update Users Table
            db.execute("UPDATE users SET cash = :cash WHERE id = :user_id", cash = user_cash + total, user_id = session["user_id"])
            flash("Sold!")
            return redirect("/")
        else:
            return apology("You don't have that enough shares to sell")

    ##return apology("TODO SELL PAGe")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
