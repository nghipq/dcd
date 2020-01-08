from server import db, ma
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(120))
    phonenumber = db.Column(db.String(20))
    address = db.Column(db.String(200))
    password = db.Column(db.String(20))
    date_register = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, username, email, phonenumber, address, password):
        self.username = username
        self.email = email
        self.phonenumber = phonenumber
        self.address = address
        self.password = password

#schema user
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'phonenumber', 'address', 'password')

userSchema = UserSchema()
usersSchema = UserSchema(many = True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sicknessId = db.Column(db.Integer)
    image_file = db.Column(db.String(20))
    lx = db.Column(db.Float)
    ly = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, sicknessId, image_file, lx, ly, user_id):
        self.sicknessId = sicknessId
        self.image_file = image_file
        self.lx = lx
        self.ly = ly
        self.user_id = user_id

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'sicknessId', 'image_file', 'lx', 'ly', 'user_id')

postSchema = PostSchema()
postsSchema = PostSchema(many = True)

class Sickness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(200))
    solution = db.Column(db.String(1000))

    def __init__(self, name, description, solution):
        self.name = name
        self.description = description
        self.solution = solution

#schema user
class SicknessSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'desciption', 'solution')

sicknessSchema = SicknessSchema()
sicknessesSchema = SicknessSchema(many = True)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(200))
    phonenumber = db.Column(db.String(20))

    def __init__(self, name, address, phonenumber):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber

#schema user
class DepartmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'phonenumber')

departmentSchema = DepartmentSchema()
departmentsSchema = DepartmentSchema(many = True)

