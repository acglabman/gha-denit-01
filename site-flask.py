from flask import Flask, render_template


application = Flask(__name__)


@application.route("/about-site")
def index():
    return "Hello site-flask.py v1.0"


@application.route("/")
def root():
    return render_template("index.html")


@application.route("/man")
def helppage():
    return render_template("man.html")

#--------Main------------------
if __name__ == "__main__":
    application.debug = True
    application.run()
#------------------------------