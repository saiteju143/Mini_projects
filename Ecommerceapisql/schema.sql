CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(250) unique NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL 
        CHECK (price>0),
    inventory INTEGER NOT NULL
        CHECK (inventory>=0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    total_amount NUMERIC(10,2) NOT NULL
        CHECK(total_amount>0),
    status VARCHAR(30) NOT NULL
        DEFAULT 'placed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_order
    FOREIGN KEY (user_id)
    REFERENCES users(id)
);
CREATE TABLE IF NOT EXISTS order_items(
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL
        CHECK(unit_price>0),
    quantity NUMERIC(10,2) NOT NULL
        CHECK(quantity>0),
    item_price NUMERIC(10,2) NOT NULL
        CHECK(item_price>0),
    CONSTRAINT fk_order_id
    FOREIGN KEY (order_id)
    REFERENCES orders(id)
    ON DELETE CASCADE,
    CONSTRAINT fk_order_product_id
    FOREIGN KEY (product_id)
    REFERENCES products(id)
);

