from server import app, db
import os
import markdown
from flask import request, jsonify, render_template, send_file
from server.models import User, Post, Sickness, Store, Product, Bill, postsSchema, productsSchema, billsSchema,Department
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import cv2
import tensorflow as tf
import h5py
from server.unity import *

# load model
datamodel = h5py.File("E:\\fbiz\\api\chicken.h5", "r")
model = tf.keras.models.load_model(datamodel)
checkChicken = tf.keras.applications.resnet50.ResNet50(weights='imagenet')


def load_image(img_path, size, show=False):

    img = image.load_img(img_path, target_size=(size, size))
    img_tensor = image.img_to_array(img)
    # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    # imshow expects values in the range [0, 1]
    img_tensor /= 255.

    return img_tensor

##API
# home
@app.route("/", methods=["GET"])
def home():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/Document.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

# load image
@app.route("/images", methods=["GET"])
def send_images():
    image_name = get_queries(request)["image"]
    return send_file(f"./images/product/{image_name}", mimetype='image/gif')

# user register
@app.route("/user/auth/register", methods=["POST"])
def register():
    data = request.json
    try:
        username = data.get("username")
        email = data.get("email")
        phonenumber = data.get("phonenumber")
        try:
            existUsername = User.query.filter_by(username=username).first()
            if existUsername:
                return jsonify(
                    success=False,
                    error="This username is alrealy exist"
                )

            existEmail = User.query.filter_by(email=email).first()
            if existEmail:
                return jsonify(
                    success=False,
                    error="This email is alrealy exist"
                )

            existPhonenumber = User.query.filter_by(username=username).first()
            if existPhonenumber:
                return jsonify(
                    success=False,
                    error="This phonenumber is alrealy exist"
                )
        except:
            pass

        address = data.get("address")

        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            return jsonify(
                success=False,
                error="password not match"
            )

        newUser = User(username, email, phonenumber, address, password)
        try:
            db.session.add(newUser)
            db.session.commit()

            return jsonify(
                success=True,
            )
        except:
            return jsonify(
                success=False,
                error="cannot register"
            )

    except:
        return jsonify(
            success=False,
            error="cannot register"
        )

# user login
@app.route("/user/auth/login", methods=["POST"])
def login():
    email = request.json.get("email")
    dataEmail = User.query.filter_by(email=email).first()
    if dataEmail:
        password = request.json.get("password")
        if password == dataEmail.password:
            return jsonify(
                success=True,
                username=dataEmail.username,
                id=dataEmail.id
            )
        else:
            return jsonify(
                success=False,
                error="password is not correct"
            )
    else:
        return jsonify(
            success=False,
            error="This email does not exist"
        )

# store register
@app.route("/store/auth/register", methods=["POST"])
def store_register():
    data = request.json
    print(data)
    try:
        name = data.get("name")
        email = data.get("email")
        phonenumber = data.get("phonenumber")
        try:
            existName = Store.query.filter_by(name=name).first()
            if existName:
                return jsonify(
                    success=False,
                    error="This name is alrealy exist"
                )

            existEmail = Store.query.filter_by(email=email).first()
            if existEmail:
                return jsonify(
                    success=False,
                    error="This email is alrealy exist"
                )

            existPhonenumber = User.query.filter_by(username=username).first()
            if existPhonenumber:
                return jsonify(
                    success=False,
                    error="This phonenumber is alrealy exist"
                )
        except:
            pass

        address = data.get("address")
        lx = data.get("lx")
        ly = data.get("ly")

        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            return jsonify(
                success=False,
                error="password not match"
            )

        newStore = Store(name, password, address, lx, ly, phonenumber, email)
        try:
            db.session.add(newStore)
            db.session.commit()

            return jsonify(
                success=True,
            )
        except:
            return jsonify(
                success=False,
                error="cannot register"
            )

    except:
        return jsonify(
            success=False,
            error="cannot register"
        )

# store login
@app.route("/store/auth/login", methods=["POST"])
def storeLogin():
    data = request.json
    email = data.get("email")
    dataEmail = Store.query.filter_by(email=email).first()
    if dataEmail:
        password = data.get("password")
        if password == dataEmail.password:
            return jsonify(
                success=True,
                username=dataEmail.name,
                id=dataEmail.id
            )
        else:
            return jsonify(
                success=False,
                error="password is not correct"
            )
    else:
        return jsonify(
            success=False,
            error="This email does not exist"
        )

# insert product
@app.route("/store/product/create", methods=["POST"])
def create_product():
    data = request.json
    try:
        name = data.get("name")
        store = data.get("storeId")
        brand = data.get("brand")
        productExist = Product.query.filter_by(name=name, store=store, brand=brand).first()

        if productExist:
            return jsonify(
                success=False,
                error="This product is alrealy exist"
            )
        else:
            description = data.get("description")
            price = data.get("price")
            quantity = data.get("quantity")
            types = data.get("types")

            try:
                imagesName = f"{len(os.listdir('./images/products'))}.jpg"
                imagesFile = request.files["photo"]
                imagesFile.save(f"./images/products/{imagesName}")
            except:
                imagesName = "default.jpg"
               
            newProduct = Product(name, description, price, quantity, store, imagesName, types, brand)

            try:
                db.session.add(newProduct)
                db.session.commit()

                return jsonify(
                    success=True,
                )
            
            except:
                return jsonify(
                    success=False,
                    error="cannot create this product"
                )
    except:
        return jsonify(
            success=False,
            error="cannot create this product"
        )


# delete product
@app.route("/store/product/delete", methods = ["GET"])
def delete_product():
    productId = get_queries(request)["id"]

    try:
        product = Product.query.filter_by(id = productId)
        if not product:
            return jsonify(
                        success = False,
                        error = "Cannot find this product"
                    )
        product.delete()
        db.session.commit()

        return jsonify(
            success = True
        )
    except:
        return jsonify(
            success = False,
            error = "Cannot delete this product"
        )

# update product
@app.route("/store/product/update", methods = ["POST"])
def update_product():
    data = request.json
    try:
        id = data.get("id")
        product = Product.query.filter_by(id = id).first()
        if product:
            name = data.get("name")
            description = data.get("description")
            price = data.get("price")
            quantity = data.get("quantity")
            
            try:
                product.name = name
                product.description = description
                product.price = price
                product.quantity = quantity
                db.session.commit()

                return jsonify(
                    success = True
                )
            except:
                return jsonify(
                    success = False,
                    error = "Cannot update this product"
                )
        else:
            return jsonify(
                success = False,
                error = "Product not found"
            ) 
    except:
        return jsonify(
            success = False,
            error = "Cannot update this product!"
        )    

# get product
@app.route("/user/product/getProducts", methods = ["GET"])
def getAll_product():
    queries = get_queries(request)
    products = Product.query.all()
    all_products = format_products_list(filter_arr_by_queries(productsSchema.dump(products), queries))
    
    if len(all_products) == 0:
        return jsonify(
            message = "don't have any products!"
        )
    else:
        return jsonify(all_products)

# create bill
@app.route("/store/bill/create", methods = ["POST"])
def create_bill():
    data = request.json
    userId = data.get("userId")
    address = data.get("address")
    lx = data.get("lx")
    ly = data.get("ly")
    phone = data.get("phone")
    products = data.get("products")
    products = products.split(",")
    numberStoreProduct = dict()

    for product in products:
        storeId = Product.query.filter_by(id = int(product[0])).first().store
        numberStoreProduct[storeId] = numberStoreProduct.get(storeId, list()) + [product]

    for store, items in numberStoreProduct.items():
        storeId = int(store)
        totalPrice = 0
        for item in items:
            pId = int(item[0])
            quantity = int(item[2:])
            p = Product.query.filter_by(id = pId).first()
            price = float(p.price)

            totalPrice += price * quantity
        try:
            newBill = Bill(userId, storeId, ",".join(items), str(totalPrice), lx, ly, address, phone)
            db.session.add(newBill)
            db.session.commit()

        except:
            return jsonify(
                success = False,
                error = "cannot create bill"
            )
    return jsonify(
                success = True
            )

# get bill
@app.route("/store/bill/getBills", methods = ["GET"])
def get_all_bill():
    queries = get_queries(request)
    try:
        all_bill = format_bills_list(filter_arr_by_queries(billsSchema.dump(Bill.query.all()), queries))       
        return jsonify(all_bill)

    except:
        return jsonify(
            success = False,
            error = "cannot show bill list"
        )

# update bill by id
@app.route("/store/bill/update", methods = ["POST"])
def update_bill():
    data = request.json
    try:
        bill = Bill.query.filter_by(id = data.get("id")).first()
        bill.isCheck = data.get("check")
        db.session.commit()

        return jsonify(
            success = True
        )
    except:
        return jsonify(
            success = False,
            error = "cannot updata"
        )

# location
@app.route("/location", methods=["GET"])
def location():
    posts = Post.query.all()
    all_post = postsSchema.dump(posts)
    res = []

    for post in all_post:
        feature = {"sicknessId": str(post["sicknessId"]), "cotinate": [
            post["lx"], post["ly"]]}
        res.append(feature)

    return jsonify(res)

# diaglogic
@app.route("/diaglogic", methods=["POST"])
def diaglogic():
    chickenList = ["cock", "hen", "chicken", "bird", "quail", "partridge", "pillow"]

    isCorrect = True
    # load a single image
    name = f'{len(Post.query.all())+1}.jpg'
    photo = request.files["photo"]
    photo.save(f'E:/fbiz/api/server/images/data/{name}')
    
    img = image.load_img(f'E:/fbiz/api/server/images/data/{name}', target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

        # check prediction
    predRs = checkChicken.predict(x)
    predCheck = decode_predictions(predRs, top=3)[0]
    print(predCheck)
    check = False
    for i in predCheck:
        if i[1] in chickenList: 
            check = True
            break


    if check == False:
        res = {"success": False, "mgs": "Vui lòng chụp ảnh rõ hơn hoặc gần đối tượng để có được kết quả chính xác. Xin cám ơn!"}
        return jsonify(res)

    new_image = load_image(f'E:/fbiz/api/server/images/data/{name}', 64)

    # check prediction
    pred = model.predict(new_image)
    print("Thong so cac benh:", pred)
    rs = max(pred[0])
    if rs < 90:
        isCorrect = False
    pred = pred[0]
    pred = pred.tolist()
    idx = pred.index(rs)
    print("Ket qua tra ve:", idx)
    result = Sickness.query.filter_by(id=(idx + 1)).first()

    newPost = Post(int(idx+1), name, float(request.values["lng"]), float(
        request.values["lat"]), int(request.values["userId"]))

    userAddress = User.query.filter_by(
        id=int(request.values["userId"])).first().address

    department = Department.query.filter_by(name=userAddress).first()

    try:

        db.session.add(newPost)
        db.session.commit()

    except:
        return jsonify(
            success=False,
            error="cannot post"
        )

    res = {"success": True, "sickness": result.name, "description": result.description,
           "solution": result.solution, "isCorrect": isCorrect, "Department": department.phonenumber}

    return jsonify(res)

# sickness
@app.route("/sickness", methods=["POST"])
def sickness():
    newSickness = Sickness(
        request.values["name"], request.values["description"], request.values["solution"])
    
    db.session.add(newSickness)
    db.session.commit()

    return "success"

# department
@app.route("/department", methods=["POST"])
def department():
    newDepartment = Department(
        request.values["name"], request.values["address"], request.values["phonenumber"])
    
    db.session.add(newDepartment)
    db.session.commit()

    return "success"

##WEB SERVER
# home
@app.route("/web/")
def home_page():
    return render_template("index.html")

# user
@app.route("/web/user")
def user_page():
    return render_template("user.html")

#map
@app.route("/web/maps")
def maps_page():
    return render_template("map.html")

#chat
@app.route("/web/chat")
def chat_page():
    return render_template("chat.html")