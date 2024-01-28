from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://root:icecream@localhost/127.0.0.1?charset=utf8mb4")
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
