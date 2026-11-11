how_many = int(input("how many appliances? "))
total_kwh = 0

appliance_energy = []
for i in range(how_many):


    # ask for machine details
    power = float(input("enter power in watts: "))
    hours = float(input("hours used per day: "))
    total_kwh = total_kwh + (power / 1000) * hours
    appliance_energy.append((power / 1000) * hours)


# daily energy in kWh



def monthly_energy(energy_list):
    return sum(energy_list) * 30
print("daily energy:", total_kwh, "kwh")
tariff = float(input("cost per kWh (naira): "))
cost = total_kwh * tariff
print("daily cost: N", cost)
print("monthly energy:", monthly_energy(appliance_energy), "kwh")
print("monthly cost: N", cost * 30)
budget = float(input("enter ur monthly budget (naira): "))
if cost * 30 > budget:
	print("warning: u are above ur monthly budget")
else:
	print("u are within ur monthly budget")