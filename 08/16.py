class Fighter(object):
    """
    represent a fighter with the ability to perform specials.
    the special gauge increases as the fighter is hurt. one
    damage == increase the special gauge by one.
    """
    def __init__(self, life_points, max_special_gauge):
        """
        life_points (int): life points the fighter starts with

        max_special_guage (int): the maximum number of points in the
        special gauge. if maxed out, the fighter can perform their
        special.
        """
        pass

    def hurt(self, damage):
        """ hurts the fighter for x damage, and increases the special gauge by x """
        pass

    def is_dead(self):
        """ returns true if the fighter has 1 life point or less """
        pass

    def can_use_special(self):
        """ returns true if the fighter can use their special """
        pass

    def use_special(self):
        """ uses the fighter's special, depleting their special gauge. """
        pass


nightmare = Fighter(2000, 500)
nightmare.hurt(300)
assert nightmare.can_use_special() is False
nightmare.hurt(700)
assert nightmare.can_use_special() is True
nightmare.use_special()
assert nightmare.can_use_special() is False
nightmare.hurt(500)
assert nightmare.can_use_special() is True
assert nightmare.is_dead() is False
nightmare.hurt(1000)
assert nightmare.is_dead() is True
