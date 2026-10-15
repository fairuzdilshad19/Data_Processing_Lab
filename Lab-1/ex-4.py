name=input("Passenger Name: ")
destination=input("Destination: ")
ticket_count=int(input("Number of Tickets: "))
passenger_type=input("Passenger Type (child/student/senior/adult): ")

if destination=="Dhaka":
    fare=500
elif destination=="Chittagong":
    fare=800
elif destination=="Sylhet":
    fare=700
else:
    fare=1000

if passenger_type=="child":
    discount=0.50
elif passenger_type=="student":
    discount=0.20
elif passenger_type=="senior":
    discount=0.30
else:
    discount=0

total=fare*ticket_count
discount_amount=total*discount
final_fare=total-discount_amount

print("\n TRAIN TICKET ")
print("Passenger:",name)
print("Destination:",destination)
print("Passenger Type:",passenger_type)
print("Tickets:",ticket_count)
print("Fare per ticket:",fare)
print("Discount:",discount_amount)
print("Total Fare:",final_fare)
