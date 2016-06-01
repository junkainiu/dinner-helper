from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def handle_entry():
    return render_template("index.html")


@app.route("/lihua")
def handle_lihua():
    return 'hello lihua'


@app.route("/zkf")
def handle_zkf():
    return "hello zkf"

if __name__ == "__main__":
    app.run()
