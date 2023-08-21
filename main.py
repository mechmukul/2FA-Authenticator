import time
import pyotp
import qrcode

# Generate a valid base32 secret key
key = pyotp.random_base32()
print(f"Generated Secret Key: {key}")
totp = pyotp.TOTP(key)

# Display current OTP
print(totp.now())

# Generate a QR code for the key
uri = totp.provisioning_uri(name="Mukul Mech", issuer_name="2FA CyberGritt")
print(uri)

# Adjust QR code size for better recognition
img = qrcode.make(uri)
img = img.resize((256, 256))
img.save("otpgen.png")

# Ask user for the 2FA code
input_code = input("Enter 2FA Code: ")
print(totp.verify(input_code))

# Continuously prompt user for 2FA code and verify it
while True:
    input_code = input("Enter 2FA code (or 'exit' to stop): ")
    
    if input_code.lower() == 'exit':
        break

    print(totp.verify(input_code))
