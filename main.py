from flask import Flask, render_template
from caesar import rotate_string
from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True


form = """<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
        <form method="POST" action ="/encrypt">
        Rotate by: 
        <input type = "text" name = "rotate">

        <br>
        <textarea name = "flipped" ">{0}</textarea>
        <br>
        <input type = "submit" name="submit" value="Submit">
        </form>
        </body>
    </html>"""



@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt", methods = ['Post'])
def encrypt():
    display = rotate_string(request.form["flipped"], int(request.form["rotate"]))
    return form.format(display)


app.run()