from flask import Flask, render_template
from caesar import rotate_string
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True


form = """<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
        <form method="POST">
        Rotate by: 
        <input type = "text" name = "rotate">
        <br>
        <input type = "text" name = "body" style ="width:500px; height:90px;">
        <br>
        <input type = "button" name="submit" value="Submit" >
        </form>
        </body>
    </html>"""



@app.route("/")
def index():
    return form

@app.route("/", methods = ['Post'])
def encrypt():
    return form


app.run()