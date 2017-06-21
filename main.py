from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True



form = """
<!DOCTYPE html>

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
        <form action="/rotate" method="post">
              <label for="rotate-factor">
                  Rotate by:
                  <input type="text" id="rotate-factor" name="rot" value='0'/>
              </label>
              <input type="textarea" id="textarea" name="text"/>
              <input type="submit" value="Submit Query"/>
          </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form


@app.route("/rotate")
def u():
    return

@app.route("/", methods=['POST'])
def encrypt(rot, text):
    rot = int(rot)
    text = text

    newtext = rotate_string(text, rot)

    return "<h1> + newtext + </h1>"

app.run()
