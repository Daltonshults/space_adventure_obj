import random


class Controller:
    '''
    This class is responsible for the logic between the Interface and the ReadFile class.
    Receives an Interface and ReadFile object that are used within the run method.
    '''

    def __init__(self, interface, read_file):
        '''
        Recieves an Interface and a ReadFile that are passed into the constructor
        '''
        self.interface = interface
        self.read_file = read_file

    def run(self, path_to_file):
        '''
        A method that is responsible for running the program,
        and using the Interface, and ReadFile object that are
        passed into the constructor
        '''

        # Prints greeting
        self.interface.greeting()

        # Stores the returun of the read_json method from the ReadFile class into data returns a List
        data = self.read_file.read_json(path_to_file)

        # Ask the user if they want to visit a random planet, return a Boolean
        if_random = self.interface.want_random()

        # If the user does want a random planet
        if if_random == True:
            rand = random.randint(0, 8)
            self.interface.print_planet(rand, data)

        # If the user does not want a random planet
        elif if_random == False:

            # Ask the user what planet they want to go to.
            planet = self.interface.pick_a_planet()

            # Flag to see if the planet is found
            found = False

            # For loop to iterate through the data list looking at the 'name' key
            for i in range(len(data)):

                # If user input matches a planet on the data list
                if data[i]['name'].lower() == planet.lower().strip():

                    # Prints the planet if the user selected a planet on the list
                    self.interface.print_planet(i, data)

                    # Flag set to True
                    found = True

            # If not found print the planet not found message
            if found == False:
                self.interface.planet_not_found()
