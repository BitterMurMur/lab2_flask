
from CompanyModule import *
from flask import Flask,  g


app = Flask(__name__)

def getCompany():
    if 'company' not in g:
        g.company = Company()
    return g.company

@app.route("/")
def companyindex():
    return getCompany().show()

@app.route("/showform/<id>")
def showform(id):
    return getCompany().showFormId(id)

@app.route("/delete/<id>")
def delete(id):
    return getCompany().delete(id)

@app.route("/add/", methods=['POST'])
def add():
    return getCompany().add()

@app.teardown_appcontext
def teardown(ctx):
    getCompany().storage.save()

if __name__ == "__main__":
    app.run(debug=True)