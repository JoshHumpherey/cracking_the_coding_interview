# Cracking the Coding Interview: 7.2
# Written by Josh Humphrey

class Call_Center():

    director = ["Mr. CEO"]
    managers = ["Big Boy 1", "Big Boy 2", "Big Boy 3"]
    respondents = ["Wagie 1", "Wagie 2", "Wagie 3", "Wagie 4", "Wagie 5", "Wagie 6"]

    def __init__(self, name):
        self.name = name
        self.director = []
        self.managers = []
        self.respondents = []


        class director():

            def __init__(self, name, free):
                self.name = name
                self.free = free

        class managers():

            def __init__(self, name, free):
                self.name = name
                self.free = free

        class respondents():

            def __init__(self, name, free):
                self.name = name
                self.free = free

    def dispatch_call():
        for x in self.respondents:
            if x.free == True:
                x.free = False
                return
        for x in self.managers:
            if x.free == True:
                x.free = False
                return
        if self.director.free == True:
            self.director.free = False
            return

        return None
