
from sqlalchemy import create_engine
from sqlalchemy import text


db_string = "postgresql://root:root@localhost:5050/mydb"

engine = create_engine(db_string)
connection = engine.connect()

connection.execute(text("CREATE TABLE IF NOT EXISTS films (title text, director text, year test"))
#connection.execute("INSERT INTO films (title,director,year) VALUES ('Doctor Stange','Scott Derrickson','2016')")
