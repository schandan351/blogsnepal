import pyqrcode

def qrcode():
    q=pyqrcode.create("http://www.barsacgudail.com")
    q.png('barsha.png',scale=6)
    print("qrcode is generated")

if __name__=='__main__':
    qrcode()

    