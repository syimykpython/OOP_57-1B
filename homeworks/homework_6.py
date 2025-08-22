from blessed import Terminal

term = Terminal()

fruict = {
    "apple": term.red,
    "orange": term.darkorange,
    "banana": term.yellow,
    "grape": term.purple,
    "mango": term.orange,
    "peach": term.green,
    "cherry": term.pink,
}

for fruict, color in fruict.items():
    print(color + fruict + term.normal)