# from csv import DictReader
from models import db, ReadingCardPlacement, Suit, Card, Spread, Placement, Reading

db.drop_all()
db.create_all()

db.session.add(Suit(name="Major",
                    element="-"))
db.session.add(Suit(name="Cups",
                    element="water"))
db.session.add(Suit(name="Swords",
                    element="air"))
db.session.add(Suit(name="Pentacles",
                    element="earth"))
db.session.add(Suit(name="Wands",
                    element="fire"))


db.session.add(Card(name="The Magician",
                    suit_name="Major"))
db.session.add(Card(name="The High Priestess",
                    suit_name="Major"))
db.session.add(Card(name="The Empress",
                    suit_name="Major",
                    num=3))
db.session.add(Card(name="The Emperor",
                    suit_name="Major",
                    num=4))
db.session.add(Spread(name="Three Card Spread",
                      num_of_cards=3,
                      image_url="/",
                      description="..."))

db.session.add(
    SpreadPlacement(
        spread_id=1,
        place_num=1,
        place_meaning="past"))

db.session.add(
    SpreadPlacement(
        spread_id=1,
        place_num=2,
        place_meaning="present"))

db.session.add(
    SpreadPlacement(
        spread_id=1,
        place_num=3,
        place_meaning="future"))

db.session.add(Spread(name="Celtic Cross",
                      num_of_cards=10,
                      image_url="/",
                      description="..."))

db.session.add(Reading(spread_id=1,
                       thoughts="meow"))

db.session.add(CardReading(reading_id=1,
                           card_name="The Emperor"))
db.session.add(CardReading(reading_id=1,
                           card_name="The Magician"))
db.session.add(CardReading(reading_id=1,
                           card_name="The Empress"))

db.session.commit()