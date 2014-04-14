__author__ = 'cooklee'


def get_method_form_class(classname, start_with='action'):
    names_of_functions = dir(classname)
    interested_function = []
    for name in names_of_functions:
        if name.startswith(start_with):
            interested_function.append(name)
    return interested_function


class Mind(object):

    def __init__(self, objects):
        self.options = [getattr(objects, x) for x in get_method_form_class(objects)]

    def decide(self):
        import random
        gen = random.randrange(len(self.options))
        self.options[gen]()

class Creature(object):

    def __init__(self, health=100.0):
        self.health = health
        self.live = 1
        self.mind = Mind(self)

    def check_status(self):
        if self.health <= 0:
            self.live = 0

    def action_move(self):
        print 'move'
        self.health -= 0.5
        self.check_status()

    def action_eat(self, portion=0.1):
        print 'eat'
        self.health += portion

    def action_nothing(self):
        print 'nothing'

    def think(self):
        self.mind.decide()


c = Creature()
c.think()