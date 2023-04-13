engine = create_engine(db_string)
connection = engine.connect()

create_user_table_query="""
CREATE TABLE IF NOT EXISTS users (
    ID SERIAL PRIMARY KEY,
    firstname varchar(50),
    lastname varchar(50),
    age int, email varchar(50),
    job varchar(50)
);"""


create_application_table_query="""
CREATE TABLE IF NOT EXISTS Application (
    ID SERIAL PRIMARY KEY,
    appname varchar(50),
    username varchar(50),
    lastconnection date,
    user_id INT references users (ID)
);"""


connection.execute(text(create_user_table_query))
connection.execute(text(create_application_table_query))


connection.commit()
connection.close()