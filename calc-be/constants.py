from dotenv import load_dotenv 
import os

# Load environment variables
load_dotenv()

# Use environment variables or defaults
SERVER_URL = os.getenv('SERVER_URL', '0.0.0.0')  # Default to '0.0.0.0' for deployment
PORT = os.getenv('PORT', '8000')  # Default to '8000' for Railway
ENV = os.getenv('ENV', 'dev')  # Default to 'dev'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
