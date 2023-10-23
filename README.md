Shoe Shop API

You should have already completed some source about building relational databases. To further develop your knowledge and skills, create a schema which satisfies this set of endpoints. 

Building your database schema

Ensure you have a local postgres server running with a database for this project
Develop your schema in a file in your project root, `db.sql`
Generate a bash script which will empty the database and import the schema from db.sql so as you build out the schema and make changes, you can run this script to refresh the database structure
Later on, you may consider using the end of the db.sql also to seed some of your tables where needed, i.e. you may want to fill the shoes table with a set of shoes, using INSERT statements.		


Entity information

Your database schema should be able to provide the following information. It does not include things like primary key or foreign key fields.

Brands
Should contain ‘name’

Shoes
Should contain ‘name’
should provide the brand they belong to
Price of the shoe

Users
Should contain first and last name of the user

Orders
User information of who made the order
The shoe(s) purchased in the order
The date of the order
The total monetary amount of the order 

Search
Should return a list of shoes that match a given search term

Endpoint guide

GET /brands - get all brands
GET /brands/{id} - get a brand

GET /shoes - get all shoes
GET /shoes/{id} - get a shoe 

GET /users
GET /users/{id}
POST /users
PUT /users/{id}
DELETE /users/{id}

POST /orders payload: {shoe_id, user_id} - create a new order
we can post multiple shoe_id's as a List

GET /shoes/{show_id}/orders - get all orders for a specific shoe
GET /users/{user_id}/orders - get all orders for a specific user
GET /brands/{brand_id}/orders - get all orders for a specific brand

** Because one user can order multiple shoes in one order, and one shoe can be inclued in many orders, we will need to form a many to many here. 

GET /search/{search_string} - search's all shoe names for a shoe, not exact match, but where the string exists inside the product title


Let's now imitate an admin area:

POST admin/brands - create a brand
PUT admin/brands/{id} - replace a brand
DELETE admin/brands/{id} - delete a brand

POST admin/shoes - create new shoe * will need brand
PUT admin/shoes/{id} - replace a shoe
DELETE admin/shoes/{id} - delete a shoe

GET admin/orders - get all orders
GET admin/shoes - return list of all shoes, with how many orders each shoe has




