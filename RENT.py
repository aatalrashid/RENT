#this is a rent system::

class Rent:
    def __init__(self, House_No, Occupant_Name, Date_of_payment, Amount_payed):

        self.House_No = House_No
        self.Occupant_Name = Occupant_Name
        self.Date_of_payment = Date_of_payment
        self.Amount_payed = Amount_payed

        print()
        print("RECEIPT:")
        print('On {2} {1} paid {3}shs for house number {0}.'
              .format(self.House_No,
                      self.Occupant_Name,
                      self.Date_of_payment,
                      self.Amount_payed)
              )

        print()
        print("       Thanks for your cooperation. MGT")

c = Rent(
         int(input("Enter the House_No: ")),
         input("Enter the Occupant_Name: "),
         input("Enter the Date_of_payment: "),
         input("Enter the Amount_Payed: ")
        )




