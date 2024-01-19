import sqlalchemy

from sqlalchemy.orm import sessionmaker

from models import create_tables, Genre

DSN = 'postgresql://postgres:valentina1923@localhost:5432/MusicAppDB'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()

genre1 = Genre(genre_name='Hip-hop')
print(genre1.id)

session.add(genre1)
session.commit()

print(genre1.id)
print(genre1)
session.close()
