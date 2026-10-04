
# Requiere name: 
def require_name():
    while True:
        # Require name of the user 
        name = input("Enter your name: ").strip()
        
        # Validate 
        if not name:
            print("Name empty, insert it: ")
        else:
            return name.capitalize()  

# Requiere age:
def require_age():
    while True:
        # Requiere a valid age
        try:
            age = int(input("Enter your age: "))
            if age <= 0 or age > 100:
                print("Insert a valid age: ")
            else:
                return age
        except ValueError:
            print("Only numbers")  
            
# Requiere phone number
def require_number():
    # Requiere for phone number
    while True:
        try:
            phone_number = input("Enter your phone number: ")
            if len(phone_number) != 10:
                print("Invalid phone number")
            else:
                return phone_number    
            
        except ValueError:
            print("Only numbers") 

# Id of the user
def register_id():
    while True:
        try:
            identity = input("Enter your id: ")
            if len(identity) != 10:
                print("Id must have at least 10 digist")
            else:
                return identity     
        except ValueError:
            print("Only numbers")    
                            
# Create client or user
def create_user():
    # Save name and age of the user
    name_first = require_name()
    age_first = require_age()
    phone_first = require_number()
    id_first = register_id()
    
    client = {
        "name_first": name_first,
        "age_first": age_first,
        "phone_first": phone_first,
        "id_first": id_first
    }
    return client
    
# Menu 
print("\n = = = M E N U = = = ") 
# Empty list 
clients = []

while True:
    try:
        print("1) Register user ")
        print("2) Show clients ")
        print("3) Search client (Use id)")
        print("4) Exit ")
        choice = int(input("Select an option: ( 1 - 4 ) "))
        # Use if or match in this case
        match choice:
            case 1:
                # Register a client
                client = create_user()
                clients.append(client)
                print("✅Cliente registrado exitosamente.")
        
            case 2:
                # Validation 
                if not clients:
                    print("There aren't clients to show ")
                else:
                    for client in clients:
                        print(f"Name: {client['name_first']} | Age: {client['age_first']} | Phone Number: {client['phone_first']} | Id: {client['id_first']}")
                        
            case 3:
                try:
                    found = False
                    search_id = input("Insert id to look for ")
                    for i in clients:
                        if i['id_first'] == search_id:
                            print("Client exist: ✅" )
                            found = True
                            break
                        
                    if not found:
                        print("Client does not exist")    
                            
                except ValueError:
                    print("Insert only numbers")            
                              
            case 4:
                # Exit 
                print("Exiting of the program...")
                break
                        
            case _:
                # If the option is invalid 
                print("Invalid option")
                
    except ValueError:
        print("Insert valid inputs please: ")                      
    
    
                 