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
# cur.execute("CREATE TABLE info( Name varchar(225) , PhoneNo int, TableNo int NOT NULL, PRIMARY KEY(PhoneNo))")
# cur.execute("DELETE FROM info;")
# cur.execute("INSERT INTO info (Name, PhoneNo, TableNo) VALUES ('DEV',9,69);")
# connection.commit()
cur.execute("Select * from info;")
print(cur.fetchall())
connection.close()