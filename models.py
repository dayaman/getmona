from flaskr import db

class Latest_Price(db.Model):
    __tablename__ = 'latest_prices'
    pair = db.Column(db.String, primary_key=True)
