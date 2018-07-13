# models.py
from wsgi import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.Text())
    image_url = db.Column(
        db.String(),
        default='https://picsum.photos/180/50/'
    )

    def __repr__(self):
        return '<id {}>'.format(self.id)