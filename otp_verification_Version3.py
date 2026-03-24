# Correct OTP (already set)
correct_otp = "5678"

# User se OTP lena
entered_otp = input("Enter OTP: ")

# Check karna
if entered_otp == correct_otp:
    print("Verification Successful")
else:
    print("Invalid OTP")