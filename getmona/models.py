from getmona import db

class Price(db.Model):
    __tablename__ = 'prices'
    pair = db.Column(db.String, primary_key=True)
    latest_price = db.Column(db.Float)
    yesterday_price = db.Column(db.Float)

    def __repr__(self):
        return '<pair={pair} latest_price={latest_price} yesterday_price={yesterday_price}>'.format(
            pair=self.pair, latest_price=self.latest_price, yesterday_price=self.yesterday_price)

def init():
    db.create_all()
