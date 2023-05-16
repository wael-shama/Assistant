import time
import pyotp
import qrcode

k = pyotp.random_base32()
secret_key = "GeeksforGeeksIsBestForEverything"

totp_auth = pyotp.totp.TOTP(
  secret_key).provisioning_uri(
  name='Dwaipayan_Bandyopadhyay',
  issuer_name='GeeksforGeeks')
  
print(totp_auth)


# Generating QR CODE


qrcode.make(totp_auth).save("qr_auth.png")
totp_qr = pyotp.TOTP(secret_key)

# Verify Code in Python 
# We can also verify the code generated using Python.

totp = pyotp.TOTP(secret_key)
  
while True:
    print(totp.verify(input(("Enter the Code : "))))
    
    
    
# Complete Implementation
import time
import pyotp
import qrcode

key = "GeeksforGeeksIsBestForEverything"

uri = pyotp.totp.TOTP(key).provisioning_uri(
	name='Dwaipayan_Bandyopadhyay',
	issuer_name='GeeksforGeeks')

print(uri)


# Qr code generation step
qrcode.make(uri).save("qr.png")

"""Verifying stage starts"""

totp = pyotp.TOTP(key)

# verifying the code
while True:
print(totp.verify(input(("Enter the Code : "))))




