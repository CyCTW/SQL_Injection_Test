from flask import Flask
from flask import request, render_template
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
db.init_app(app)

@app.route('/login', methods=['POST', 'GET'])
def login():
  error =''
  try:
    if request.method == 'POST':
      username = request.form['username']
      passwd = request.form['password']

      # check username and passwd in DB
      record = db.engine.execute("SELECT * FROM userdata WHERE username = '%s' and password = '%s';"\
         % (username, passwd)).fetchone()

      print("record", record)
      if record is not None:
        return render_template('user.html', username=record.username)
      else:
        error = 'Invalid username or password'
    return render_template('login.html', error=error) 
  except pymysqlpe as e:
    print(e)
    app.logger.info(str(e))
    return "Database error", 400

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=80)