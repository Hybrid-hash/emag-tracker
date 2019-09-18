#from request_parser import print_current_price
import request_parser as pars
import urls_manage as manage
ans=True
while ans:
    print("""
    1.Add Product
    2.Print All
    3.Delete Product
    4.Print Current Price
    5.Exit/Quit
    """)
    ans=input("What would you like to do?")
    
    if ans=="1":
        print("\nAdd Product")
        new_address=input("Input a new web site") 
        manage.add_url(new_address)
    elif ans=="2":
        manage.print_all()
    elif ans=="3":
        print("\nDelete Product")
        indextodel=input("Input index to delete :")
        manage.delete_url(indextodel)
    elif ans=="4":
        print("\nPrint current price\n")
        pars.print_current_price()
    elif ans=="5":
        print("\nGoodbye") 
        ans = None
    else:
        print("\nNot Valid Choice Try again")     
        ans = True