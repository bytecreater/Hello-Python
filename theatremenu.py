
# Theatre Application
menu={"pizza":200,
"chips":30,"wet corn":70,
"popcorn":500,"soda":100,
"samosa":70}
cart=[] 
total=0
print("--------MENU--------")
for keys, values in menu.items():
    print(f"{keys:10}: ${values:.2f}")
print("--------------------")    
while True:
    order=input("Enter your order(press q to quit):").lower()
    if order=="q":
        break
    elif menu.get(order) is not None:
            cart.append(order)
print("------------------")    
for order in cart:
    total=total+menu.get(order)
    print(f"{order:8}"+":$"+str(f"{menu.get(order):.2f}"))
print("------------------")        
print(f"Total   :${total:.2f}")
print("****Thank You****")
    