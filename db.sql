-- Tables definitions:

create table brands (
    id serial primary key,
    name varchar(255) not null unique
);

create table shoes (
    id serial primary key, 
    name varchar(255) not null unique, 
    brand_id int not null,
    price int not null
);

create table users (
    id serial primary key,
    first_name varchar(255) not null, 
    last_name varchar(255) not null
);


CREATE TABLE orders (
    id serial primary key,
    user_id int,
    shoe_id int,
    total_amount int not null,
    date_of_order date default current_date
);


-- seedings: 

insert into brands (name) values ('Nike'), ('Adidas'), ('Fila');

insert into shoes (name, brand_id, price) values 
    ('Air Force 1', 1, 120),
    ('Rockstar', 2, 60),
    ('Disruptor', 3, 80);

insert into users (first_name, last_name) values 
    ('Alice', 'Anderson'),
    ('Bob', 'Brown'),
    ('Charlie', 'Clark');