import unicodedata

def print_skulls():
    print("\n\n"+ (unicodedata.lookup("skull") + " ") * 30 + "\n\n")

def print_error_message():
    print_skulls()
    print(" FATAL ERROR ")
    print_skulls()
