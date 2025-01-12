import qrcode

def generate_qr_code(link, filename):
    """Generates a QR code for the given link and saves it as filename."""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    generate_qr_code("https://medium.com/@uday410ry/next-js-devs-secret-weapon-677d889a53fa", "article-link.png")
    print(f"QR code saved successfully!!")