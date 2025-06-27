# switch case

def switch_case(argument):
    switcher = {
        1: "One",
        2: "Two",
        3: "Three",
    }
    return switcher.get(argument, "Invalid argument")

print(switch_case(1))
print(switch_case(2))

