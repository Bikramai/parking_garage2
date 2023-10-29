
class ParkingGarage:
    def __init__(self):
        self.tickets = []
        self.parking_spaces = []
        self.current_ticket = {}
        self.return_tickets = {}
        
    
    def take_ticket(self):
        if len(self.tickets) > 0 and len(self.parking_spaces) > 0:
            self.tickets.pop(0) 
            self.parking_spaces.pop(0)
            self.current_ticket = {"paid": False} 
            print("Please take your ticket.")
        else:
            print("Sorry, the parking garage is full.") 

    def pay_parking(self):
        if self.current_ticket:
            payment = input("Please enter your payment amount: ")
            if payment:
                self.current_ticket["paid"] = True
                print("Your ticket has been paid. You have 90 minutes to leave")
        else:
            print("You do not have a current ticket.")

    def leave_garage(self):
        if self.current_ticket and self.current_ticket["paid"]:
            print("Thank you, have a nice day!")
            self.parking_spaces.append("empty")
            self.tickets.append("available")
            self.current_ticket = {}
        else:
            payment = input("Pay your parking fee: ")
            if payment:
                self.current_ticket["paid"] = True
                print("Thank you, have a nice day!")
                self.parking_spaces.append("empty")
                self.tickets.append("available")
                self.current_ticket = {}
            else:
                print("You must pay your parking fee before leaving.")

    def validate_ticket(self, ticket):
        return ticket in self.tickets and self.tickets[ticket]["paid"]
    
    def return_ticket(self, ticket):
        if self.validate_ticket(ticket):
            self.validate_ticket(ticket)
            self.parking_spaces.append("empty")
            self.current_ticket = {}
        else:
            print("Invalid ticket.")
            

    
ParkingGarage = ParkingGarage()
ParkingGarage.take_ticket()

ParkingGarage.pay_parking()

ParkingGarage.leave_garage()

