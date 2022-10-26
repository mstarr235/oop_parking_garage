from parking_garage import Garage

my_garage = Garage()

def run():
    while True:
        response = input('\nWelcome to The Parking Garage.'
                            '\n\nWhat would you like to do?'
                            '\nEnter "Show", for How many spaces are available'
                            '\nEnter "Take", for Take a ticket,'
                            '\nEnter "Pay", Pay for parking,'
                            '\nEnter "Leave", To leave garage"'
                            '\n or "Quit": ')
        if response.lower() == 'quit':
            print('\nThank You!  Have a nice day!')
            break
        elif response.lower() == 'show':
            my_garage.showSpaces()
            my_garage.showTickets()
        elif response.lower() == 'take':
            my_garage.takeTicket()
        elif response.lower() == 'pay':
            if my_garage.paid_tickets['paid'] == False:
                my_garage.payForParking()
            else:
                my_garage.paidForParking()
        elif response.lower() == 'leave':
            my_garage.leaveGarage()
        
        else:
            print('\nPlease enter a valid input. Show/Take/Pay/Leave or Quit')

run()


        
