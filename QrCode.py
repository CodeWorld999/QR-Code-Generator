import pyqrcode
import png
from pyqrcode import QRCode


link = input("Enter the link: ")
size = input("Size of the QRCode you want: Example-5 ")
saveAs = input("Save as: ")

# Generate QR code
url = pyqrcode.create(link)

# Create and save
url.svg(saveAs+".svg", scale = size)
url.png(saveAs+".png",scale = size)
