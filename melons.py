class AbstractMelonOrder(object):
    """Abtract melon order class"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5

        if self.species == "Christmas_melons":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty): 
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)   
        
        
    

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code): 
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)  
        self.country_code = country_code
        
      
    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government (in the US) melon order."""

    def __init__(self, species, qty): 
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0) 


    def mark_inspection(self, passed):
        """Set pass inspection to passed"""

        self.passed_inspection = passed

