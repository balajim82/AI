from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

DB_URL = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
