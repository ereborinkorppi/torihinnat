CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT,
	admin BOOLEAN DEFAULT false
);

CREATE TABLE locations (
	id SERIAL PRIMARY KEY,
	location_name TEXT,
	address TEXT,
	city TEXT,
	visible BOOLEAN DEFAULT true,
	postal_code TEXT
);

CREATE TABLE price_info (
	id SERIAL PRIMARY KEY,
	location_id INTEGER REFERENCES locations(id),
	product_id INTEGER REFERENCES products(id),
	price_unit TEXT,
	added TIMESTAMP,
	visible BOOLEAN DEFAULT true,
	price REAL
);

CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	product_name TEXT,
	visible BOOLEAN DEFAULT true,
);
