weight = 41.5

# Ground Shipping 

if weight <= 2:
   ground_ship_cost = weight * 1.5 + 20
elif weight >2 and weight <= 6:
  ground_ship_cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  ground_ship_cost = weight * 4.00 + 20.00
elif weight > 10:
  ground_ship_cost = weight * 4.75 + 20.00
elif weight == 8.4:
  ground_ship_cost = weight * 4.00 + 20.00
  
print("Ground Cost Shippin $:", ground_ship_cost)

# Ground Shipping Premium
ground_premium_ship = 125
print("Ground Shipping Premium $:", ground_premium_ship)

# Drone Shipping

weight = 80

if weight <= 2:
  drone_ship_cost = weight * 4.50 + 0.00
elif weight > 2 and weight <= 6:
  drone_ship_cost = weight * 9.00 + 0.00
elif weight > 6 and weight <= 10:
  drone_ship_cost = weight * 12.00 + 0.00
elif weight > 10:
  drone_ship_cost = weight * 14.25 + 0.00
elif weight == 1.5:
  drone_ship_cost = weight * 4.50 + 0.00 
print("Drone Shopping cost $:", drone_ship_cost)


