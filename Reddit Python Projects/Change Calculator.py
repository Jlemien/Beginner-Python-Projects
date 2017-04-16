#http://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/

while True:
    try:
        Input_amount = float(input("Please enter the amount of dollars and cents you have (e.g: 7.43): "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
    
Input_amount = Input_amount * 10
given_list_of_money = {"quarters": 25, "dimes": 10, "nickels": 5, "pennies": 1}
result_list_of_money = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}

for coin_type in given_list_of_money:
    result_list_of_money[coin_type] = int(Input_amount / given_list_of_money[coin_type])
    Input_amount = (Input_amount % given_list_of_money[coin_type])

print(result_list_of_money)

