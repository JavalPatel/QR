import pyqrcode
import png
from pyqrcode import QRCode

def qr(upi="6351489115@paytm", name="Patel Javal Kalpeshbhai", amount=0):
    # upi = input("Enter your upi id:- ")
    # name = input("Enter your name as per upi:- ")
    # amount = input("Enter amount:- ")
    a= "upi://pay?pa="+upi+"&pn="+name+"&mc=0000&cu=INR&am="+amount+".00&tn=Payment%20receive"
    a1 = list(a)
    for i in range(len(a1)):
        if a1[i] == " ":
            a1[i] = "%20"
    a = "".join(a1)
    print(a)

    url = pyqrcode.create(a)
    url.png('static/myqr.png', scale = 6)
    print("done")

if __name__ == "__main__":
    qr(upi="6351489115@paytm", name="Patel Javal Kalpeshbhai", amount=0)