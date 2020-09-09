from app import db
from sqlalchemy.dialects.postgresql import JSON


voyages = db.Table('voyages',
      db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
      db.Column('celestial_bodies_id', db.Integer, db.ForeignKey('celestial_bodies.id'), primary_key=True)
)


class CelestialBodies(db.Model):
    __tablename__ = 'celestial_bodies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    image = db.Column(db.String())
    celestial_body_type = db.Column(db.String())
    gravity = db.Column(db.Integer())
    landmark = db.relationship('Landmark', backref='celestial_bodies', lazy=True)
    user = db.relationship('User', secondary=voyages, back_populates='user')


    def __init__(self, name, image, celestial_body_type, gravity):
      self.name = name
      self.image = image
      self.celestial_body_type = celestial_body_type
      self.gravity = gravity

    def __repr__(self):
          return '<id {}>'.format(self.id)


class Landmark(db.Model):
    __tablename__ = 'landmark'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    landmark_type = db.Column(db.String())
    image = db.Column(db.String())
    description = db.Column(db.String())
    celestial_body_id = db.Column(db.Integer, db.ForeignKey('celestial_bodies.id'),
        nullable=False) 

    def __init__(self, name, landmark_type, image, description, celestial_body_id):
      self.name = name
      self.landmark_type = landmark_type
      self.image = image
      self.description = description
      self.celestial_body_id = celestial_body_id

    def __repr__(self):
          return '<id {}>'.format(self.id)

class User(db.Model): 
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password_digest = db.Column(db.String())
    passenger = db.relationship('Passenger', backref='passengers', lazy=True)
    celestial_bodies = db.relationship('CelestialBodies', secondary=voyages, back_populates='celestial_bodies')


    def __init__(self, user_name, email, password_digest):
      self.user_name = user_name
      self.email = email
      self.password_digest = password_digest

    def __repr__(self):
            return '<id {}>'.format(self.id)

class Passenger(db.Model): 
    __tablename__ = 'passengers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.String())
    weight = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False) 
    



    def __init__(self, name, age, weight):
      self.name = name
      self.age = age
      self.weight = weight
      self.user_id = user_id

    def __repr__(self):
            return '<id {}>'.format(self.id)






