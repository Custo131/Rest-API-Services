from flask_sqlalchemy import SQLAlchemy
# Creating SQL instance
db = SQLAlchemy()


#Models

class Profile(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)

    #represent obbjects of the database
    def __rep__(self):
        return  f"Name : {self.first_name}"
    


