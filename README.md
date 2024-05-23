# FastAPI CRUD with MongoDB

This project demonstrates how to build a FastAPI application with CRUD operations using MongoDB. The project is structured to follow the Abstract Factory pattern, promoting clean code organization and maintainability.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases how to create a scalable and maintainable FastAPI application with MongoDB. By applying the Abstract Factory pattern, we ensure a clear separation of concerns and easy extensibility for future enhancements.

## Project Structure

fastapi-crud-mongodb/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── item_service.py
│   │   └── mongodb_item_service.py
│   │   └── item_factory.py
│   └── database.py
├── .env
└── requirements.txt



## Features

- FastAPI framework for building APIs
- MongoDB for data storage
- Abstract Factory pattern for service creation
- Clean separation of models, services, and application logic
- Interactive API documentation with Swagger UI

## Installation

### Prerequisites

- Python 3.7+
- MongoDB instance running locally or remotely

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/fastapi-crud-mongodb.git
    cd fastapi-crud-mongodb
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your MongoDB connection details:
    ```
    DATABASE_URL=mongodb://localhost:27017
    DATABASE_NAME=fastapi_db
    ```

## Usage

### Run the application

1. **Activate the virtual environment if not already activated:**
    ```bash
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

2. **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```

3. **Access the API documentation:**
    Open your browser and go to `http://127.0.0.1:8000/docs` to interact with the API using Swagger UI.

## API Endpoints

- **Create an Item**
    - **Endpoint:** `POST /items/`
    - **Description:** Create a new item.
    - **Request Body:**
        ```json
        {
            "name": "Item Name",
            "description": "Item Description",
            "price": 100.0,
            "tax": 5.0
        }
        ```

- **Read Items**
    - **Endpoint:** `GET /items/`
    - **Description:** Get a list of items.
    - **Query Parameters:**
        - `skip`: Number of items to skip (default: 0)
        - `limit`: Maximum number of items to return (default: 10)

- **Read an Item**
    - **Endpoint:** `GET /items/{item_id}`
    - **Description:** Get a single item by its ID.

- **Update an Item**
    - **Endpoint:** `PUT /items/{item_id}`
    - **Description:** Update an existing item by its ID.
    - **Request Body:**
        ```json
        {
            "name": "Updated Item Name",
            "description": "Updated Item Description",
            "price": 150.0,
            "tax": 10.0
        }
        ```

- **Delete an Item**
    - **Endpoint:** `DELETE /items/{item_id}`
    - **Description:** Delete an item by its ID.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


