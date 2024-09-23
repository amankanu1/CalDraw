from fastapi import APIRouter, HTTPException
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('/calculate')
async def run(data: ImageData):
    try:
        # Decode the image from the base64 string
        image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)

        # Process the image
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        response_data = []  # Use a different name to avoid confusion with the parameter
        for response in responses:
            response_data.append(response)

        return {"message": "Image processed", "data": response_data, "status": "success"}
    
    except Exception as e:
        # Handle any exceptions that occur during image processing
        raise HTTPException(status_code=400, detail=str(e))
