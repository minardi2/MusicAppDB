import sqlalchemy

DSN = 'postgresql://postgres:valentina1923@localhost:5432/MusicAppDB'
engine = sqlalchemy.create_engine(DSN)