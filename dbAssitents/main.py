from config.dbconnect import conn

def run():
    while True:
        print("Welcome to the AI Database assistant!")
        print("Choice from the following options:")
        print("1. Natural Language Query :- nlq")
        print("2. Schema Query :- schema")
        print("3. Data search Query :- search")
        print("4. Data analysis Query :- analysis")
        print("5. Export data :- export")
        print("6. Generate report :- report")
        print("7. Exit :- exit")
        print("Please enter your choice:")
        choice = input("Enter your choice: ")
        if choice == 'nlq':
            print("You have selected Natural Language Query.")
            # Call the function to handle natural language queries
        elif choice == 'schema':
            print("You have selected Schema Query.")
            # Call the function to handle schema queries
        elif choice == 'search':
            print("You have selected Data search Query.")
            # Call the function to handle data search queries
        elif choice == 'analysis':
            print("You have selected Data analysis Query.")
            # Call the function to handle data analysis queries
        elif choice == 'export':
            print("You have selected Export data.")
            # Call the function to handle data export
        elif choice == 'report':
            print("You have selected Generate report.")
            # Call the function to handle report generation
        elif choice == 'exit':
            break
        print("Type 'exit' to quit the program.")
        query = input("What is your query ?")
        if query.lower() == 'exit':
            break

if __name__ == "__main__":
    run()
    conn.close()
