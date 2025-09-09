from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "this home page"

@app.route("/about")
def about():
    return "This is about page"
                                          #app routing
@app.route("/product")
def product():
    return "This is product page"

@app.route("/product/laptop")
def laptop():
    return "This is laptop detail page"

@app.route("/contact")
def contact():
    return "This is contact page"

if __name__=="__main__":

    app.run(debug=True)


