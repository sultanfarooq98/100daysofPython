#python Day 02

print("Welcome to the split calculator.")

bill = float(input("What was the total bill : "))
per = int(input("What percentage tax : "))

intax = (1 + per / 100) * bill
print(intax)

p = int(input("How many people to split bill : "))
result = intax/p
split = print("Each person should pay : ", result)
total_round_amount = round(split)
print(total_round_amount)