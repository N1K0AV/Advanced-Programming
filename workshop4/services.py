import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_ud")
def hello_ud():
    """
    Endpoint to return a welcome message.
    """
    return "Welcome to UD!"

# Corrected connection string to match the local PostgreSQL server setup.
engine = create_engine('postgresql://myuser:mypassword@localhost:5432/mydatabase')
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

metadata.create_all(engine)  # make sure to create the table

@app.get("/products")
def get_products():
    """
    Endpoint to fetch all products from the database.
    """
    query = products.select()
    result = session.execute(query)
    products_list = result.fetchall()
    return [{"id": product.id, "name": product.name, "description": product.description} for product in products_list]

@app.post("/products")
def create_product(name: str, description: str):
    """
    Endpoint to create a new product in the database.
    """
    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
