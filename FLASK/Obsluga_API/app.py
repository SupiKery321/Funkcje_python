import requests

from flask import app, render_template, request, Flask
app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
dane = response.json()


rates = dane[0]["rates"]

kurs_wybranej_waluty = 0
 

@ app.route("/", methods = ["GET", "POST"])
def main():
    return render_template("api.html")

@ app.route("/wybierz", methods = ["GET", "POST"])
def wybierz():
    
    if request.method == "POST":
        currency = request.form.get("operation")
        rates = dane[0]["rates"]
        for a in rates:
            print(a)
            kurs_wybranej_waluty = a["bid"]
            if currency== a["currency"]:
                print(a["code"], a["bid"])
                return render_template("api.html", code = a["code"], bid = a["bid"])
        return render_template("api.html")

@ app.route("/wybierz/przelicz", methods = ["GET", "POST"])
def przelicz():
    if request.method == "POST":
        liczenie = request.form.get("counting")
        koooperacja = (kurs_wybranej_waluty * liczenie)
        print(koooperacja)
        return render_template("api.html", operacja = koooperacja)
    return render_template("api.html")



