class Jaeger(object):
    """
    a Jaeger starts with no equipment,
    but can equip and remove equipment
    """

    def equip(self, place, equipment):
        """ the jaeger equips the part at the place specified """
        pass

    def get_equipment(self, place):
        """ returns the equipment at the place if one exists, else None """
        pass

    def remove(self, part):
        """ removes the equipment at the place """
        pass


danger_gypsy = Jaeger()
danger_gypsy.equip("arm", "cannon")
danger_gypsy.equip("back", "boosters")

assert danger_gypsy.get_equipment("arm") == "cannon"
assert danger_gypsy.get_equipment("back") == "boosters"
assert danger_gypsy.get_equipment("legs") == None

danger_gypsy.remove("arm")
assert danger_gypsy.get_equipment("arm") == None
