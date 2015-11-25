from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route('/hello/<name>', methods=['GET'])
def hello(name=None):
    return render_template("main.html",name=name)

@app.route('/calc', methods=['POST'])
def calc():
    adress = request.form["from"]
    print(adress)
    return render_template("main.html",name=adress)

if __name__ == "__main__":
    app.run()