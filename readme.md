# SiteGen Backend

This project is a FastAPI application designed to generate images using the Hetic Ray Tracer. It includes a cleanup function to manage generated image files and is containerized using Docker for easy deployment.

## Project Structure

```
SiteGen-backend
├── backend
│   ├── main.py          # FastAPI application setup
│   ├── requirements.txt  # Python dependencies
│   └── Dockerfile        # Docker image instructions
├── .dockerignore         # Files to ignore in Docker build
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd SiteGen-backend
   ```

2. **Navigate to the backend directory:**
   ```
   cd backend
   ```

3. **Install dependencies:**
   You can install the required Python packages using pip:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   You can run the FastAPI application using Uvicorn:
   ```
   uvicorn main:app --reload
   ```

## Docker Instructions

To build and run the Docker container for the FastAPI application, follow these steps:

1. **Build the Docker image:**
   ```
   docker build -t sitegen-backend .
   ```

2. **Run the Docker container:**
   ```
   docker run -d -p 8000:8000 sitegen-backend
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:8000/generate?seed=<your_seed_value>` to generate an image.

## Usage

- The `/generate` endpoint accepts a `seed` parameter to generate an image. The generated image will be available for download if successfully created.

## Cleanup

The application includes a background thread that automatically deletes images older than 20 minutes to manage disk space.

## License

This project is licensed under the MIT License.