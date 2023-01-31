import random
response = "g"
while response == "g":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  x  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ x   ]")
        print("[     ]")
        print("[   x ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[x x x]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[x   x]")
        print("[     ]")
        print("[x   x]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[x   x]")
        print("[  x  ]")
        print("[x   x]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[x x x]")
        print("[     ]")
        print("[x x x]")
        print("[-----]")
    response=input("Pressione g para jogar novamente ou n para sair: ")
    print("\n")