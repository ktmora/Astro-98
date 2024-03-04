#problem 2
percentages = [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
max_score = 300

scores = [int(percent * max_score) for percent in percentages]

print('Scores corresponding to the given percentages, on a scale out of 300:')
print(scores)

#problem 3
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient #changed from indexing to just patient inside list patients, that way each [] in patients is run thru
    bmi = calculate_bmi(weight, height) #fixed the order of weight, height. it was switched before which would cause all #s to flip
    print(f"Patient's BMI is: {bmi}")

#problem 4


total = 0
def cart_cost(cart_items, item_prices):
    cart_items = ['apple', 'banana', 'orange', 'milk']
    item_prices = [1.2, 0.9, 1.0, 2.5]
    discounts = {'apple': 0.1, 'banana': 0.05}
    for i in range(len(cart_items)): #len function gives each item a number, and the range function assigns the numbers
        if cart_items[i] in discounts.keys(): #why is it discounts.keys and not just discounts
            total += (1-discounts[cart_items[i]])*item_prices[i]
    else:
        total += item_prices[i] #dunno what's going on here. watch the lectures!
print(total)