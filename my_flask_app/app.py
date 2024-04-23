from flask import Flask, render_template, jsonify, request,url_for
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



@app.route('/')
def index():
    return render_template('new.html')



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



@app.route('/home/atc')
def atc():
    return render_template('atc.html')


if __name__ == '__main__':
    app.run(debug=True)
