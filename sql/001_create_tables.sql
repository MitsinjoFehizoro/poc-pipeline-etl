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

CREATE TABLE IF NOT EXISTS payment_methods(
	id SERIAL PRIMARY KEY,
	method VARCHAR(259) NOT NULL
);

CREATE TABLE IF NOT EXISTS sales(
	id SERIAL PRIMARY KEY,
	transaction_id VARCHAR(20) NOT NULL UNIQUE,
	customer_id VARCHAR(20) NOT NULL,
	unit_price DECIMAL(10, 1) NOT NULL,
	quantity DECIMAL(5, 1) NOT NULL, 
	total_price DECIMAL (12, 1) NOT NULL,
	location VARCHAR(250),
	transaction_date DATE NOT NULL,
	discount_applied BOOLEAN NOT NULL,
	product_id INT,
	payment_method_id INT,
	CONSTRAINT fk_product FOREIGN KEY(product_id) REFERENCES products(id),
	CONSTRAINT fk_payment_method FOREIGN KEY(payment_method_id) REFERENCES payment_methods(id)
);