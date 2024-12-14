def pang_hello():
    print("HELLO IT1C")
                
def pang_hello_V2(name):
    print(f"Hello {name}")
                
    tuloy = True
    while tuloy == True:
        ask = input("Please provide a name --> ")
        if ask.lower() != "stop":
            pang_hello_V2(ask)
        else:
            break
