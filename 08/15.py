class Car(object):
    """
    Represents a car, with information about
    when it needs on oil change.

    each car has a unique oil change requirement:
    the # of miles until an oil change is reccomended.
    """
    def __init__(self, reccomended_oil_change_miles):
        """
        reccomended_oil_change_miles is the # of
        miles the car should be driven before an oil
        change is necessary.
        """
        pass

    def drive(self, miles):
        """ drive the car x miles """
        pass

    def needs_oil_change(self):
        """
        returns true if this care needs an oil change.
        """
        pass

    def change_oil(self):
        """
        changes the oil, resetting the miles until oil change back
        to 3000
        """

honda = Car(3000)  # 3000 miles reccommended between oil changes.
honda.drive(500)
assert honda.needs_oil_change() is False
honda.drive(3000)
assert honda.needs_oil_change() is True
honda.change_oil()
assert honda.needs_oil_change() is False
honda.drive(2500)
assert honda.needs_oil_change() is False
honda.drive(500)
assert honda.needs_oil_change() is True
honda.change_oil()
honda.drive(3100)
assert honda.needs_oil_change() is True
