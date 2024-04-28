from flask import Flask, render_template, redirect, jsonify, request,url_for , session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
import pymysql
import os
import asyncio  
# Establish MySQL connection


timeout = 10
conn = pymysql.connect(
charset="utf8mb4",
connect_timeout=timeout,
cursorclass=pymysql.cursors.DictCursor,
db="WEBSITE",
host="mysql-14da71f7-devmittal9705-d8fc.d.aivencloud.com",
password="AVNS_M8EGsbDUEeMajooE7YC",
read_timeout=timeout,
port=22874,
user="avnadmin",
write_timeout=timeout,
)
cursor = conn.cursor()
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY  # Required by Flask-WTF

# Define the form class
class ReservationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    table_number = IntegerField('Table Number', validators=[DataRequired(), NumberRange(min=1)])
phone = ''
# Form validation route
@app.route('/validate_form', methods=['POST'])
def form_validation():
    global phone
    form = ReservationForm()

    if form.validate_on_submit():
        try:
            # Get user input from the form
            name = request.form['name']
            phone = request.form['phone_number']
            table = request.form['table_number']
            print("Name:", name)
            print("Phone Number:", phone)
            print("Table Number:", table)

            
            # Prepare SQL statement with user input
            sql = "INSERT INTO info (Name, PhoneNo, TableNo) VALUES (%s, %s,%s);"
            cursor.execute(sql, (name, phone,table))

            # Commit changes and close connection
            conn.commit()
            table_name=str(phone)
            cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}` (Item VARCHAR(225) NOT NULL,Quantity INT ,Price INT, PRIMARY KEY (Item));")

            return render_template("home.html")

        except Exception as e:
            return f'Error: {str(e)}'
    else:
        print("Form validation failed:", form.errors)
        # If form data is invalid, render the form again with error messages
        return render_template('new.html', form=form)

# Render the form
@app.route('/')
def index():
    form = ReservationForm()
    return render_template('new.html', form=form)

total_items_food=0

# @app.route('/update_total_items_food', methods=['GET'])
# def update_total_items_food():
#     global total_items_food
#     total_items_food = int(request.args.get('total_items_food', 0))
#     return 'Total items updated'  
data={}
@app.route('/process_data', methods=['POST'])
def process_data():
    global data
    try:
        
        # Retrieve JSON data from the request
        data = request.get_json()
        print('Received data from client:', data)

        # Process the received data as needed...

        return jsonify({'message': 'Data received successfully', 'data': data}), 200
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 500


@app.route('/validate_form/atc', methods=['POST'])
def atc():
    global data
    global phone
    if data!={}:
        try:
            # Print the updated item list
            for item_name, item_info in data.items():
                Item=item_name
                price=item_info['price']
                quantity=item_info['quantity']
                total = int(price) * int(quantity)  # Calculate total price
                item_info['total'] =str(total )  # Add total price to item_info dictionary

                # print(f"Item: {item_name}, Price: {item_info['price']}, Quantity: {item_info['quantity']}")
                # Execute SQL query to update quantity
                table_name=str(phone)
                update_query = f"INSERT INTO `{table_name}` (Item, Quantity,Price) VALUES (%s, %s, %s);"
                cursor.execute(update_query, (Item,quantity,price))

                # Commit changes
                conn.commit()
            return render_template("atc.html",data1=data)

        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        # Redirect to another route or render a different template if no items in cart
        return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)
