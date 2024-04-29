import pymysql

timeout = 10
connection = pymysql.connect(
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

cur = connection.cursor()
# cur.execute("CREATE TABLE Aditya( Name varchar(255) , PhoneNo varchar(10), TableNo int NOT NULL,Item VARCHAR(225) NOT NULL,Quantity INT ,Price INT,Total INT )")
# cur.execute("DELETE FROM info;")
# cur.execute("DROP TABLE  Aditya;")
# cur.execute("INSERT INTO info (Name, PhoneNo, TableNo) VALUES ('DEV',9,69);")
# connection.commit()
cur.execute("Select * from Aditya;")
print(cur.fetchall())
connection.close()