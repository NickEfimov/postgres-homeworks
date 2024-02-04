-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar (100) NOT NULL,
	title varchar (100),
	birth_date date,
	notes text
);

CREATE TABLE costumers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar (100),
	contact_name varchar (100)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) UNIQUE REFERENCES costumers(customer_id),
	employee_id int UNIQUE REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar (100) NOT NULL
);