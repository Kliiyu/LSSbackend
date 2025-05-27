# LSS Backend - User Guide

This guide provides instructions for installing and running the LSS Backend FastAPI Python project using Docker Compose.

## Prerequisites

- Docker and Docker Compose installed on your system
- MongoDB Compass (optional, for database management)
- Git (to clone the repository)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Kliiyu/LSSbackend.git
cd LSSbackend
```

### 2. Configure Environment Variables

1. Locate the `.env.example` file in the project root directory
2. Rename the file to `.env`:

```bash
mv .env.example .env
```

3. Open the `.env` file and update any settings if necessary

### 3. Build and Start the Application

Run Docker Compose to build and start the services:

```bash
docker-compose up -d
```

This will:
- Build the application container
- Start the FastAPI application
- Initialize the MongoDB database

## Verification

### Check API Documentation

1. Open your browser and navigate to:
    ```
    http://localhost:8000/docs
    ```
    
2. You should see the FastAPI Swagger documentation where you can explore and test the available endpoints.

### Connect to MongoDB with MongoDB Compass

1. Open MongoDB Compass
2. Connect to your MongoDB instance using the connection string:
    ```
    mongodb://localhost:27017
    ```
3. You should be able to browse the created databases and collections (after atleast one item exists in a collection).

## Stopping the Application

To stop the running containers:

```bash
docker-compose down
```

To stop the containers and remove volumes (will erase database data):

```bash
docker-compose down -v
```

## Troubleshooting

- If the service doesn't start, check Docker logs:
  ```bash
  docker-compose logs -f
  ```
  
- Ensure all required ports (especially 8000) aren't being used by other services

- Verify that the `.env` file has the correct configuration values
