import sqlalchemy

from sqlalchemy.orm import sessionmaker

from models import create_tables, Genre, Artist

DSN = 'postgresql://postgres:valentina1923@localhost:5432/MusicAppDB'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Service:

    def __init__(self, session):
        self.session = session

    def create_genre(self, name):
        genre = Genre(genre_name=name)
        session.add(genre)
        session.commit()
        return genre

    def create_artist(self, name):
        artist = Artist(artist_name=name)
        session.add(artist)
        session.commit()
        return artist




genre1 = Genre(genre_name='Hip-hop')
print(genre1.id)

session.add(genre1)
session.commit()

print(genre1.id)
print(genre1)
session.close()
