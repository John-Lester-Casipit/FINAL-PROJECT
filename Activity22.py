#Name listing and then count names

tuloy = True
pangalan = []
while tuloy == True:
    name = input('What name would you like to add?(type "stop" to terminate the loop) ')
    if name.lower() == "stop":
        print(pangalan)
        print(f"You have entered {len(pangalan)} names! ")
        break
    else:
        pangalan.append(name)