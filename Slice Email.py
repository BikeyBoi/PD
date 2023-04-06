# ---------------------------
# -- Practical Slice Email --
# ---------------------------

theName = input('What\'s Your Name ?').strip().capitalize() #strip() to remove the spaces , capitalize() to make only first charachter capital
theEmail = input('What\'s Your Email ?').strip()

theUsername = theEmail[:theEmail.index("@")] # to start from the beginning of the Email and stop at the @ sign
theDomain = theEmail[theEmail.index("@") + 1:] # to skip the @ sign and start from the charachter after it

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \nYour Domain Is {theDomain}")

# email = "test@gmail.com"
# print(email[:email.index("@")])