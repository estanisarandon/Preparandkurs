
def print_menu():
    print("menu")
    print("===============")
    print ("1. först prylen")
    print ("2. andra prylen")
    print ("3. tredje prylen")
    print ("4. avsluta")
    selection = input("Ange ditt val: ")
    return selection

def do_selection():
    if selection == "1":
        print("Du valde det första valet")
    elif selection == "2":
        print("Du gjorde det andra valet")
    elif selection == "3":
        print("Du gjorde det tredje valet")
    else:
        print("Tack och hej då")

selection = print_menu()
do_selection()
