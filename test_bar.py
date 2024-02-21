import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import HorizontalSquareBarsDrawer

vcf = '''BEGIN:VCARD
N:Wesley;Nick;
TEL;TYPE=mobile,VOICE:+17086060637
EMAIL:nick@urbanriv.org
ORG:Urban Rivers
TITLE:Executive Director
ADR;TYPE=WORK,PREF:;;1440 N Kingsbury St Suite 005;Chicago;IL;60642;
URL:UrbanRivers.org
VERSION:3.0
END:VCARD
'''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(vcf)

img_1 = qr.make_image(

    image_factory=StyledPilImage, 
    module_drawer=HorizontalSquareBarsDrawer())

img_1.save("some_file.png")