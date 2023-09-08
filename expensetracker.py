print("Welcome to the Expense tracker!")

#initializing categories
groceries = []
transport = []
entertainment = []
necessities = []
other = []
#askforcategories

categories = input("Which category for your first entry: Groceries, Transport, Entertainment, Necessities, Other?\nenter 'done' to finish\n")


while categories != "done":
    if categories.lower() == "groceries":
        print('Enter your grocery expenses, enter "0" when finished:')
        groceries_input = input(">")
        groceries.append(float(groceries_input))
        if groceries_input == "0":
            sum_groceries = round(sum(groceries),2)
            avg_groceries = round((sum(groceries))/((len(groceries))-1),2)
            msg = f'Total expense on groceries: ${sum_groceries}\nAverage expense on groceries: ${avg_groceries}'
            print(msg)
            break
    elif categories.lower() == "transport":
        print('Enter your transport expenses, enter "0" when finished:')
        transport_input = input(">")
        transport.append(float(transport_input))
        if transport_input == "0":
            sum_transport = round(sum(transport), 2)
            avg_transport = round((sum(transport)) / ((len(transport)) - 1), 2)
            msg1 = f'Total expense on groceries: ${sum_transport}\nAverage expense on groceries: ${avg_transport}'
            print(msg1)
            break
    elif categories.lower() == "entertainment":
        print('Enter your entertainment expenses, enter "0" when finished:')
        entertainment_input = input(">")
        entertainment.append(float(entertainment_input))
        if entertainment_input == "0":
            sum_entertainment = round(sum(entertainment), 2)
            avg_entertainment = round((sum(entertainment)) / ((len(entertainment)) - 1), 2)
            msg2 = f'Total expense on groceries: ${sum_entertainment}\nAverage expense on groceries: ${avg_entertainment}'
            print(msg2)
            break
    elif categories.lower() == "necessities":
        print('Enter your necessities expenses, enter "0" when finished:')
        necessities_input = input(">")
        necessities.append(float(necessities_input))
        if necessities_input == "0":
            sum_necessities = round(sum(necessities), 2)
            avg_necessities = round((sum(necessities)) / ((len(necessities)) - 1), 2)
            msg3 = f'Total expense on groceries: ${sum_necessities}\nAverage expense on groceries: ${avg_necessities}'
            print(msg3)
            break
    elif categories.lower() == "Other":
        print('Enter your other expenses, enter "0" when finished:')
        other_input = input(">")
        groceries.append(float(other_input))
        if other_input == "0":
            sum_other = round(sum(other), 2)
            avg_other = round((sum(other)) / ((len(other)) - 1), 2)
            msg4 = f'Total expense on groceries: ${sum_other}\nAverage expense on groceries: ${avg_other}'
            print(msg4)
            break
    else:
        print("Sorry, I do not understand. Please type in 'groceries', 'transport', 'entertainment','necessities', or 'other'")
        break

