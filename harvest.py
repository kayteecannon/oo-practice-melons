############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        """Initialize a melon."""
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.pairings = [] 


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')

    cas = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    cas.add_pairing('strawberries') 
    cas.add_pairing('mint')

    cren = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    cren.add_pairing('proscuitto')

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')

    all_melon_types = [musk, cas, cren, yw]
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with:')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print('\n')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_code_dict = {}

    for melon in melon_types:
        if melon not in melon_code_dict:
            melon_code_dict[str(melon.code)] = melon

    return melon_code_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by= harvested_by

    def is_sellable(self):

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_code = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_code['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_code['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_code['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_code['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_code['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_code['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_code['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_code['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_code['yw'], 7, 10, 3, 'Michael')

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return melons
    

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



