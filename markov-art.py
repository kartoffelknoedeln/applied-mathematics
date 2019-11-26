import random
import csv

class Markov(object):

    def __init__(self, counter = 0, green = 0, red = 0, blue = 0, yellow = 0):
        self.counter = counter
        self.green = green
        self.red = red
        self.blue = blue
        self.yellow = yellow

    def write_to_csv(self, green, red, blue, yellow):
        savefile.write(str(green) + ',')
        savefile.write(str(red) + ',')
        savefile.write(str(blue) + ',')
        savefile.write(str(yellow) + '\n')
            
    def yellow_colour(self, counter, green, red, blue, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 800:
            if randnum <= 10:
                counter += 1
                green += 1
                self.green_colour(counter, green, red, blue, yellow)
            elif 11 <= randnum <= 25:
                counter += 1
                red += 1
                self.red_colour(counter, green, red, blue, yellow)
            elif 26 <= randnum <= 40:
                counter += 1
                blue += 1
                self.blue_colour(counter, green, red, blue, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, green, red, blue, yellow)
        else:
            self.write_to_csv(green, red, blue, yellow)

    def red_colour(self, counter, green, red, blue, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 800:
            if randnum <= 15:
                counter += 1
                green += 1
                self.green_colour(counter, green, red, blue, yellow)
            elif 16 <= randnum <= 65:
                counter += 1
                red += 1
                self.red_colour(counter, green, red, blue, yellow)
            elif 66 <= randnum <= 90:
                counter += 1
                blue += 1
                self.blue_colour(counter, green, red, blue, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, green, red, blue, yellow)
        else:
            self.write_to_csv(green, red, blue, yellow)

    def blue_colour(self, counter, green, red, blue, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 800:
            if randnum <= 15:
                counter += 1
                green += 1
                self.green_colour(counter, green, red, blue, yellow)
            elif 16 <= randnum <= 40:
                counter += 1
                red += 1
                self.red_colour(counter, green, red, blue, yellow)
            elif 41 <= randnum <= 90:
                counter += 1
                blue += 1
                self.blue_colour(counter, green, red, blue, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, green, red, blue, yellow)
        else:
            self.write_to_csv(green, red, blue, yellow)

    def green_colour(self, counter, green, red, blue, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 800:
            if randnum <= 40:
                counter += 1
                green += 1
                self.green_colour(counter, green, red, blue, yellow)
            elif 41 <= randnum <= 60:
                counter += 1
                red += 1
                self.red_colour(counter, green, red, blue, yellow)
            elif 61 <= randnum <= 80:
                counter += 1
                blue += 1
                self.blue_colour(counter, green, red, blue, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, green, red, blue, yellow)
        else:
            self.write_to_csv(green, red, blue, yellow)
           
if __name__ == '__main__':
    markov = Markov()
    savefile = open('Art.csv', 'w')
    savefile.write(' , Green, Red, Blue, Yellow\n')   
    
    for i in range(1, 17):
        savefile.write(str(i) + ',')
        markov.yellow_colour(markov.counter, markov.green, markov.red, markov.blue, markov.yellow)

    savefile.close()
    print('Done.')
