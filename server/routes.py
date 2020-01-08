from server import app, db
import os
import markdown
from flask import request, jsonify, render_template
from server.models import User, Post, Sickness, postsSchema, Department
from keras.preprocessing import image
import numpy as np
import os
import tensorflow as tf
import h5py

# load model
datamodel = h5py.File("E:\\fbiz\\api\chicken.h5", "r")
model = tf.keras.models.load_model(datamodel)


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(64, 64))
    # (height, width, channels)
    img_tensor = image.img_to_array(img)
    # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    # imshow expects values in the range [0, 1]
    img_tensor /= 255.

    return img_tensor

# home
@app.route("/", methods=["GET"])
def home():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

# register
@app.route("/register", methods=["POST"])
def register():
    data = request.values
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

# login
@app.route("/login", methods=["POST"])
def login():
    email = request.values.get("email")
    dataEmail = User.query.filter_by(email=email).first()
    if dataEmail:
        password = request.values.get("password")
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

# location
@app.route("/location", methods=["GET"])
def location():
    posts = Post.query.all()
    all_post = postsSchema.dump(posts)
    res = []

    for post in all_post:
        feature = {"sicknessId": str(post["id"]), "cotinate": [
            post["lx"], post["ly"]]}
        res.append(feature)

    return jsonify(res)

# diaglogic
@app.route("/diaglogic", methods=["POST"])
def diaglogic():
    isCorrect = True
    # load a single image
    name = f'{len(Post.query.all())+1}.jpg'
    photo = request.files["photo"]
    photo.save(f'E:/fbiz/api/server/images/{name}')

    new_image = load_image(f'E:/fbiz/api/server/images/{name}')

    # check prediction
    pred = model.predict(new_image)

    rs = max(pred[0])
    if rs < 90:
        isCorrect = False
    pred = pred[0]
    pred = pred.tolist()
    idx = pred.index(rs)

    result = Sickness.query.filter_by(id=idx + 1).first()

    newPost = Post(int(idx+1), name, float(request.values["lng"]), float(
        request.values["lat"]), int(request.values["userId"]))

    userAddress = User.query.filter_by(
        id=int(request.values["userId"])).first().address

    print(userAddress)

    try:

        db.session.add(newPost)
        db.session.commit()

    except:
        return jsonify(
            success=False,
            error="cannot post"
        )

    res = {"sickness": result.name, "description": result.description,
           "solution": result.solution, "isCorrect": isCorrect}

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

# map
@app.route("/maps")
def maps():
    return render_template("index.html")