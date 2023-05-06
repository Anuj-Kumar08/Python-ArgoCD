from flask_pymongo import PyMongo
from flask import Flask, request
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)
app.secret_key = "mysecretkey"

with open("./conf.json", "r") as myfile:
    data = myfile.read()
    json_data = json.loads(data)


@app.route("/")
def wrapper():
    return """
        <body style="background-color: sky;">
            <script type="text/javascript">
            window.onload = function(){ 
                            alert("Welcome to the dashboard");
                            }
            </script>
            <form method="POST" action="/upload" class="inline" enctype="multipart/form-data">
                <p align="center"><button class=grey style="background-color:yellow;box-shadow: 0 0 5px 0;backdrop-filter:blur(10px);height:150px;width:700px"><h1><i>ArgoCD Demo<i></h1></button></a></p>
            </form>
        </body>
    """


@app.route("/upload", methods=["POST"])
def index():
    return """
        <body style="background-color:powderblue;">
                       <h1><i>Upload Your Files</i></h1>
                <i>Username</i> <input type="text" name="username" required>
                <input type="file" name="file_name" required>
                <input type="submit" value= Upload>
            </form>
        </body>    
    """


@app.route("/create", methods=["POST"])
def create():
    if "file_name" in request.files:
        file_name = request.files["file_name"]
        mongo.save_file(file_name.filename, file_name)
        mongo.db.users.insert_one(
            {
                "username": request.form.get("username"),
                "file_name_name": file_name.filename,
            }
        )
    return json.loads(data)
