from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120))
    name = db.Column(db.String(120))
    active = db.Column(db.Integer, default=1)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('user', lazy='dynamic'))

    _restricted_fields = ["password", "active", "id"]

    def __init__(self, user_data):
        for k, v in user_data.items():
            self.__setattr__(k, v)

    def __str__(self):
        return self.username

    def __repr__(self):
        return '<User %r>' % self.username

    def as_dict(self):
        return {
            c.name: getattr(self, c.name) for c in self.__table__.columns
            if c.name not in self._restricted_fields
        }


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name

    def __str__(self):
        return self.name
