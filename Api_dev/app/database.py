
from multiprocessing import pool
from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from . local_setting import postgressql as settings 

# #SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Smith3dx:@localhost/fastapi'

# #engine = create_engine(SQLALCHEMY_DATABASE_URL)

# #SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
def get_engine(user, passwd, host, post, db):
    url = f"postgresql://{user}:{passwd}@{host}:{post}/db"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine    

engine = get_engine(settings['pguser'],
                    settings['pgpasswd'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])

engine.url

def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file ')
    return get_engine(settings['pguser'],
                    settings['pgpasswd'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])

def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine())
    return session


session = get_session()


