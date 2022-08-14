
-- A. Tabel product_category ---------------------------------------
CREATE TABLE product_category (
Id serial PRIMARY KEY,
Name varchar(80) )

INSERT INTO product_category (name) 
VALUES ('Hardisk'),('RAM'),('VGA')

SELECT * FROM product_category


-- B. Tabel product -------------------------------------------------
CREATE TABLE product (id serial PRIMARY KEY,
                      categories int REFERENCES product_category(ID),
                      name varchar(80))

INSERT INTO product (categories, name)
VALUES (2, 'Corsair'),(3,'Zotac'),(1,'Seagate'),
	  (1, 'Toshiba'), (3, 'MSI'),(3, 'Radeon RX')

SELECT * FROM product

-- C. Tabel sale ---------------------------------------------
CREATE TABLE sale (id serial PRIMARY KEY,
                   Product int REFERENCES product(id),
                   date date,
                   qty double precision,
                   price double precision,
                   state varchar(80))

INSERT INTO sale (product, date, qty, price, state)
VALUES 
    (2, '2019-08-27', 3, 8000000, 'done'), (5, '2019-10-09', 2, 4500000, 'done'),
	(4, '2019-12-12', 7, 20000000, 'cancel'), (3, '2020-01-01', 4, 10000000, 'done'),
    (1, '2020-01-31', 2, 1500000, 'done'), (1, '2020-04-13', 3, 3750000, 'done'),
    (6, '2020-07-30', 5, 20000000, 'done'), (5, '2020-12-28', 2, 2500000, 'cancel'),
    (2, '2021-01-20', 3, 10500000, 'done'), (5, '2021-07-09', 2, 4500000, 'cancel')

SELECT * FROM sale

-- D. Menampilkan data penjualan per category, dan state = done
SELECT 
    sale.id AS id_sale, 
    product_category.name AS category, 
    product.name AS product_name, 
    sale.state 
FROM sale
INNER JOIN product ON sale.product=product.id
INNER JOIN product_category ON product.categories=product_category.id
WHERE sale.state = 'done'
ORDER BY product_category.name

-- Menampilkan Hanya category tertentu saja (Misal VGA)
SELECT 
    sale.id AS id_sale, 
    product_category.name AS category, 
    product.name AS product_name, 
    sale.state 
FROM sale
INNER JOIN product ON sale.product=product.id
INNER JOIN product_category ON product.categories=product_category.id
WHERE sale.state = 'done' AND product_category.id=3
ORDER BY product_category.name

-- E. Menampilkan data penjualan per product dan date > 1 januari 2020
SELECT 
    sale.id AS id_sale,  
    product.name AS product_name,
    sale.date 
FROM SALE
INNER JOIN product ON sale.product=product.id
where sale.date > '2020-01-01'

