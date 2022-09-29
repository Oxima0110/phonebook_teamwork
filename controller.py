# Денис

import operations as o
import user_interface as ui


def button_click():
    ui.greetings_user()
    while True:
        menu = ui.show_menu()
        choice = ui.get_choice(menu)
        if choice == 1:
            contact = ui.add_contact()
            o.add_contact_csv(contact)
        elif choice == 2:
            searchstring = ui.get_action('Введите данные для поиска: ')
            searched_contact = o.search_contact(searchstring)
            ui.view_data(searched_contact)
            while True:
                    menu_s = ui.menu_search()
                    choice = ui.get_choice(menu_s)
                    if choice == 1:
                         ui.edit_user_contact(searchstring)
                         contact = ui.add_contact()
                         o.edit_contact(searchstring, contact)
                    elif choice == 2:
                         o.delete_contact(searchstring)
                         ui.delete_user_contact(searchstring)
                    else:
                         break
        elif choice == 3:
            result = o.read_csv()
            ui.view_data(result)

        elif choice == 4:
            o.write_json()

        else:
            ui.farewell_user()
            break
