import qrcode
import cv2
qr = qrcode.make("Manan Patel")
qr.save("Qrcode.png")

d= cv2.QRCodeDetector()
val , points, straight_qrcode = d.detectAndDecode(cv2.imread("Qrcode.png"))
print(val)
