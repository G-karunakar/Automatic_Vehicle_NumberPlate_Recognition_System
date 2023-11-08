import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from pyzbar.pyzbar import decode
input('........................plz click on enter to proceed........................')
root = tk.Tk()
root.withdraw
a = filedialog.askopenfilename(
    initialdir="/",
    title="close this popup after selecting the image",
    filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*"))
)
root.destroy()
# Load the image containing the QR code
qr_code_image = Image.open(a)

# Decode the QR code
decoded_objects = decode(qr_code_image)

# Extract the QR code data
if decoded_objects:
    qr_code_data = decoded_objects[0].data.decode('utf-8')
    print(f"........................QR Code data........................\n {qr_code_data}")
else:
    print("No QR code found in the image.")