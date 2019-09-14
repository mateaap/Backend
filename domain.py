from model import  Korisnik,Knjiga,Zanr,Lista_Zelja
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID

class Korisnici:
    @db_session()
    def listaj():
        # ORM upit
        q = select(s for s in Korisnik)
        data = [x.to_dict() for x in q]
        return data,


    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            korisnik = Korisnik(**s)
            return True, korisnik.id
        except Exception as e:
            return False, str(e)

class Knjige:
    @db_session()
    def listaj():

        q = select(s for s in Knjiga)

        def zanrovi_knjiga(x):
            if "zanrovi" in x:
                x["zanrovi"] = [Zanr[z].to_dict() for z in x ["zanrovi"]]
            return x
        knjige=[zanrovi_knjiga(s.to_dict(with_collections=True)) for s in q]
        return knjige
    @db_session()
    def dodaj(s):
        try:
            s["id"] = str(gid())
            knjiga = Knjiga(**s)
            return True, knjiga.id
        except Exception as e:
            return False, str(e)

class Lista:
    @db_session()
    def listaj():
        q = select(s for s in Lista_Zelja)

        def zelje_sve(x):
            if "knjige" in x:
                x["knjige"] = [Knjiga[z].to_dict() for z in x ["knjige"]]
            return x
        knjige=[zelje_sve(s.to_dict(with_collections=True)) for s in q]
        return knjige

    @db_session()
    def dodaj(s):
        try:
            s["id"] = str(gid())
            if "knjige" in s:

                knjige_sve = s["knjige"]
                moja_lista = list(Knjiga[x] for x in knjige_sve)
                s["knjige"] = moja_lista
            lista_knjiga = Lista_Zelja(**s)
            return True, None
        except Exception as e:
            return False, str(e)

    @db_session
    def update(s):
        try:

            if "knjige" in s:
                sve_knjige = s["knjige"]
                lista_knjiga = list(Knjiga[x] for x in sve_knjige)
                s["knjige"] = lista_knjiga
                Lista_Zelja[s["id"]].set(**s)

            return True, None

        except Exception as e:
            return False,str(e)

class Zanrovi:
    @db_session()
    def listaj():
        q = select(s for s in Zanr)
        data = [x.to_dict() for x in q]
        return data,

    @db_session()
    def dodaj(s):
        try:
            s["id"] = str(gid())
            zanr = Zanr(**s)
            return True, zanr.id
        except Exception as e:

            return False, str(e)
