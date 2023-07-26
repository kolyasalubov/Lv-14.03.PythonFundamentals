from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer, UnicodeText, String

engine = create_engine("sqlite:///database_new.db")
metadata = MetaData()

posts_table = Table("posts",
                    metadata,
                    Column("id", Integer, primary_key=True, autoincrement=True),
                    Column("created", String, nullable=False),
                    Column("title", String(200), nullable=False),
                    Column("content", UnicodeText, nullable=False)
                    )

metadata.create_all(engine)
