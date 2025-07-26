from queries import get_top_5_products, get_order_status, get_inventory_count

def handle_query(query, products, orders, order_items, inventory):
    if "top 5" in query.lower():
        return get_top_5_products(order_items, products).to_dict(orient='records')
    elif "status of order" in query.lower():
        order_id = ''.join(filter(str.isdigit, query))
        return get_order_status(order_id, orders)
    elif "how many" in query.lower():
        words = query.split()
        try:
            idx = words.index("many") + 1
            product_name = ' '.join(words[idx:]).replace("are left in stock", "").strip()
        except:
            product_name = ""
        return {"stock_count": get_inventory_count(product_name, inventory)}
    else:
        return {"message": "Sorry, I don't understand the question."}