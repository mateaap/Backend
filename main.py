
from flask import Flask, Response, jsonify, request
from domain import Korisnici,Knjige,Lista,Zanrovi
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/korisnici', methods=['GET','POST'])
def main_korisnici():
    if request.method == 'GET':
        korisnici = Korisnici.listaj()
        return jsonify({"korisnici": korisnici })
    elif request.method == 'POST':
        status, greske = Korisnici.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

@app.route('/zanrovi', methods=['GET','POST'])
def main_zanrovi():
    if request.method == 'GET':
        zanrovi = Zanrovi.listaj()
        return jsonify({"zanrovi": zanrovi})
    elif request.method == 'POST':
        status, greske = Zanrovi.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

@app.route('/knjige', methods=['GET','POST'])
def main_knjige():
    if request.method == 'GET':
        knjige = Knjige.listaj()
        return jsonify({"knjige": knjige})
    elif request.method == 'POST':
        status, greske = Knjige.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

@app.route('/lista', methods=['GET', 'PUT','POST'])
def main_lista():
    if request.method == 'GET':
        lista = Lista.listaj()
        return jsonify({"lista": lista})
    elif request.method == 'POST':
        status, greske = Lista.dodaj(request.get_json())
    elif request.method == 'PUT':
        status, greske = Lista.update(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

if __name__ == '__main__':
    app.debug = True
    app.run()