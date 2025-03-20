from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
from fastapi.responses import FileResponse
import threading
import time
from dotenv import load_dotenv

load_dotenv()

# Retrieve environment variables
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000",],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EXECUTABLE_PATH = "HeticRayTracer.exe"  

@app.get("/generate")
def generate_image(seed: int):
    image_name = f"output_{seed}.png"
    
    if os.path.exists(image_name):
        os.remove(image_name)

    process = subprocess.run([EXECUTABLE_PATH, str(seed)])

    if os.path.exists(image_name):
        return FileResponse(image_name, media_type="image/png")
    
    return {"error": "Image non générée", "output": process.stdout, "error_log": process.stderr}


def cleanup_images():
        while True:
            time.sleep(1200)
            
            for file in os.listdir("."):
                if file.startswith("output_") and file.endswith(".png"):
                    os.remove(file)
                    print(f"Deleted: {file}")

thread = threading.Thread(target=cleanup_images, daemon=True)
thread.start()