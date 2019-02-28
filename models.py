from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


def connect_db(app):
    """ Connects to database """

    db.app = app
    db.init_app(app)


class ReadingCardPlacement(db.Model):
    """
    List of all cards in each reading based on placement.

    Connects Reading, Card, Placement tables

    Through Relationships: card.readings,
                           card.placements,
                           placements.cards,
                           reading.cards
    """

    __tablename__ = "r_cards_placements"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    reading_id = db.Column(
        db.Integer,
        db.ForeignKey('readings.id')
    )

    card_num = db.Column(
        db.Integer,
        db.ForeignKey('cards.number')
    )

    placement_id = db.Column(
        db.Integer,
        db.ForeignKey('placements.id'),
        nullable=False
    )

    def __repr__(self):
        rpc = self

        return f"< Reading {rpc.reading_id}, {rpc.card_name} >"


class Suit(db.Model):
    """
    All suits in deck

    suit.cards: cards in this suit
    """

    __tablename__ = "suits"

    name = db.Column(
        db.String(10),
        primary_key=True
    )

    element = db.Column(
        db.String(10),
        nullable=False
    )

    description = db.Column(db.Text)

    cards = db.relationship(
        'Card',
        backref='suit'
    )

    def __repr__(self):
        suit = self

        return f"< {suit.name} Suit, {suit.elemet}: {suit.description} >"


class Card(db.Model):
    """
    78 Card Rider-Waite Tarot Deck

    card.readings: readings this card was in
    card.placements: placements this card was read in
    """

    __tablename__ = "cards"

    number = db.Column(
        db.Integer,
        primary_key=True
    )

    arcana = db.Column(
        db.String(10),
        nullable=False
    )

    name = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    suit_name = db.Column(
        db.String(10),
        db.ForeignKey('suits.name')
    )

    image_url = db.Column(db.Text)

    description = db.Column(db.Text)

    meaning = db.Column(db.Text)

    readings = db.relationship(
        'Reading',
        secondary='r_cards_placements',
        backref='cards'
    )

    placements = db.relationship(
        'Placement',
        secondary='r_cards_placements',
        backref='cards'
    )

    def __repr__(self):

        return f"< {self.name} >"

    def introduce(self):
        """ Introduce card """

        return f"{self.name}: {self.description}"

    @classmethod
    def get_by_suit(cls, suit):
        """ Gets all cards of requested suit"""

        return cls.query.filter_by(suit=suit).all()


class Spread(db.Model):
    """
    Spreads with descriptions

    spread.placements: placements details for this spread
    spread.readings: readings that used this spread
    """

    __tablename__ = "spreads"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    num_of_cards = db.Column(
        db.Integer,
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(20)
    )

    placements = db.relationship(
        'Placement',
        backref='spread'
    )

    def __repr__(self):

        return f"< {self.name} Spread ({self.num_of_cards} Cards) >"

    @classmethod
    def get_by_card_num(cls, card_num):
        """ Gets all spreads with requested number of cards """

        return cls.query.filter_by(num_of_cards=card_num).all()


class Placement(db.Model):
    """
    Placement details for each spread.

    placement.cards: cards that have been read in this placement
    """

    __tablename__ = "placements"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    spread_id = db.Column(
        db.Integer,
        db.ForeignKey('spreads.id'),
        nullable=False
    )

    num = db.Column(
        db.Integer,
        nullable=False
    )

    details = db.Column(
        db.String(100),
        nullable=False
    )

    def __repr__(self):

        return f"< Card #{self.num} Placement Details for Spread ID {self.spread_id} >"


class Reading(db.Model):
    """ 
    Reading details

    reading.cards: cards in this reading
    reading.cards_placements: placement each card was in for this reading
    """

    __tablename__ = "readings"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    timestamp = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        index=True
    )

    spread_id = db.Column(
        db.Integer,
        db.ForeignKey('spreads.id')
    )

    thoughts = db.Column(db.Text)

    cards_placements = db.relationship(
        'ReadingCardPlacement',
        backref='readings'
    )

    def __repr__(self):

        return f"< Reading {self.id} >"