-- Simple demo schema and some data

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT,
    signup_date DATE
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    order_date DATE,
    quantity INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);

INSERT INTO users (name, country, signup_date) VALUES
('Alice', 'France', '2024-05-01'),
('Bob', 'India', '2024-04-12'),
('Charlie', 'USA', '2024-05-10');

INSERT INTO products (name, price) VALUES
('Widget', 9.99),
('Gadget', 19.99),
('Thingamajig', 29.99);

INSERT INTO orders (user_id, product_id, order_date, quantity) VALUES
(1, 1, '2024-05-12', 2),
(2, 2, '2024-04-15', 1),
(3, 3, '2024-05-11', 5),
(1, 2, '2024-05-13', 1);