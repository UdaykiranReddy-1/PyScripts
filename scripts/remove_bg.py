"""
Remove Background module

This module provides functions to remove backgrounds from images using rembg.
"""

from rembg import remove
from PIL import Image

def remove_background(input_path: str, output_path: str = None) -> None:
    """
    Remove background from an image and save the result.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the output image. If None, 
                          will save with '_nbg' suffix in the same directory.
    """
    try:
        # Open the input image
        input_img = Image.open(input_path)
        
        # Remove background
        output_img = remove(input_img)
        
        # Determine output path if not provided
        if output_path is None:
            base_name = input_path.rsplit('.', 1)[0]
            ext = input_path.rsplit('.', 1)[1]
            output_path = f"{base_name}_nbg.{ext}"
        
        # Save the result
        output_img.save(output_path)
        
    except Exception as e:
        raise Exception(f"Error removing background: {str(e)}")
