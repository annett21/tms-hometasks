-- Active: 1667227946530@@127.0.0.1@5432@some_shop
CREATE DATABASE some_shop;

CREATE TABLE
    category(
        c_id SERIAL PRIMARY KEY,
        c_name VARCHAR(100) NOT NULL,
        c_description TEXT NOT NULL
    );

CREATE TABLE
    discount(
        d_id SERIAL PRIMARY KEY,
        d_name VARCHAR(100) NOT NULL,
        d_percent INT NOT NULL
    );

CREATE TABLE product(
        p_id SERIAL PRIMARY KEY,
        p_name VARCHAR(100) NOT NULL,
        p_price INT NOT NULL,
        c_id INT NOT NULL,
        d_id INT NOT NULL,
        CONSTRAINT FK_category_id 
            FOREIGN KEY(c_id) 
                REFERENCES category(c_id) 
                ON DELETE CASCADE,

        CONSTRAINT FK_discount_id 
            FOREIGN KEY(d_id) 
                REFERENCES discount(d_id) 
                ON DELETE CASCADE
    );


INSERT INTO category (c_name, c_description) VALUES
('Fruts', 'we all can eat it'),
('Shoes', 'no high hills'), 
('Shampo', 'no parabens'), 
('Vegetables','fermer''s product');


INSERT INTO discount (d_name, d_percent) VALUES 
('Black', 35), ('Birthday', 12), ('Extrem', 50), ('First', 15);


INSERT INTO product (p_name, p_price, c_id, d_id) VALUES 
('Apples', 12, 1, 1),
('Snikers', 200, 2, 2),
('Pantine', 23, 3, 3),
('Tomatoes', 10, 4, 4);


SELECT
    product.p_id,
    product.p_name,
    product.p_price,
    category.c_name,
    category.c_description,
    discount.d_name,
    discount.d_percent,
    product.p_price - product.p_price * discount.d_percent / 100 AS pretty_price
FROM product
    JOIN category ON category.c_id = product.c_id
    JOIN discount ON discount.d_id = product.d_id
WHERE
    product.p_price BETWEEN 10 AND 100
