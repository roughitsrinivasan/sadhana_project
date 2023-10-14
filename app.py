from flask import Flask, render_template, request , redirect,url_for, session
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def start():
    return redirect(url_for('login'))
    # return render_template('start.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        pwd = request.form['pwd']
        print(user)
        print(pwd)
        if user=="sadhana" and pwd == "sadhana@123":
            session["name"] = user
            return redirect(url_for('home'))
        else:
            return render_template('not.html')
        
            
    return render_template('login.html')
    # else:
    #     user = request.args.get('nm')
    #     return redirect(url_for('home', name=user))

@app.route('/home')
def home():
    if not session.get("name"):
        return "Not a valid user"
    return render_template('home.html')

@app.route('/details1')
def details1():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('product-1.html')

@app.route('/details2')
def details2():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('product-2.html')

@app.route('/details3')
def details3():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('product-3.html')

@app.route('/details4')
def details4():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('product-4.html')

@app.route('/details5')
def details5():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('prod_detail5.html')

@app.route('/details6')
def details6():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('prod_detail6.html')

@app.route('/details7')
def details7():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('prod_detail7.html')

@app.route('/details8')
def details8():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('prod_detail8.html')


@app.route('/cart',methods=['POST','GET'])
def cart():
    if not session.get("name"):
        return "Not a valid user"
    
    return render_template('cart.html')

@app.route('/checkout')
def cash():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('checkout_new.html')


@app.route('/order',methods=['POST','GET'])
def order():
    if not session.get("name"):
        return "Not a valid user"
    
    if request.method=='POST':
        username=request.form['con_name']
        email=request.form['con_email']
        phnNo=request.form['con_phone']
        address=request.form['con_address']
        items=request.form['items']
        from datetime import date
        cur_date=date.today()
        from utils import index
        import random
        order_id= random.randint(100000,999999)
        check=index(email,username,cur_date,order_id,address,phnNo,items)
        print(check)
        return render_template('thankyou.html')

    return render_template('thankyou.html')

@app.route('/orders')
def orders():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('orders.html')


@app.route('/product')
def product():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('thankyou.html')

@app.route('/logout')
def logout():
    session.pop("name", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000,debug = True)