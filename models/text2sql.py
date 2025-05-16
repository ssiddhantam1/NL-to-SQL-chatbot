from transformers import pipeline

# For demo, static mapping for quick response. Replace with actual model for production.
_demo_map = {
    "show all users": "SELECT * FROM users;",
    "list all products": "SELECT * FROM products;",
    "show all orders": "SELECT * FROM orders;",
    "users from france": "SELECT * FROM users WHERE country = 'France';",
    "orders after may 1": "SELECT * FROM orders WHERE order_date > '2024-05-01';",
}

def get_text2sql_pipeline():
    try:
        pipe = pipeline("text2sql-generation", model="defog/sqlcoder-7b-2")
        return pipe
    except Exception:
        return None

def nl_to_sql(question, schema=None):
    # Static mapping for demo; use model for production.
    q = question.lower()
    for k, v in _demo_map.items():
        if k in q:
            return v
    # If model available, call it
    pipe = get_text2sql_pipeline()
    if pipe:
        result = pipe(question)
        sql_query = result[0]['generated_text']
        return sql_query
    return "-- Sorry, no SQL generated for this question."