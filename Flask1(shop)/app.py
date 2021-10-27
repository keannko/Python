from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from cloudipsp import Api, Checkout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class goods (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    about = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.title}"


@app.route('/')
def main():
    items = goods.query.order_by(goods.title.desc()).all()
    return render_template('main.html',items=items)

@app.route('/item')
def asdss():
    return render_template('item.html')


@app.route('/create',methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        about = request.form['about']
        price = request.form['price']
        item = goods(title=title, about=about, price=price)
        db.session.add(item)
        db.session.commit()
        return redirect('/')
    else:
        render_template('main.html')
    return render_template('create.html')


@app.route('/item/<int:id>')
def item(id):
    item = goods.query.get(id)
    api = Api(merchant_id=1397120,
          secret_key='test')
    checkout = Checkout(api=api)
    data = {
    "currency": "UAH",
    "amount": str(item.price) + "00"
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@app.route('/delete', methods=['POST', 'GET'])
def idelete():
    data = goods.query.all()
    if request.method == 'POST':
        ids = request.form ['delete']
        tovar = goods.query.get(ids)
        try:   
            db.session.delete(tovar)
            db.session.commit()
            return redirect('/delete')
        except:
            return render_template('error.html')
    else:
        return render_template ('delete.html', data = data)


   

if __name__ == '__main__':
    app.run(debug=True)