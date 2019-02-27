from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def connect_db(app):
    """ Connects to database """

    db.app = app
    db.init_app(app)


class Card(db.Model):
    """ Rider-Waite Tarot Deck """

    __tablename__ = "cards"

    name = db.Column(db.String(30),
                     primary_key=True)
    arcana = db.Column(db.String(5),
                       nullable=False)
    suit = db.Column(db.String(10),
                     db.ForeignKey('suits.name'))
    num = db.Column(db.Integer)
    image_url = db.Column(db.Text)
    description = db.Column(db.Text)
    meaning = db.Column(db.Text)

    suit = db.relationship('Suit', backref='cards')
    spread = db.relationship('Spread', backref='cards')
    cards_readings = db.relationship('CardReading',
                                     backref='cards')
    reading = db.relationship('CardReading',
                              secondary='cards_readings',
                              backref='cards')

    def __repr__(self):
        card = self

        return f"<Tarot Card {card.id} {card.name}>"

    def introduce(self):
        """ Introduce card """

        return f"{self.name}: {self.description}"

    @classmethod
    def get_by_arcana(cls, arcana):
        """ Gets all cards of major or minor arcana"""

        return cls.query.filter_by(arcana=arcana).all()

    @classmethod
    def get_by_suit(cls, suit):
        """ Gets all cards of requested suit"""

        return cls.query.filter_by(suit=suit).all()


class Suit(db.Model):
    """ Suits """

    __tablename__ = "suits"

    name = db.Column(db.String(10),
                     primary_key=True)
    element = db.Column(db.String(10),
                        nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        suit = self

        return f"<{suit.name} Suit, {suit.elemet}: {suit.description}>"


class Spread(db.Model):
    """ Spreads """

    __tablename__ = "spreads"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(30),
                     nullable=False,
                     unique=True)
    num_of_cards = db.Column(db.Integer,
                             nullable=False)
    image_url = db.Column(db.Text,
                          nullable=False)
    description = db.Column(db.Text,
                            nullable=False)

    def __repr__(self):
        spread = self

        return f"<{spread.name} Spread ({spread.num_of_cards} Cards): {spread.description}>"

    @classmethod
    def get_by_card_num(cls, card_num):
        """ Gets all spreads with requested number of cards """

        return cls.query.filter_by(num_of_cards=card_num).all()


class Reading(db.Model):
    """ Saved Readings """

    __tablename__ = "readings"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String(30),
                     nullable=False,
                     unique=True)
    spread_id = db.Column(db.Integer,
                          db.ForeignKey('spreads.id'))
    
    cards_readings = db.relationship('CardReading',
                                     backref='readings')


class CardReading(db.Model):
    """ Each Card in Each Reading Association Table """

    __tablename__ = "cards_readings"

    reading_id = db.Column('reading_id',
                           db.Integer,
                           db.ForeignKey('readings.id'),
                           primary_key=True)
    card_id = db.Column('card_name',
                        db.String(30),
                        db.ForeignKey('cards.name'),
                        primary_key=True)