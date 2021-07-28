from flask import Flask
from flask import request, render_template
import os
from dotenv import load_dotenv


import mysql.connector
load_dotenv()
db = mysql.connector.connect(
  host=os.getenv('DB_HOST'),
  user=os.getenv('DB_USER'),
  password=os.getenv('DB_PASS'),
  database=os.getenv('DB_NAME')
)

cursor = db.cursor()
# hack_str = '\' OR 1=1 -- '
# passwd='hack'
# cursor.execute("SELECT * FROM userdata WHERE username = '%s' and password = '%s';" % (hack_str, passwd) )
# # cursor.execute("SELECT * FROM userdata WHERE username = '' or 1=1 -- and password=mark ")
# record = cursor.fetchone()
# print(f"record: {record}")
# db.close()


app = Flask(__name__)
 
@app.route('/login', methods=['POST', 'GET'])
def login():
  error =''

  if request.method == 'POST':
    username = request.form['username']
    passwd = request.form['password']
    print("username", username)
    print("password", passwd)

    # check username and passwd in DB
    # hackstr = "' OR 1=1 -- "
    cursor.execute("SELECT * FROM userdata WHERE username = '%s' and password = '%s';" % (username, passwd) )

    record = cursor.fetchone()
    print("record", record)
    if record is not None:
      print(f"record: {record} {type(record)}")
      return render_template('user.html', username=record[0])
    else:
      error = 'Invalid username or password'
  return render_template('login.html', error=error) 

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)