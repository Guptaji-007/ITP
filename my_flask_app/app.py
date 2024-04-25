from flask import Flask, render_template, redirect, jsonify, request,url_for , session,request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
import pymysql

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
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY  # Required by Flask-WTF

# Define the form class
class ReservationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    table_number = IntegerField('Table Number', validators=[DataRequired(), NumberRange(min=1)])

# Form validation route
@app.route('/validate_form', methods=['POST'])
def form_validation():
    form = ReservationForm()

    if form.validate_on_submit():
        print("Form validation successful")
        # If form data is valid, redirect to home route
        return redirect(url_for('home'))
    else:
        print("Form validation failed:", form.errors)
        # If form data is invalid, render the form again with error messages
        return render_template('new.html', form=form)

# Render the form
@app.route('/')
def index():
    form = ReservationForm()
    return render_template('new.html', form=form)

@app.route('/submit', methods=['post'])
def submit():
    try:
    # Get user input from the form
        name = request.form['name']
        phone = request.form['phno']
        table = request.form['table']
        print("Name:", name)
        print("Phone Number:", phone)
        print("Table Number:", table)

        
        # Prepare SQL statement with user input
        sql = "INSERT INTO info (Name, PhoneNo, TableNo) VALUES (%s, %s,%s);"
        cursor.execute(sql, (name, phone,table))

        # Commit changes and close connection
        conn.commit()

        conn.close()
        return 'Data submitted successfully!'

    except Exception as e:
        return f'Error: {str(e)}'


total_items_food=0

@app.route('/update_total_items_food', methods=['GET'])
def update_total_items_food():
    global total_items_food
    total_items_food = int(request.args.get('total_items_food', 0))
    return 'Total items updated'  

@app.route('/home/atc')
def atc():
    global total_items_food
    if total_items_food != 0:
        return render_template('atc.html')
    else:
        # Redirect to another route or render a different template if no items in cart
        return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
