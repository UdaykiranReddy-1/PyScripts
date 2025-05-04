"""
QR Code Generator module

This module provides functions to generate QR codes from URLs or text.
"""

import qrcode

def create_qr_code(data: str, output_path: str, version: int = 1, box_size: int = 10, border: int = 4) -> None:
    """
    Create a QR code from the given data and save it as an image file.
    
    Args:
        data (str): The data to encode in the QR code (URL or text)
        output_path (str): Path to save the generated QR code image
        version (int): QR code version (1-40)
        box_size (int): Size of each box in pixels
        border (int): Width of the border in boxes
    """
    try:
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_path)
        
        print(f"QR code saved successfully to {output_path}")

    except Exception as e:
        raise Exception(f"Error creating QR code: {str(e)}")
