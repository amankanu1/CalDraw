from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from apps.calculator.route import router as calculator_router

# Load environment variables
SERVER_URL = os.getenv('SERVER_URL', '0.0.0.0')  # Default to 0.0.0.0 for Railway
PORT = os.getenv('PORT', '8000')  # Default to 8000, Railway typically uses this port
ENV = os.getenv('ENV', 'dev')

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def health():
    return {"message": "Server is running"}

app.include_router(calculator_router, prefix='/calculate', tags=['calculate'])

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))
