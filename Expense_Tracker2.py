class Ex_Tracker:

        def add_expense(self):
            try:
                amount = float(input("Enter the amount: "))
            except ValueError:
                print("Invalid input ! ")
                return   # important fix

            category = input("Enter the category: ")
            date = input("Enter the date (DD-MM-YYYY): ")

            with open("csk.txt", "a") as file:
                file.write(f"{amount},{category},{date}\n")

            print("Expense Added Successfully\n")
            print()

        def view_expense(self):
            try:
                with open("csk.txt", "r") as file:
                    print("\n--- All Expenses ---")
                    for line in file:
                        amount, category, date = line.strip().split(",")
                        print(f"{date:<12} | {category:<12} | ₹{amount}")
            except FileNotFoundError:
                print("No Expenses found!\n")
            print()

        def total_expense(self):
            total = 0
            try:
                with open("csk.txt", "r") as file:
                    
                    for line in file:
                        try:
                            amount, _, _ = line.strip().split(",")
                            total += float(amount)
                        except:
                            continue
                print(f"\nTotal Expense: ₹{total}\n")

            except FileNotFoundError:
                print("File not found\n")
            print()

        # 🔥 NEW FUNCTION
        def category_total(self):
            totals = {}

            try:
                with open("csk.txt", "r") as file:
                    for line in file:
                        amount, category, _ = line.strip().split(",")
                        amount = float(amount)

                        if category in totals:
                            totals[category] += amount
                        else:
                            totals[category] = amount

                print("\n--- Category Wise Total ---")
                print("_________________________________")
                for cat, amt in totals.items():
                    print(f"{cat:<12}: ₹{amt}")

            except FileNotFoundError:
                print("No data found\n")
            print()

    # object create
obj = Ex_Tracker()

    # menu
while True:
        print("\n=========Expense Tracker==========")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Category Wise Total")   # 👈 new
        print("5. Exit")
        print("=============================")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            obj.add_expense()

        elif choice == "2":
            obj.view_expense()

        elif choice == "3":
            obj.total_expense()

        elif choice == "4":
            obj.category_total()   # 👈 call

        elif choice == "5":
            break

        else:
            print("Invalid choice\n")