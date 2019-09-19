#from request_parser import print_current_price
import request_parser as pars
import urls_manage as manage
import database_manager as db_manager
ans=True
while ans:
    print("""
    1.Add Product
    2.Print All
    3.Delete Product
    4.Print Current Price
    5.Create DataBase
    6.Exit/Quit
    7.Exit/Quit
    """)
    ans=input("What would you like to do?")
    
    if ans=="1":
        print("\nAdd Product")
        new_address=input("Input a new web site") 
        manage.add_url(new_address)
    elif ans=="2":
        print("\nProduct List")
        manage.print_all()
    elif ans=="3":
        print("\nDelete Product")
        indextodel=input("Input index to delete :")
        manage.delete_url(indextodel)
    elif ans=="4":
        print("\nPrint current price and update db\n")
        pars.print_current_price()
    elif ans=="5":
        print("\nCreate DataBase") 
        db_manager.create_database()
    elif ans=="6":
        print("\nGoodbye") 
        ans = None
    elif ans=="7":
        print("\nGoodbye") 
        ans = None
    else:
        print("\nNot Valid Choice Try again")     
        ans = True