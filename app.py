from flask import Flask, request, render_template, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Deck, Suit

app= Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tarot_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)

@app.route('/')
def show_index():
    """ Show index page """

    return render_template("index.html")

@app.route('/deck')
def show_deck():
    """ Show full deck """

    deck = Deck.query.all()

    return render_template("deck.html", deck=deck)

@app.route('/deck/<card_name>')
def card_detail(card_name):
    """ Show card detail """

    card = Deck.query.get(card_name)

    return render_template("card.html", card=card)


@app.route('/spreads')
def show_spreads():
    """ Show all spreads """

    spreads = Spread.query.all()

    return render_template("spreads.html", spreads=spreads)

@app.route('/spreads/new')
def new_spread_form():
    """ Show new spread form """

    return render_template("spread_new.html")

@app.route('/spreads', methods=['POST'])
def create_spread():
    """ Create spread """

    name = request.form.get('name')
    num_of_cards = request.form.get('num_of_cards')
    image_url = request.form.get('image_url')
    description = request.form.get('description')

    new_spread = Spread(name=name, num_of_cards=num_of_cards, image_url=image_url, description=description)

    db.session.add(new_spread)
    db.session.commit()

    return redirect('/spreads')

@app.route('/spreads/<int:spread_id>')
def spread_detail(spread_id):
    """ Show spread detail """

    spread = Spreads.query.get(spread_id)

    return render_template("spread.html", spread=spread)

@app.route('/spreads/<int:spread_id>/edit')
def edit_spread_form(spread_id):
    """ Show edit spread form"""

    spread = Spreads.query.get(spread_id)

    return render_template("spread_edit.html", spread=spread)

@app.route('/spreads/<int:spread_id>/edit', methods=['POST'])
def edit_spread(spread_id):
    """ Edit spread """

    updated_spread = Spreads.query.get(spread_id)

    updated_spread.name = request.form.get('name')
    updated_spread.num_of_cards = request.form.get('num_of_cards')
    updated_spread.image_url = request.form.get('image_url')
    updated_spread.description = request.form.get('description')

    db.session.add(updated_spread)
    db.session.commit()

    return redirect('/spreads')

@app.route('/spreads/<int:spread_id>/delete', methods=['POST'])
def delete_spread(spread_id):
    """ Delete spread """

    spread = Spreads.query.get(spread_id)

    db.session.delete(spread)
    db.session.commit()

    redirect('/spreads')

@app.route('/readings')
def show_readings():
    """ Show all readings """

    readings = Reading.query.all()

    return render_template("readings.html", readings=readings)

@app.route('/readings/new')
def new_reading_form():
    """ Show new reading form """

    spreads = Spread.query.all()

    return render_template("reading_new.html", spreads=spreads)

@app.route('/readings', methods=['POST'])
def do_reading():
    """ Process reading """

    name = request.form.get('name')
    spread_id = request.form.get('spread_id')

    new_reading = Reading(name=name, spread_id=spread_id)

    db.session.add(new_reading)
    db.session.commit()

    return redirect('/readings')