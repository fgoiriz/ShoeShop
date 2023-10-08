#!/bin/bash

# Set PostgreSQL password
export PGPASSWORD='secret'

# Empty the database and recreate the schema
psql -h localhost -U admin -d shoe_shop_db -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
psql -h localhost -U admin -d shoe_shop_db < db.sql

# Unset PostgreSQL password
unset PGPASSWORD
