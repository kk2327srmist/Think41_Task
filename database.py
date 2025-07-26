import pandas as pd
import os

DATA_DIR = '../data'

def load_data():
    products = pd.read_csv(os.path.join(DATA_DIR, 'products.csv'))
    orders = pd.read_csv(os.path.join(DATA_DIR, 'orders.csv'))
    order_items = pd.read_csv(os.path.join(DATA_DIR, 'order_items.csv'))
    inventory = pd.read_csv(os.path.join(DATA_DIR, 'inventory_items.csv'))
    return products, orders, order_items, inventory