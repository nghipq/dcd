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

class Store(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(20))
    address = db.Column(db.String(200))
    lx = db.Column(db.Float)
    ly = db.Column(db.Float)
    phonenumber = db.Column(db.String(15))
    email = db.Column(db.String(50))
    date_register = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, name, password, address, lx, ly, phonenumber, email):
        self.name = name
        self.password = password
        self.address = address
        self.phonenumber = phonenumber
        self.lx = lx
        self.ly = ly
        self.email = email

#schema store
class StoreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'password', 'phonenumber', 'address', 'email')

storeSchema = StoreSchema()
storesSchema = StoreSchema(many = True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(500))
    price = db.Column(db.String(10))
    quantity = db.Column(db.Integer)
    store = db.Column(db.Integer, db.ForeignKey("store.id"))
    images = db.Column(db.String(10))
    types = db.Column(db.String(20))
    brand = db.Column(db.String(50))
    date_update = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __init__(self, name, desciption, price, quantity, store, images, types, brand):
        self.name = name
        self.description = desciption
        self.price = price
        self.quantity = quantity
        self.store = store
        self.images = images
        self.types = types
        self.brand = brand

#schema product
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity', 'store', 'images', 'types', 'brand')

productSchema = ProductSchema()
productsSchema = ProductSchema(many = True)

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"))
    storeId = db.Column(db.Integer, db.ForeignKey("store.id"))
    products = db.Column(db.String(500))
    totalPrice = db.Column(db.String(10))
    lx = db.Column(db.Float)
    ly = db.Column(db.Float)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(15))
    isCheck = db.Column(db.Integer, default = 0)
    date_register = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, userId, storeId, products, totalPrice, lx, ly, address, phone):
        self.userId = userId
        self.storeId = storeId
        self.products = products
        self.totalPrice = totalPrice
        self.lx = lx
        self.ly = ly
        self.address = address
        self.phone = phone

#schema bill
class BillSchema(ma.Schema):
    class Meta:
        fields = ('id', 'userId', 'storeId','products', 'totalPrice', 'lx', 'ly', 'address', 'phone', 'isCheck', 'date_register')

billSchema = BillSchema()
billsSchema = BillSchema(many = True)