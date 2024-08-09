## Flask API
This project is a simple Flask API application with complete CRUD functionality for managing post data. The project is containerized using Docker and Docker Compose for easy setup and deployment.

## Project Structure
```
flask-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
```

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**

    ```bash
    git clone https://gitlab.com/khachornchit/python-flask-api-docker
    cd python-flask-api-docker
    ```

2. **Build and run the Docker containers**

    ```bash
    docker-compose up --build
    ```

3. **Access the API**

   The API will be accessible at `http://localhost:5001`.

## API Endpoints

The following endpoints are available:

- **GET /posts**: Retrieve all posts
- **GET /posts/{id}**: Retrieve a single post by ID
- **POST /posts**: Create a new post
- **PUT /posts/{id}**: Update an existing post by ID
- **DELETE /posts/{id}**: Delete a post by ID

## Post Data Structure

The expected structure for post data is as follows:

```json
{
  "userId": 1,
  "id": 1,
  "title": "xxx",
  "body": "xxx"
}
```

