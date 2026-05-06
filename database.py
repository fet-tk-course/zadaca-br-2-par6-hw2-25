from sqlmodel import SQLModel, create_engine, Session

# Kreiranje SQLite baze podataka
# Datoteka baze će biti kreirana u root folderu projekta
DATABASE_URL = "sqlite:///./database.db"

# Kreiranje engine-a za komunikaciju sa bazom
# check_same_thread=False je potrebno za SQLite sa FastAPI
# echo=True ispisuje SQL upite u konzolu (korisno za debugging)
engine = create_engine(
    DATABASE_URL, 
    echo=True,
    connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    """
    Kreira sve tabele u bazi podataka na osnovu definisanih SQLModel klasa.
    Ova funkcija se poziva prilikom pokretanja aplikacije (startup event).
    """
    SQLModel.metadata.create_all(engine)


def get_session():
    """
    Generator funkcija koja kreira novu sesiju baze podataka.
    Koristi se kao dependency u FastAPI rutama.
    
    Yields:
        Session: SQLModel sesija za komunikaciju sa bazom
    """
    with Session(engine) as session:
        yield session