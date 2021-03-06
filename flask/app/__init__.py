from flask import Flask, render_template
from app.dynamodb_access import get_all_readings, get_item_by_attribute

app = Flask(__name__)


@app.get('/')
def index():
    readings = get_all_readings()
    return render_template('index.html', readings=readings)


@app.get('/graph')
def graph():
    
    # SENSOR 1 
    items = get_item_by_attribute('Camera', 1)
    items.sort(key=lambda item: item['datetime'])
    labels = [row['datetime'] for row in items]
    values = [int(row['Speed']) for row in items]

    # SENSOR 1
    items2 = get_item_by_attribute('Camera', 2)
    items2.sort(key=lambda item: item['datetime'])
    labels2 = [row['datetime'] for row in items2]
    values2 = [int(row['Speed']) for row in items2]

    # SENSOR 1
    items3 = get_item_by_attribute('Camera', 3)
    items3.sort(key=lambda item: item['datetime'])
    labels3 = [row['datetime'] for row in items3]
    values3 = [int(row['Speed']) for row in items3]

    return render_template('graph.html', labels=labels, values=values, labels2=labels2, values2=values2, labels3=labels3, values3=values3)
