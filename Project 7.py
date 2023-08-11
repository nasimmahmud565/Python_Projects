Contact = {}

def ShowFunction():
    print(Contact.items())
    print('Name \t Contact')
    for key in Contact:
        print('{} \t {}'.format(key,Contact.get(key)))

while True:
    choice = int(input('1. Add New Contact \n'
                   '2. Search the Contact \n'
                   '3. Dispaly the Contact \n'
                   '4. Edit teh Contact \n'
                   '5. Delete the Contact \n'
                   '6. Exit \n'
                   'Please Write Number Between 1-6: '))

    if choice == 1:
        name = input('Add your Contact name: ')
        phone = input('Add your Phone number: ')
        Contact[name] = phone

    elif choice == 2:
        ContactName = input('Search the Contact: ')
        if ContactName in Contact:
            print(ContactName, 'contact number is ', Contact[ContactName])
        else:
            print('Not Found the Contact')

    elif choice == 3:
        if not contact:
            print('contact book is empty')
        else:
            ShowFunction()

    elif choice == 4:
        EditContact = input('Edit your Contact: ')
        if EditContact in Contact:
            phone = input(('Change your number: '))
            Contact[EditContact] = phone
            print('Contact updated successfully')
            ShowFunction()
        else:
            print('Name is not Found')

    elif choice == 5:
        Del_Contact = input('which Contact do you want to delete?: ')
        if Del_Contact in Contact:
            DeletedConfirm = input('do you want to delete this Contact y/n')
            if DeleteConfirm == 'y' or DeleteConfirm == 'y':
                Contact.pop(Del_Contact)
            ShowFuntion()
        else:
            print('the name is not found in the Contact')


    else:
        break
