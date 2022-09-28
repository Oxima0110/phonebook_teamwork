import operations as o
import user_interface as ui


def button_click():
     ui.greetings_user()
     while True:
       menu = ui.show_menu()
       choice = ui.get_choice(menu)
       if choice == 1:  
            o.write_csv()
      
       
       elif choice == 2:
            lst = o.read_csv()
            result = o.search(lst)
            ui.view_data(result)
            
       elif choice == 3:
            result = o.read_csv()
            ui.view_data(result)
            
       elif choice == 4:
            o.write_json()
          
       else:
            ui.farewell_user()
            break
