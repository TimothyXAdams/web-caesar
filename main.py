from flask import flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/rotate",methods=['POST'])

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
                  <input type="text" id="rotate-factor" name="rotate-factor"/>
              </label>
              <input type="submit" value="Submit Query"/>
          </form>
    </body>
</html>
"""
def index():


app.run()
