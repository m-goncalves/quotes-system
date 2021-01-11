from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_sqlalchemy import SQLAlchemy 
import os
from sqlalchemy import text 
from sqlalchemy import exc
import json

app = Flask(__name__)

user = os.environ.get("MYSQL_USER")
pwd = os.environ.get("MYSQL_PASSWORD")
host = os.environ.get("MYSQL_HOST")
port = os.environ.get("MYSQL_PORT")
database = os.environ.get("MYSQL_DATABASE")

url = "mysql+pymysql://%s:%s@%s:%s/%s" %(user, pwd, host, port, database)

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

@app.route('/version', methods=['GET'])
def version():
    return json.dumps({'version':'1'}), 200, {'ContentType':'application/json'}
@app.route('/healthz', methods=['GET'])
def healthz():
    try:
        db.engine.execute('SELECT 1')
        return json.dumps({'up':True}), 200, {'ContentType':'application/json'}
    except:
        return json.dumps({'up':False}), 500, {'ContentType':'application/json'}

@app.route('/api/v1/get-quote', methods=['GET'])
def get_quote():
    # Getting the number of quotes saved in the DB.
    length_query = text('SELECT COUNT(ID) FROM quotes')
    length_result = db.engine.execute(length_query)
    length = length_result.fetchone()[0]
    # Returning a random integer random_id where: 1 < random_id < length
    random_id = randint(1, int(length))
    # Selecting a random quote using a random quote id
    sql = text('SELECT quote FROM quotes WHERE ID=%s' % (random_id))
    result = db.engine.execute(sql)
    #Returning the quote
    random_quote = result.first()[0]
    return json.dumps({'random_quote':random_quote}), 200, {'ContentType':'application/json'}

@app.route('/api/v1/set-quote', methods=['POST'])
def set_quote():
    # Reading the POST JSON data using the key "quote"
    quote = request.json['quote']
    # Inserting the quote in the DB
    sql = text('INSERT INTO quotes (quote) VALUES ("%s");' % quote)
    # This will return a success message if the quote is inserted otherwise it will return a 500 server error
    try:
        result = db.engine.execute(sql)
    except exc.IntegrityError:
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

# The API will run on port 3000 on host 0.0.0.0.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)