def get_top_5_products(order_items, products):
    top = order_items['product_id'].value_counts().head(5).reset_index()
    top.columns = ['product_id', 'count']
    return top.merge(products, left_on='product_id', right_on='id')[['name', 'count']]

def get_order_status(order_id, orders):
    order = orders[orders['order_id'] == int(order_id)]
    if order.empty:
        return "Order not found."
    status = order[['status', 'created_at', 'shipped_at', 'delivered_at', 'returned_at']].to_dict('records')[0]
    return status

def get_inventory_count(product_name, inventory):
    items = inventory[(inventory['product_name'].str.lower() == product_name.lower()) & (inventory['sold_at'].isnull())]
    return len(items)