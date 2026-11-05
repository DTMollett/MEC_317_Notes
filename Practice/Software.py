components = ["Motor" , "Sensor" , "relay" , "potentiometer" , 
"motor", "photoresistor"]
for component in components:
    print(component)
 

for component in components:
    print(f"A {component} is a common part in mechatronic systems.")
 

foods = ["pizza", "tacos", "sushi", "burgers", "pasta", "ramen"]
print(f"I could eat {foods[0]} every Friday night.")
print(f"{foods[1].title()} are best with extra salsa.")
print(f"Fresh {foods[2]} is worth the splurge.")
print(f"A good {foods[3][:-1]} needs a toasted bun.")
print(f"Homemade {foods[4]} reminds me of family dinners.")
print(f"On a cold day, nothing beats hot {foods[5]}.")
 
foods.append("waffles")
print(foods)
 
foods.remove("burgers")
print(foods)
 
popped_food = foods.pop()
print(f"Popped: {popped_food}")
print(foods)
 
print(f"Sorry {popped_food}, you're too good to leave out. Welcome back!")
foods.append(popped_food)
print(foods)
 
del foods[:]
 
print(foods)
 
cars = ["Toyota", "Ford", "Subaru", "Honda", "Tesla", "BMW"]

print(cars)
 
print(sorted(cars))
 
print(cars)
 
print(sorted(cars, reverse=True))
 
print(cars)
 
cars.reverse()
print(cars)
 
cars.reverse()
print(cars)
 
cars.sort()
print(cars)
 
cars.sort(reverse=True)
print(cars)