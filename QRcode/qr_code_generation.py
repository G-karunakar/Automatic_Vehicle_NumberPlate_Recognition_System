import qrcode
def generate_qr_code(a, b):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
    qr.add_data(a)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(b)
c = input('enter name of QRcode:- ')
a=""
print('enter the text:- ')
while 1<2:
    d= input()
    if d=='@END':
        break
    e='\n'
    f=d+e
    a=a+f
b=c+'.png'
generate_qr_code(a, b)
print(f"A QR code has been generated and saved as {b}.")