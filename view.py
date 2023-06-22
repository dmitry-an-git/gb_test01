from presenter import Presenter

def start():

    presenter = Presenter()
    global continue_loop 
    continue_loop = True

    print('*** Super app for notes 1.0 ***\n')

    def stop_loop():
        global continue_loop
        continue_loop = False
        print("Good bye!")

    while continue_loop:
        print('1: Create note')
        print('2: Modify note')
        print('3: Remove note')
        print('4: Display note')
        print('5: Print all notes')
        print('6: Search notes by date')
        print('7: Quit')
        choice = input('Choose an action: ')
        if choice == '1':
            presenter.create()
        elif choice == '2':
            presenter.modify()
        elif choice == '3':
            presenter.remove()
        elif choice == '4':
            presenter.display()
        elif choice == '5':
            presenter.print_all()
        elif choice == '6':
            presenter.search_by_date()
        elif choice == '7':
            stop_loop()