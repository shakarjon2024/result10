from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result10():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")

        return render_template("result10.html", name=name, email=email, age=age)


    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
