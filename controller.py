#Денис
import string
import operations as o
import user_interface as ui


def button_click():
     ui.greetings_user()
     while True:
       menu = ui.show_menu()
       choice = ui.get_choice(menu)
       if choice == 1:
            list = ui.get_contact   
            o.write_csv()
            o.write_json()
       elif choice == 2:
            lst = o.read_csv()
            result = o.search_contact(lst)
            ui.view_data(result)
          #   while True:
          #        menu_s = ui.menu_search()
          #        choice = ui.get_choice(menu_s)
          #        if choice == 1:
          #             o.edit_contact(ui.edit_user_contact(result[0]))
          #             list = ui.get_contact   
          #             o.write_csv()
          #             o.write_json()
          #        elif choice == 2:
          #             o.delete_contact(result)
          #             ui.delete_user_contact(result)
          #        else:
          #             break                   
       elif choice == 3:
            result = o.read_csv()
            ui.view_data(result)
       elif choice == 4:
            o.write_json()
       else:
            ui.farewell_user()
            break
