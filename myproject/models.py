from myproject import db



class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __str__(self):
        if self.owner:
            return f"Puppy Name is {self.name}, Owner Name is {self.owner.name}"
        return f"Puppy Name: {self.name} and no owner assigned yet!"
    

class Owner(db.Model):


    __tablename__ = 'owner'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable=False)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"
    