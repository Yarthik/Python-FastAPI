# Python-FastAPI

# Python FastAPI Product Management

## Setup Instructions

1. Install Python 3.11 or higher.
2. Create a virtual environment: python -m venv venv source venv/bin/activate # For Linux/Mac venv\Scripts\activate # For Windows
3. Install dependencies: pip install -r requirements.txt
4. Set up MySQL and create a database `products_db`. Update `DATABASE_URL` in `database.py`.
5. Run the server: uvicorn main:app --reload
6. Test APIs using Postman or any REST client.

## Endpoints

- `GET /product/list`: List products with pagination.
- `GET /product/{pid}/info`: Get product details by ID.
- `POST /product/add`: Add a new product.
- `PUT /product/{pid}/update`: Update a product by ID.
