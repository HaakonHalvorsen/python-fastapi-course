import databases
import sqlalchemy

from socialmedia_api.config import config  # This line run config.py

# Metadata to store info about our tables and columns
metadata = sqlalchemy.Metadata()

post_table = sqlalchemy.table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("body", sqlalchemy.String),
)

comment_table = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("body", sqlalchemy.String),
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.id"), nullable=False),
)

# Connect to database with SQLAlchemy
engine = sqlalchemy.create_engine(
    config.DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create all tables based on metadata
metadata.create_all(engine)

# Uses databases module to create a database object to interact with the database
database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
