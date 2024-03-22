from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, TimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is my secret key, create urs.'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    locURL = URLField('Location URL', validators=[DataRequired(),URL()])
    openTime = StringField('Open Time eg. 8AM', validators=[DataRequired()])
    closeTime = StringField('Close Time eg. 9PM', validators=[DataRequired()])
    coffeeRating = SelectField('Coffee Rating',choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifiRating = SelectField('Wifi Rating',choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    powerOutletRating = SelectField('Power Outlet Rating',choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        row = [form.cafe.data,form.locURL.data, form.openTime.data, form.closeTime.data,form.coffeeRating.data,form.wifiRating.data, form.powerOutletRating.data]
        with open('day-62/cafe-data.csv',mode='a',encoding='utf-8') as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('day-62/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
