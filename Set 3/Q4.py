''' Find double space in the string'''

from re import A


a = "Hey, I am Preksha  Thakkar. I am a  girl"

b = a.find("  ")
# finds the first double space char index in the string

# c = a.replace("  ", " ")
# replaces only the first double space char in the string

c = a.replace("  ", " ")
# replaces all double space char in the string
print(a)