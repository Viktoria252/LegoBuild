from datetime import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
import datetime


class Comment(SqlAlchemyBase, UserMixin):
    __tablename__ = "comments"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    body = sqlalchemy.Column(sqlalchemy.Text(100), nullable=False)
    timestamp = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.datetime.utcnow)
    blog_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('blogs.id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.body}', '{self.timestamp}')"