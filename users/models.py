from datetime import datetime

from app import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(300), nullable=False)
    last_name = db.Column(db.String(300), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # comments = db.relationship('Comment', foreign_keys='comment.user_id', backref='user', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def is_password_valid(self, password):
        return bcrypt.check_password_hash(self.password, password)