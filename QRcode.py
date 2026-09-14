import qrcode

# Taking UPI id as input
user_id = input("Enter your upi id:")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the paymwnt URL based on the UPI ID and the payment app
# We can modify these Urls based on the payment appd we want to support

phonepe_url = f"upi://pay?pa=(upi_id)&pn=Recipient%20Name&mc=1234" 
paytm_url = f"upi://pay?pa=(upi_id)&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa=(upi_id)&pn=Recipient%20Name&mc=1234" 

#Creating qr codes for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the QR code to image file
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('goggle_pay_qr.png')

#Display the qr codes

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()


