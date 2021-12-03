class Interface:

    '''
    This class is responsible for all interactions with the user.    
    '''

    def greeting(self):
        '''
        Prints a greeting to the user about which planet they would like to visit
        Takes a name and prints name back within greeting
        '''


        print()
        print("Welcome to the Space Adventure! We will be visiting planets all over the universe!")
        print()

        name = input('What is your name? Please type name: ')
        print('Welcome, ' + str(name) + '. We are going to go on an adventure!')
        print()

    def want_random(self):
        '''
        Asks the user if they would like to visit a random planet.
        If the answer is not Y, y, N, n it will continue to ask the user repeatedly
        '''

        while True:

            random_y_n = input(
                'Would you like to visit a random planet? Y/N ').lower().strip()

            if random_y_n == 'y':
                return True

            if random_y_n == 'n':
                return False

            else:
                print()
                print("Sorry I didn't get that!")

    def pick_a_planet(self):
        '''
        Asks the user which planet they would like to go to,
        and returns the answer.
        '''
        print()
        planet = input("Which planet do you want to go to then? ")
        return planet

    def planet_not_found(self):
        '''
        Prints if the planet is not found.
        '''        
        print
        print("We don't have that planet!")

    def print_planet(self, i, data):
        '''
        Prints the planet that is being selected, either by the user,
        or randomly. 
        '''
        print()
        print(data[i]['name'])
        print(data[i]['description'])
