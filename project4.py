import qrcode


message = "Kya re Hathi🐘🐘 Kya dekh rha h jake padhai kr"


qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(message)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")
img.save("kunal_qr_code.png")

print("QR code saved as kunal_qr_code.png")