
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



#creating a Flask app

app = Flask(__name__)
app.debug = True

#adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


#Initializing SQLAlchemy with app
db = SQLAlchemy(app)


#Models
class Profile(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    

 # represent objects of the data table.
    def __repr__(self):
        return f"Name : {self.first_name}"






if __name__ == '__main__':
    app.run()
