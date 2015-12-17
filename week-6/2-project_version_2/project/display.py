import unicodedata

def print_skulls():
    print("\n"+ (unicodedata.lookup("skull") + " ") * 30 + "\n")

def print_error_message():
    print_skulls()
    print(" FATAL ERROR ")
    print_skulls()

def print_luck():
    print_skulls()
    print(" YOU ARE LUCKY!")

def print_no_luck():
    print_skulls()
    print(" NO LUCK THIS TIME! ")
