import cv2
import qrcode

# Load the QR code image
qr_code = cv2.imread('Toce_QR.png')

# Create a QRCode detector
qr_code_detector = cv2.QRCodeDetector()

# Detect and decode the QR code
retval, decoded_info, decoded_points, straight_qrcode = qr_code_detector.detectAndDecodeMulti(qr_code)

# Check if a QR code was detected and decoded
if retval:
    for data in decoded_info:
        print('QR Code Data:', data)
else:
    print('No QR code found or could not be decoded.')
