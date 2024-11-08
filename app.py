from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schema1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = 'Customers'
    CUSTOMER_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Menu(db.Model):
    __tablename__ = 'MENU'
    menu_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.String(100), nullable=False)
    item_description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(60), nullable=True)
    item_price = db.Column(db.Float, nullable=False)
    item_calories = db.Column(db.Integer, nullable=True)
    is_it_available = db.Column(db.Boolean, nullable=True)

class Order(db.Model):
    __tablename__ = 'ORDERS'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CUSTOMER_ID = db.Column(db.Integer, db.ForeignKey('Customers.CUSTOMER_ID'))
    order_date = db.Column(db.DateTime)
    status = db.Column(db.String(60))
    total_amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(60))



class OrderItem(db.Model):
    __tablename__ = 'OrderItems'
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('ORDERS.order_id'))
    menu_item_id = db.Column(db.Integer, db.ForeignKey('MENU.menu_item_id'))
    price = db.Column(db.Float, nullable=False)


class Payment(db.Model):
    __tablename__ = 'PAYMENTS'
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('ORDERS.order_id'))
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(60))
    payment_status = db.Column(db.String(20), default='pending')
    payment_date = db.Column(db.DateTime)


class MenuModify(db.Model):
    __tablename__ = 'MENUMODIFY'
    modify_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('MENU.menu_item_id'))
    modifieditem_name = db.Column(db.String(100))
    modified_price = db.Column(db.Float, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']

        customer_add = Customer(
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
            email = email
        )
        try:
            db.session.add(customer_add)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There is an issue with the data input: {e}"





@app.route('/orders', methods=['POST'])
def orders():
    if request.method == 'POST':
        CUSTOMER_ID = request.form['CUSTOMER_ID']
        status = request.form['status']
        total_amount = request.form['total_amount']
        payment_method = request.form['payment_method']

        order_info = ORDERS(
            CUSTOMER_ID = CUSTOMER_ID,
            status = status,
            total_amount = total_amount,
            payment_method = payment_method
        )
        try:
            db.session.add(order_info)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There is an issue with the data input: {e}"




@app.route('/order_items', methods=['POST'])
def order_items():
    if request.method == 'POST':
        order_id = request.form['order_id']
        menu_item_id = request.form['menu_item_id']
        price = request.form['price']

        order_item_info = OrderItems(
            order_id = order_id,
            menu_item_id = menu_item_id,
            price = price
        )
        try:
            db.session.add(order_item_info)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There is an issue with the data input: {e}"



@app.route('/menu', methods=['POST'])
def menu():
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_description = request.form['item_description']
        category = request.form['category']
        item_price = request.form['item_price']
        item_calories = request.form['item_calories']
        is_it_available = request.form['is_it_available']

        menu_info = MENU(
            item_name = item_name,
            item_description = item_description,
            category = category,
            item_price = item_price,
            item_calories = item_calories,
            is_it_available = is_it_available
        )
        try:
            db.session.add(menu_info)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There is an issue with the data input: {e}"



@app.route('/payments', methods=['POST'])
def payments():
    if request.method == 'POST':
        order_id = request.form['order_id']
        amount = request.form['amount']
        payment_method = request.form['payment_method']
        payment_status = request.form['payment_status']
    
        paymnets_information = PAYMENTS(
            order_id = order_id,
            amount = amount,
            payment_method = payment_method,
            payment_status = payment_status
        )
        try:
            db.session.add(paymnets_information)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There is an issue with the data input: {e}"


@app.route('/menu_modify', methods=['POST'])
def menu_modify():
    if request.method == 'POST':
        menu_item_id = request.form['menu_item_id']
        modifieditem_name = request.form['modifieditem_name']
        modified_price = request.form['modified_price']

        menu_modification = MENUMODIFY(
            menu_item_id = menu_item_id,
            modifieditem_name = modifieditem_name,
            modified_price = modified_price
        )
        try:
            db.session.add(menu_modification)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"There is an issue with the data input: {e}"

#############################
#Testing all db
@app.route('/test_all_db', methods=['GET'])
def test_all_db():
    try:
        # 1. Insert into Customers table
        new_customer = Customer(
            first_name="John",
            last_name="Doe",
            phone_number="123456789",
            email="john.doe@example.com"
        )
        db.session.add(new_customer)
        db.session.commit()

        # Verify Customer Insert
        customer = Customer.query.first()
        customer_result = f"Customer added: {customer.first_name} {customer.last_name}<br>"

        # 2. Insert into MENU table
        new_menu_item = Menu(
            item_name="Pizza",
            item_description="Delicious cheese pizza",
            category="Main Course",
            item_price=9.99,
            item_calories=800,
            is_it_available=True
        )
        db.session.add(new_menu_item)
        db.session.commit()

        # Verify Menu Insert
        menu_item = Menu.query.first()
        menu_result = f"Menu item added: {menu_item.item_name} - {menu_item.item_description}<br>"

        # 3. Insert into ORDERS table (linked to customer)
        new_order = Order(
            CUSTOMER_ID=customer.CUSTOMER_ID,  # Link order to the first customer
            status="Processing",
            total_amount=9.99,
            payment_method="Credit Card"
        )
        db.session.add(new_order)
        db.session.commit()

        # Verify Order Insert
        order = Order.query.first()
        order_result = f"Order added for customer: {order.CUSTOMER_ID} - Status: {order.status}<br>"

        # 4. Insert into OrderItems table (linked to order and menu)
        new_order_item = OrderItem(
            order_id=order.order_id,  # Link to the first order
            menu_item_id=menu_item.menu_item_id,  # Link to the first menu item
            price=9.99
        )
        db.session.add(new_order_item)
        db.session.commit()

        # Verify OrderItem Insert
        order_item = OrderItem.query.first()
        order_item_result = f"Order item added: {order_item.order_id} - Price: {order_item.price}<br>"

        # 5. Insert into PAYMENTS table (linked to order)
        new_payment = Payment(
            order_id=order.order_id,  # Link to the first order
            amount=9.99,
            payment_method="Credit Card",
            payment_status="Completed"
        )
        db.session.add(new_payment)
        db.session.commit()

        # Verify Payment Insert
        payment = Payment.query.first()
        payment_result = f"Payment added: {payment.amount} - Status: {payment.payment_status}<br>"

        # 6. Insert into MENUMODIFY table (linked to menu item)
        new_menu_modification = MenuModify(
            menu_item_id=menu_item.menu_item_id,  # Link to the first menu item
            modifieditem_name="Pizza with Extra Cheese",
            modified_price=11.99
        )
        db.session.add(new_menu_modification)
        db.session.commit()

        # Verify MenuModify Insert
        menu_modify = MenuModify.query.first()
        menu_modify_result = f"Menu modification added: {menu_modify.modifieditem_name} - Price: {menu_modify.modified_price}<br>"

        # Return results for all table inserts and queries
        return (customer_result + menu_result + order_result +
                order_item_result + payment_result + menu_modify_result)

    except Exception as e:
        return f"An error occurred: {e}"






if __name__ == '__main__':
    app.run(debug=True, port=6006)