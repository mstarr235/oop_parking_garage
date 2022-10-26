class Garage():
    '''
        The Garage class will have tickets, parking spaces list, 
        an empty spaces taken list, and a paid tickets dictionary with 
        a key of paid and value of False.  You shall be able to move 
        back and forth between the menus if you have entered the wrong
        main menu response.

        Attributes for the class:
        - tickets: expected to be an integer
        - parking_spaces: the amount of spaces must be equivalent to your
                            integer for tickets.
        - spaces_taken: is an empty list for you to move spaces that are
                        filled while the program is running.
        - paid_tickets: expected to be a dictionary, with a key of paid
                        and a value set to a Boolean type False.
    '''
    def __init__(self):
        self.tickets = 5
        self.parking_spaces = ['A2', 'B2', 'C2', 'D2', 'E2']
        self.spaces_taken = []
        self.paid_tickets = {'paid' : False}
    
    def showSpaces(self):
        print(f'\nThere are {len(self.parking_spaces)} parking spots available')

    def showTickets(self):
        print(f'\nThere are {self.tickets} tickets available')

    def takeTicket(self):
        if self.parking_spaces == []:
            print(f'\nSorry, we have {self.tickets} available at this time.')
        else:
            self.tickets -= 1
            spot_taken = self.parking_spaces.pop(0)
            self.spaces_taken.append(spot_taken)
            print(f'\nProceed to a parking space')
            print(f'\nThere are {self.tickets} tickets available, and {len(self.parking_spaces)} parking spaces remaining.')

    def payForParking(self):
        
        payment = input('\nWould you like to pay for parking? "Yes/No/Back": ')
        if payment.lower() == 'back':
            print('Returning to main menu...')
        elif payment.lower() == 'yes':        
            self.paid_tickets['paid'] = True
            print('\nYour ticket for parking has been paid.'
            '\nYou have 15 minutes to leave the garage.')
        else:
            print('\nYou will have to pay at the gate when leaving')

    def leaveGarage(self):
        while True:
            if self.paid_tickets['paid'] == False:
                gate_payment = input('\nTo exit, please pay for parking, "Yes/No/Back": ')
                if gate_payment.lower() == 'yes':
                    self.paid_tickets['paid'] = True
                elif gate_payment.lower() == 'back':
                    print('\nReturning to main menu...')
                    break  
                else:
                    print("\nYou will need to pay for your parking, before you can exit.")
            else:
                print('\nParking has been paid, Have a nice day!')
                self.tickets += 1
                new_spot = self.spaces_taken.pop(0)
                self.parking_spaces.append(new_spot)
                self.paid_tickets['paid'] = False
                break
    
    def paidForParking(self):
        if self.paid_tickets['paid'] == True:
            print(f'\nYou have already paid for parking.  You must leave the garage with 15 minutes.')

