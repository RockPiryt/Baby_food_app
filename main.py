import pandas
from baby_info import Baby
from milk_info import ModifiedMilk



#BABY INFORMATION
baby_days = int(input(f"Please type how many days has your baby: ")) 
baby_weight = int(input(f"Please type in how much your child weighed at birth in gram: ")) 
user_baby = Baby(baby_days, baby_weight)

#CALCULATE CURRENT WEIGHT
current_weight = user_baby.calc_current_weight()

print(f"Estimate weight of your baby is {current_weight}g after {user_baby.day} days.")



#READ VALUE OF PORTION AND AMOUNT OF FEEDING DEPENDING ON DAY
data = pandas.read_csv("Modified_milk_data.csv")

#read  portion and amount of feeding using day input by user
actual_day = data[data["Time"] == user_baby.day]

portion = actual_day.Portion.item()
feeding = actual_day.Feeding.item()

modified_milk_portion = ModifiedMilk(portion, feeding)
total_mod_milk = modified_milk_portion.calc_total_milk()


#SHOW INFORMATION ABOUT FEEDING
print(f"On the {user_baby.day}th day a single portion is {portion}ml per 1 feeding.")
print(f'Your baby should eat {feeding} times in this day.')
print(f'Total amount of modified milk in this day is: {total_mod_milk} ml')