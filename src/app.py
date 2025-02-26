from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#creating a Flask app

app = Flask(__name__)
app.debug = True

#adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


#Creating and SQLAchemy instance
db = SQLAlchemy(app)





if __name__ == '__main__':
    app.run()
