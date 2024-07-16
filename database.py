from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://fastapiuser:fastapipass@0.0.0.0:5432/todo-app-fastapi-on-nextjs"

# DBへの接続エンジン
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# DBセッション（DBの一連の操作をまとめて、それらをDBに適応する）を作成・管理するためのもの
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 新しいDBモデルを作成する際のベースとなるクラスを作成する
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()