# the child class PredatoryCreditCard will differ from the parent class CreditCard in two ways:
# If an attempted charge is rejected because it would have exceeded the credit limit,
#  a $5 fee will be charged, and
# There will be a mechanism for assessing a monthly interest charge on the outstanding balance, 
# based upon an Annual Percentage Rate (APR) specified as a constructor parameter.

# Based on the information and requirements provided above, 
# create another python file (e.g. predatory_credit_card.py) 
# and enter your implementation of the PredatoryCreditCard class.

# HINTS:
# • To charge a fee for an invalid charge attempt, you will need to override the existing charge method, thereby specializing it to provide the new functionality.
# • To provide support for charging interest (based on the APR), you will need to extend the class with a new method named process_month.
# • To translate an APR to a monthly rate, take the twelfth-root of (1 + self._apr), and use that as a multiplicative factor. E.g., if the APR is
# 12
# 0.0825 (representing 8.25%), compute √1.0825 ≈ 1.006628, and therefore
# charge 0.6628% interest per month. In this way, each $100 debt will amass $8.25 of compounded interest in a year. For this computation, you may need to use the built-in pow() function.
# The PredatoryCreditCard class provides a process_month method that models the completion of a monthly cycle. 
# Modify the class so that once a customer has made ten calls to charge in the current month,
#  each additional call to that function results in an additional $1 surcharge.
# (HINT: The key is being able to accurately track how many times charge has been called thus far during a month.)

from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and
    fees."""
    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance. """
        super().__init__(customer, bank, acnt, limit) # inherited from CreditCard class use super(). to inherit
        self._apr = apr #annual precentage rate 
        self._charge_count = 0

    def get_apr(self):
        """Return the annual percentage rate (APR) for this card."""
        return self._apr
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit
            limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        self._charge_count += 1
        if self._charge_count > 10:
            print('after 10 transaction $1 charged')
            self._balance += 1
        success = super().charge(price)
        if not success:
            print('$5 penalty charged')
            self._balance += 5
        return success
    
    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        self._charge_count=0
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

# Testing the CreditCard class
if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Lee', 'DBS','5391 0375 9387 5309', 2000, 0.15))
    count = 0
    for val in range(1, 17): 
        
        wallet[0].charge(200)
        print('transaction number',val)
        print(':Charge $200 Balance =',wallet[0].get_balance())


    print('Customer =', wallet[0].get_customer()) 
    print('Bank =', wallet[0].get_bank()) 
    print('Account =', wallet[0].get_account()) 
    print('Limit =', wallet[0].get_limit()) 
    print('Balance =', wallet[0].get_balance()) 
    while wallet[0].get_balance() > 100:
        wallet[0].make_payment(100)
        print('New balance =', wallet[0].get_balance())
    
    for val in range(1, 17): 
        wallet[0].charge(200)
        print('transaction number',val)
        print(':Charge $200 Balance =',wallet[0].get_balance()) 
    
    wallet[0].process_month()

    print('After process month =', wallet[0].get_balance())

    print()