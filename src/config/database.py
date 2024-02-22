from sqlalchemy import MetaData, create_engine

# TODO pymysqlではなくmysqlclient（デフォのやつ）で動くようにする
engine = create_engine("mysql+pymysql://user:password@db:3306/db")
meta = MetaData()
# TODO ここの変数名適切か
connection = engine.connect()
