from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template("home.html")

if __name__ == "__main__":
    print("Server is initialized")
    app.run(debug=True )
