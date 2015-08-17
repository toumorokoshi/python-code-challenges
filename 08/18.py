class Fighter(object):
    """
    this is a fighter for an RPG. they start
    with a specific hp, and can get damaged.
    """

    def __init__(self, name, starting_hp):
        """
        name (str): the name of the fighter.

        starting_hp (int): the starting hp of
        the fighter.
        """

    def damage(self, damage):
        """
        damage (int): the amount of damage to deal.

        reduces the hp of the fighter for <damage> amount. HP
        can not be negative: if more damage is dealt to bring the
        fighter below 0, hp should be 0
        """
        pass

    def get_hp(self):
        """
        returns the current hp of the fighter
        """

    def is_dead(self):
        """
        returns True if the fighter's hp is below 0, otherwise
        returns False
        """


class Party(object):

    def __init__(self, members):
        """
        members ([Fighter]): a list of fighters in the party.
        """

    def damage(self, member_name, damage):
        """
        member_name (str): the name of the party member to damage.
        damage (int): the amount of damage to deal.

        damages the member of the party with the name <member_name> for
        <damage> damage.
        """

    def get_hp(self, member_name):
        """
        member_name (str)

        returns the hp for the party member with name <member_name>
        """
        pass

    def is_party_dead(self):
        """
        returns True if all party memmbers are dead, else False
        """


cecil = Fighter("cecil", 100)
rosa = Fighter("rosa", 70)

party = Party([cecil, rosa])

assert party.get_hp("cecil") == 100
assert party.get_hp("rosa") == 70
party.damage("rosa", 30)
assert party.is_party_dead() is False
party.damage("rosa", 50)
assert party.is_party_dead() is False
# hp can't go below 0.
assert party.get_hp("rosa") == 0
assert party.damage("cecil", 30)
assert party.get_hp("cecil") == 70
party.damage("cecil", 100)
assert party.is_party_dead() is True
