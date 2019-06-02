from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cx_Oracle

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username='demoproj',
        password='pwd1demoproject',
        hostname='127.0.0.1',
        port='1521',
        database='xe',
    )
)
#engine = create_engine('sqlite:///./database/movie.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
