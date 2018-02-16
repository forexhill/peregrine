from flask import Flask, render_template, flash, request
from async_build_markets import build_arbitrage_graph_for_exchanges
from async_build_markets import build_graph_for_exchanges
import networkx as nx
import ccxt

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'peregrine-scout'

@app.route("/", methods=['GET', 'POST'])
def index():
    exchange_list = ccxt.exchanges
    if request.method == 'POST':
        selected_exchanges = request.form.getlist('exchange')

        print(selected_exchanges)

        flash(selected_exchanges)

    # if request.method == 'POST':
    #     article=request.form['article']
    #
    #     if form.validate():
    #         flash(clf.predict([article])[0])
    #     else:
    #         flash('Error categorizing article.')
    return render_template('index.html', exchange_list = exchange_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
