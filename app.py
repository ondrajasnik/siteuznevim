# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from models import db, Uzivatel

# Inicializace Flask aplikace a konfigurace databáze
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Cesta k databázovému souboru
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Zakázání sledování změn pro úsporu zdrojů
app.config['SECRET_KEY'] = 'mysecretkey'  # Tajný klíč pro ochranu proti CSRF

# Inicializace databáze
db.init_app(app)

# WTForm pro přidání nového uživatele
class UzivatelForm(FlaskForm):
    id = IntegerField('ID')
    jmeno = StringField('Jmeno', validators=[DataRequired()])
    prijmeni = StringField('Prijmeni', validators=[DataRequired()])
    submit = SubmitField('Přidat uživatele')

# Vytvoření tabulek a naplnění počátečními daty, pokud ještě nejsou přítomny
with app.app_context():
    db.create_all()
    if not Uzivatel.query.first():
        db.session.add_all([
            Uzivatel(jmeno='Alice', prijmeni='Smith'),
            Uzivatel(jmeno='Bob', prijmeni='Johnson'),
            Uzivatel(jmeno='Charlie', prijmeni='Brown')
        ])
        db.session.commit()

@app.route('/')
def index():
    uzivatele = Uzivatel.query.all()
    return render_template('index.html', uzivatele=uzivatele)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = UzivatelForm()
    if form.validate_on_submit():
        new_uzivatel = Uzivatel(jmeno=form.jmeno.data, prijmeni=form.prijmeni.data, id=form.id.data)
        db.session.add(new_uzivatel)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    uzivatel = Uzivatel.query.get_or_404(id)
    db.session.delete(uzivatel)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
