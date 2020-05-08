from flask import Flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources = {r"/*/": {"origins": "*"}})

products = '[{"id":3078,"title":"Trinity Force","price":3733,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/3/3d/Trinity_Force_item.png"},{"id":3031,"title":"Infinity Edge","price":3400,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/1/15/Infinity_Edge_item.png"},{"id":3004,"title":"Manamune","price":2400,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/6/60/Manamune_item.png"},{"id":3812,"title":"Death\'s Dance","price":3600,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/1/1c/Death%27s_Dance_item.png"},{"id":3072,"title":"Bloodthirster","price":3500,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/8/8b/Bloodthirster_item.png"},{"id":3153,"title":"Blade of the Ruined King","price":3300,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/2/2f/Blade_of_the_Ruined_King_item.png"},{"id":3151,"title":"Liandry\'s Torment","price":3100,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/f/fd/Liandry%27s_Torment_item.png"},{"id":3068,"title":"Sunfire Cape","price":2750,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/6/61/Sunfire_Cape_item.png"},{"id":3143,"title":"Randuin\'s Omen","price":2900,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/0/08/Randuin%27s_Omen_item.png"},{"id":3116,"title":"Rylai\'s Crystal Scepter","price":2600,"image":"https://vignette.wikia.nocookie.net/leagueoflegends/images/f/f2/Rylai%27s_Crystal_Scepter_item.png"}]'
stock = '[{"id":3078,"amount":3},{"id":3031,"amount":5},{"id":3004,"amount":2},{"id":3812,"amount":1},{"id":3072,"amount":5},{"id":3153,"amount":10},{"id":3151,"amount":8},{"id":3068,"amount":2},{"id":3143,"amount":10},{"id":3116,"amount":3}]'

parsed_products = json.loads(products);
parsed_stock = json.loads(stock);

@app.route('/lolshop/stock')
def stock_list():
  return stock;

@app.route('/lolshop/stock/<item_id>')
def stock_show(item_id):
  stock_item = list(filter(lambda x:x["id"]==int(item_id),parsed_stock))
  return json.dumps(stock_item[0]);

@app.route('/lolshop/products')
def products_list():
  return products;

@app.route('/lolshop/products/<item_id>')
def products_show(item_id):
  product_item = list(filter(lambda x:x["id"]==int(item_id),parsed_products))
  return json.dumps(product_item[0]);

