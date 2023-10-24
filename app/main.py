from fastapi import FastAPI, Depends
from pydapper import connect
from pydapper.commands import Commands
from dataclasses import dataclass


app = FastAPI(title="Shoe Shop")

# User dataclass for the fastapi validation, note that this is equivalent to a pydantic model but simpler
@dataclass
class User:
    first_name: str
    last_name: str


# Dependency to get the database connection, im using pydapper here, because I want to go as simple as possible
def get_db():
    with connect("postgresql+psycopg2://admin:secret@postgresql/shoe_shop_db") as conn:
        yield conn


# Endpoints:

# endpoints are in order following README

@app.get("/brands", tags=["Brands"])
def get_brands(db: Commands = Depends(get_db)):
    return db.query("select * from brands order by id")


@app.get("/brands/{brand_id}", tags=["Brands"])
def get_brand(brand_id: int, db: Commands = Depends(get_db)):
    return db.query(f"select * from brands where id = {brand_id}")


@app.get("/shoes", tags=["Shoes"])
def get_shoes(db: Commands = Depends(get_db)):
    return db.query("select * from shoes order by id")


@app.get("/shoes/{shoe_id}", tags=["Shoes"])
def get_shoe(shoe_id: int, db: Commands = Depends(get_db)):
    return db.query(f"select * from shoes where id = {shoe_id}")


@app.get("/users", tags=["Users"])
def get_users(db: Commands = Depends(get_db)):
    return db.query("select * from users order by id")


@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int, db: Commands = Depends(get_db)):
    return db.query(f"select * from users where id = {user_id}")


@app.post("/users", tags=["Users"])
def create_user(user: User, db: Commands = Depends(get_db)):
    return db.execute(f"insert into users (first_name, last_name) values ('{user.first_name}', '{user.last_name}')")


@app.put("/users/{user_id}", tags=["Users"])
def update_user(user_id: int, user: User, db: Commands = Depends(get_db)):
    return db.execute(f"update users set first_name = '{user.first_name}', last_name = '{user.last_name}' where id = {user_id}")


@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int, db: Commands = Depends(get_db)):
    return db.execute(f"delete from users where id = {user_id}")


@app.post("/orders", tags=["Orders"])
def create_order(shoe_ids: list[int], user_id: int, db: Commands = Depends(get_db)):
    for shoe_id in shoe_ids:
        db.execute(f"insert into orders (shoe_id, user_id) values ({shoe_id}, {user_id})")
    return {"message": "Order created"}


@app.get("/shoes/{shoe_id}/orders", tags=["Shoes"])
def get_shoe_orders(shoe_id: int, db: Commands = Depends(get_db)):
    return db.query(f"select * from orders where shoe_id = {shoe_id}")


@app.get("/users/{user_id}/orders", tags=["Users"])
def get_user_orders(user_id: int, db: Commands = Depends(get_db)):
    return db.query(f"select * from orders where user_id = {user_id}")


@app.get("/brands/{brand_id}/orders", tags=["Brands"])
def get_brand_orders(brand_id: int, db: Commands = Depends(get_db)):
    return db.query(f"select * from orders join shoes on orders.shoe_id = shoes.id where shoes.brand_id = {brand_id}")


@app.get("/search/{search_string}", tags=["Search"])
def search(search_string: str, db: Commands = Depends(get_db)):
    return db.query(f"select * from shoes where lower(name) like lower('%{search_string}%') order by id")



# Admin
@app.post("/admin/brands", tags=["Admin"])
def create_brand(name: str, db: Commands = Depends(get_db)):
    return db.execute(f"insert into brands (name) values ('{name}')")

@app.put("/admin/brands/{brand_id}", tags=["Admin"])
def update_brand(brand_id: int, name: str, db: Commands = Depends(get_db)):
    return db.execute(f"update brands set name = '{name}' where id = {brand_id}")

@app.delete("/admin/brands/{brand_id}", tags=["Admin"])
def delete_brand(brand_id: int, db: Commands = Depends(get_db)):
    return db.execute(f"delete from brands where id = {brand_id}")

@app.post("/admin/shoes", tags=["Admin"])
def create_shoe(name: str, brand_id: int, price: int, db: Commands = Depends(get_db)):
    return db.execute(f"insert into shoes (name, brand_id, price) values ('{name}', {brand_id}, {price})")

@app.put("/admin/shoes/{shoe_id}", tags=["Admin"])
def update_shoe(shoe_id: int, name: str, brand_id: int, price: int, db: Commands = Depends(get_db)):
    return db.execute(f"update shoes set name = '{name}', brand_id = {brand_id}, price = {price} where id = {shoe_id}")

@app.delete("/admin/shoes/{shoe_id}", tags=["Admin"])
def delete_shoe(shoe_id: int, db: Commands = Depends(get_db)):
    return db.execute(f"delete from shoes where id = {shoe_id}")

@app.get("/admin/orders", tags=["Admin"])
def get_orders(db: Commands = Depends(get_db)):
    return db.query("select * from orders")

@app.get("/admin/shoes", tags=["Admin"])
def get_shoes_with_orders(db: Commands = Depends(get_db)):
    return db.query("select shoes.id, shoes.name, shoes.brand_id, shoes.price, count(orders.id) as orders_count from shoes left join orders on shoes.id = orders.shoe_id group by shoes.id order by shoes.id")
