from random import randrange
import datetime


class AbstractMelonOrder(object):
    """Abtract melon order class"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False


    def get_base_price(self):
        """Gets current day and hour and based on that, calculates base price"""
        
        day = datetime.datetime.today().weekday()
        hour = datetime.datetime.today().hour

        base_price = randrange(5,10)

        if day < 5 and (7 < hour < 12):
            base_price += 4


        return base_price


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas_melons":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shid to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08   
        
        
    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code): 
        super(InternationalMelonOrder, self).__init__(species, qty)

        self.country_code = country_code

        
      
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government (in the US) melon order."""

    order_type = "domestic"
    tax = 0 

    def mark_inspection(self, passed):
        """Set pass inspection to passed"""

        self.passed_inspection = passed

