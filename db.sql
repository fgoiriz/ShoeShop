-- Tables definitions:

create table brands (
    id serial primary key,
    name varchar(255) not null unique
);

create table shoes (
    id serial primary key, 
    name varchar(255) not null unique, 
    brand_id int references brands(id), 
    price decimal(10, 2) not null
);

create table users (
    id serial primary key,
    first_name varchar(255) not null, 
    last_name varchar(255) not null
);


create table orders (
    id serial primary key,
    user_id int references users(id),
    date_of_order date default current_date,
    total_amount decimal(10, 2) not null
);


create table order_shoes (
    order_id int references orders(id),
    shoe_id int references shoes(id),
    primary key (order_id, shoe_id)
);
