import sqlalchemy as sq

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

DSN = 'postgresql://postgres:valentina1923@localhost:5432/MusicAppDB'
engine = sq.create_engine(DSN)

class Genre(Base):
    __tablename__ = 'genre'
    id = sq.Column(sq.Integer, primary_key=True)
    genre_name = sq.Column(sq.String(length=64), nullable=False)

class Artist(Base):
    __tablename__ = 'artist'
    id = sq.Column(sq.Integer, primary_key=True)
    artist_name = sq.Column(sq.String(length=64), nullable=False)

class Genre_Artist(Base):
    __tablename__ = 'genre_artist'
    id = sq.Column(sq.Integer, primary_key=True)
    genre_id = sq.Column(sq.Integer, sq.ForeignKey('genre.id'), nullable=False)
    artist_id = sq.Column(sq.Integer, sq.ForeignKey('artist.id'), nullable=False)

    genre = relationship(Genre, backref='genre_artist')
    artist = relationship(Artist, backref='genre_artist')

class Album(Base):
    __tablename__ = 'album'
    id = sq.Column(sq.Integer, primary_key=True)
    album_title = sq.Column(sq.String(length=64), nullable=False)
    album_release_year = sq.Column(sq.Integer, nullable=False)

class Artist_Album(Base):
    __tablename__ = 'artist_album'
    id = sq.Column(sq.Integer, primary_key=True)
    artist_id = sq.Column(sq.Integer, sq.ForeignKey('artist.id'), nullable=False)
    album_id = sq.Column(sq.Integer, sq.ForeignKey('album.id'), nullable=False)

    artist = relationship(Artist, backref='artist_album')
    album = relationship(Album, backref='artist_album')

class Song(Base):
    __tablename__ = 'song'
    id = sq.Column(sq.Integer, primary_key=True)
    song_name = sq.Column(sq.String(length=64), nullable=False)
    song_length = sq.Column(sq.Interval, nullable=False)
    album_id = sq.Column(sq.Integer, sq.ForeignKey('album.id'), nullable=False)

    album = relationship(Album, backref='song')

class Compilation(Base):
    __tablename__ = 'compilation'
    id = sq.Column(sq.Integer, primary_key=True)
    comp_title = sq.Column(sq.String(length=64), nullable=False)
    comp_release_year = sq.Column(sq.Integer, nullable=False)

class Song_Compilation(Base):
    __tablename__ = 'song_compilation'
    id = sq.Column(sq.Integer, primary_key=True)
    song_id = sq.Column(sq.Integer, sq.ForeignKey('song.id'), nullable=False)
    compilation_id = sq.Column(sq.Integer, sq.ForeignKey('compilation.id'), nullable=False)

    song = relationship(Song, backref='song_compilation')
    compilation = relationship(Compilation, backref='song_compilation')

def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

create_tables(engine)

