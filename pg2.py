
# class ParkingGarage:
#     def __init__(self):
#         self.tickets = []
#         self.parking_spaces = []
#         self.current_ticket = {}
#         self.return_tickets = {}
        
    
#     def take_ticket(self):
#         if len(self.tickets) > 0 and len(self.parking_spaces) > 0:
#             self.tickets.pop(0) 
#             self.parking_spaces.pop(0)
#             self.current_ticket = {"paid": False} 
#             print("Please take your ticket.")
#         else:
#             print("Sorry, the parking garage is full.") 

#     def pay_parking(self):
#         if self.current_ticket:
#             payment = input("Please enter your payment amount: ")
#             if payment:
#                 self.current_ticket["paid"] = True
#                 print("Your ticket has been paid. You have 90 minutes to leave")
#         else:
#             print("You do not have a current ticket.")

#     def leave_garage(self):
#         if self.current_ticket and self.current_ticket["paid"]:
#             print("Thank you, have a nice day!")
#             self.parking_spaces.append("empty")
#             self.tickets.append("available")
#             self.current_ticket = {}
#         else:
#             payment = input("Pay your parking fee: ")
#             if payment:
#                 self.current_ticket["paid"] = True
#                 print("Thank you, have a nice day!")
#                 self.parking_spaces.append("empty")
#                 self.tickets.append("available")
#                 self.current_ticket = {}
#             else:
#                 print("You must pay your parking fee before leaving.")

#     def validate_ticket(self, ticket):
#         return ticket in self.tickets and self.tickets[ticket]["paid"]
    
#     def return_ticket(self, ticket):
#         if self.validate_ticket(ticket):
#             self.validate_ticket(ticket)
#             self.parking_spaces.append("empty")
#             self.current_ticket = {}
#         else:
#             print("Invalid ticket.")
            

    
# ParkingGarage = ParkingGarage()
# ParkingGarage.take_ticket()

# ParkingGarage.pay_parking()

# ParkingGarage.leave_garage()



# Team work makes dream work


class Parking():

    def __init__(self, tickets, available_spots):
        self.tickets = tickets
        self.available_spots = available_spots

    def current_ticket(self):
        if self.tickets <= 0:
            print("This parking garage is full, come back in an hour")
            if self.tickets <0:
                print(f" Get a ticket {abs(self.tickets)}, thank you!")
                self.tickets = 0

        else:
            cars = int(input("how many parkings spots you need?"))
            self.tickets -= cars
            if self.tickets < 0:
                print(f"Change_later {abs(self.tickets)}also_change")
                self.tickets = 0
                print(f"{cars}cars have parked. There are {self.tickets} available in the garage!")

    def leave_spot (self):
        if self.tickets >= self.available_spots:
            print ("There is no self parking avaialable")
        else: 
            leave = int(input("How many cars are leaving the garage?"))
            self.tickets += leave
            if self.tickets >= self.available_spots:
                self.tickets = self.available_spots

            print(f"{leave} cars left the garage. There are {self.tickets} left")

   # Calling part 

   
    def run():
       team_garage = Parking( 45,45 )
    
    while True:
        response = input("What would you like to do? Get a ticket/leave the garage/Quit?")
        if response.lower() == "quit":
            print("Thank you for your time!")
            break

        elif response.lower() == 'Get a ticket':
            team_garage.current_tickets()
            
        elif response.lower() == "leave the garage":
            team_garage.leave_spot()
        
            
        else:
            print("That is not a valid response. Please pick from the list!")
            
    run()
    