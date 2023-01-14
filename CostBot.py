# Welcome
print ("💰💰💰💰💰💰💰💰💰")
print ("Hello! I am CostBot!")
your_name = input ("What's your name? ")
print ("Welcome " + str(your_name) + ", let me help you calculate your weekly expenses!")

# Survey of costs
print ("Please share what expenses you had this week! Type in the sum you spent in Euros. If you didn't have any expenses in a category, type 0.")
print ("💰💰💰")
input_food = input ("How much did you pay for food or beverages this week? ")
input_clothes = input ("How much did you pay for clothes or shoes this week? ")
input_toiletries = input ("How much did you pay for drugstore items this week? ")
input_medicaments = input ("How much did you pay for medicaments this week? ")
input_household = input ("How much did you pay for household items this week? ")
input_transport = input ("How much did you pay for tickets for public transport this week? ")
input_fuel = input ("How much did you pay for fuel this week? ")
input_repairs = input ("How much did you pay for repairs this week? ")
input_freetime = input ("How much did you pay for free-time activities, e.g. theatre, cinema etc.? ")
input_misc = input ("Which other expenses did you have this week? ")

# Monthly costs
print ()
print ("Now we would like to know which monthly expenses you have to take them into account on a pro rata basis.")
print ()
input_house = input ("How much are your monthly expenses for rent? ")
input_electricity = input ("How much are your monthly expenses for electricity? ")
input_insurances = input ("How much did you pay for insurance? ")
input_phone = input ("How much did you pay for phone or internet? ")

# Adding costs
print ()
print ("Now we're going to add up your costs! ")
weekly_costs_house = int(input_house) / 4.38
weekly_costs_electricity = int(input_electricity) / 4.38
weekly_costs_insurances = int(input_insurances) / 4.38
weekly_costs_phone = int(input_phone) / 4.38
weekly_costs_pro_rata = round(weekly_costs_house + weekly_costs_electricity + weekly_costs_insurances + weekly_costs_phone, 2)
weekly_costs_general = int(input_clothes) + int(input_electricity) + int(input_food) + int(input_freetime) + int(input_fuel) + int(input_household) + int(input_medicaments) + int(input_misc) + int(input_repairs)
total_costs = round(weekly_costs_pro_rata + weekly_costs_general, 2)

# Result
print ("======================================================================================================")
print ("Your pro-rata weekly costs for rent, electricity, telephone, etc. are as follows: " + str(weekly_costs_pro_rata) + " Euros.")
print ("For other purposes you have spent " + str(weekly_costs_general) + " Euros this week. ")
print ("So, all in all your total expenses this week were: " + str(total_costs) + " Euros.")
print ("======================================================================================================")

# Your income
print ()
monthly_income = input ("Now let's compare your income with your expenses! How much is your monthly income in Euros? ")
weekly_income_pro_rata = round(int(monthly_income) / 4.38)
print ()
print ("Your pro rata weekly income is as follows " +str(weekly_income_pro_rata) + " Euros.")
print ()
if weekly_income_pro_rata < total_costs:
    print ("With " + str(weekly_income_pro_rata) + " Euros, your expenses were quite high this week. Please be careful not to spend more than you have in your account next week!")

# Saving money
print ("If you want to save some money, you should set aside a small amount regularly.")
print ("If your monthly income exceeds 2000 euros, it is recommended to save at least 7 percent of the income.")
saving_input = input ("What percentage of your income would you like to save? ")
saving_amount_month = round((int(monthly_income) / 100 * int(saving_input)), 2)
saving_amount_week = round((saving_amount_month / 4.38), 2)
print ()
print ("When you want to save " + str(saving_input) + " per cent of your income, you should save " + str(saving_amount_month) + " Euros a month or " + str(saving_amount_week) + " Euros a week.")
print ("I wish you a beautiful day. See you next week!")
