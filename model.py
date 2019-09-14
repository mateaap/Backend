from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4 as gid, UUID
import datetime as dt



db = Database()



db.bind(provider='sqlite', filename='baza.sqlite', create_db=True)


class Korisnik(db.Entity):
    id= PrimaryKey(str)
    Ime = Required(str)
    Prezime = Required(str)
    korisnicko_ime = Required(str)
    lozinka = Required(str)
    liste=Set("Lista_Zelja")




class Zanr(db.Entity):
    id = PrimaryKey(str)
    naziv= Required(str)
    knjige = Set("Knjiga")

class Knjiga(db.Entity):
    id = PrimaryKey(str)
    naziv= Required(str)
    autor= Required(str)
    opis= Required(str)
    zanr = Required(Zanr)
    lista = Set("Lista_Zelja")


class Lista_Zelja(db.Entity):
    id = PrimaryKey(str)
    korisnik= Required(Korisnik)
    knjige = Set(Knjiga)

db.generate_mapping(check_tables=True, create_tables=True)
