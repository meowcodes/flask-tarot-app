# from csv import DictReader
from models import db, ReadingCardPlacement, Suit, Card, Spread, Placement, Reading

db.drop_all()
db.create_all()

db.session.add(Suit(name="Cups", element="water"))
db.session.add(Suit(name="Swords", element="air"))
db.session.add(Suit(name="Pentacles", element="earth"))
db.session.add(Suit(name="Wands", element="fire"))


db.session.add(
    Card(number=0, arcana="Major", name="The Fool"))
db.session.add(
    Card(number=1, arcana="Major", name="The Magician"))
db.session.add(
    Card(number=2, arcana="Major", name="The High Priestess"))
db.session.add(
    Card(number=3, arcana="Major", name="The Empress"))
db.session.add(
    Card(number=4, arcana="Major", name="The Emperor"))
db.session.add(
    Card(number=5, arcana="Major", name="The Heirophant"))
db.session.add(
    Card(number=6, arcana="Major", name="The Lovers"))
db.session.add(
    Card(number=7, arcana="Major", name="The Chariot"))

db.session.add(Spread(name="Three Card Spread",
                      num_of_cards=3,
                      image_url="/",
                      description="..."))

db.session.add(Spread(name="Celtic Cross",
                      num_of_cards=10,
                      image_url="/",
                      description="..."))

db.session.add(
    Placement(
        spread_id=1,
        num=1,
        details="past"))
db.session.add(
    Placement(
        spread_id=1,
        num=2,
        details="present"))
db.session.add(
    Placement(
        spread_id=1,
        num=3,
        details="future"))

db.session.add(Reading(spread_id=1,
                       thoughts="meow"))

db.session.add(
    ReadingCardPlacement(
        reading_id=1,
        card_num=3,
        placement_id=1))
db.session.add(
    ReadingCardPlacement(
        reading_id=1,
        card_num=7,
        placement_id=2))
db.session.add(
    ReadingCardPlacement(
        reading_id=1,
        card_num=0,
        placement_id=3))

db.session.commit()