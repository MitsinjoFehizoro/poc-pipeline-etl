CREATE TABLE IF NOT EXISTS categories(
	id SERIAL PRIMARY KEY,
	category VARCHAR(250) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS products(
	id SERIAL PRIMARY KEY,
	product VARCHAR(250) NOT NULL,
	unit_price DECIMAL(10, 1),
	category_id INT,
	item VARCHAR(50) NOT NULL,
	CONSTRAINT fk_category FOREIGN KEY(category_id) REFERENCES categories(id)
);

