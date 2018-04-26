from getmona import db

class Latest_Price(db.Model):
    __tablename__ = 'latest_prices'
    pair = db.Column(db.String, primary_key=True)
    price = db.Column(db.Float)

    def __repr__(self):
        return '<pair={pair} price={price!r}>'.format(
            pair=self.pair, price=self.price)

def init():
    db.create_all()
    
