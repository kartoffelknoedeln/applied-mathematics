import random
import csv

class Markov:
    def __init__(self, counter = 0, black = 0, red = 0, blue = 0, white = 0, yellow = 0):
        self.counter = counter
        self.black = black
        self.red = red
        self.blue = blue
        self.white = white
        self.yellow = yellow

    def write_to_csv(self, black, red, blue, white, yellow):
        savefile.write(str(black) + ',')
        savefile.write(str(red) + ',')
        savefile.write(str(blue) + ',')
        savefile.write(str(white) + ',')
        savefile.write(str(yellow) + '\n')

    def black_colour(self, counter, black, red, blue, white, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 100:
            if randnum <= 30:
                counter += 1
                black += 1
                self.black_colour(counter, black, red, blue, white, yellow)
            elif 31 <= randnum <= 35:
                counter += 1
                red += 1
                self.red_colour(counter, black, red, blue, white, yellow)
            elif 36 <= randnum <= 40:
                counter += 1
                blue += 1
                self.blue_colour(counter, black, red, blue, white, yellow)
            elif 41 <= randnum <= 95:
                counter += 1
                white += 1
                self.white_colour(counter, black, red, blue, white, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, black, red, blue, white, yellow)
        else:
            self.write_to_csv(black, red, blue, white, yellow)

    def red_colour(self, counter, black, red, blue, white, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 100:
            if randnum <= 5:
                counter += 1
                black += 1
                self.black_colour(counter, black, red, blue, white, yellow)
            elif 6 <= randnum <= 35:
                counter += 1
                red += 1
                self.red_colour(counter, black, red, blue, white, yellow)
            elif 36 <= randnum <= 40:
                counter += 1
                blue += 1
                self.blue_colour(counter, black, red, blue, white, yellow)
            elif 41 <= randnum <= 95:
                counter += 1
                white += 1
                self.white_colour(counter, black, red, blue, white, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, black, red, blue, white, yellow)
        else:
            self.write_to_csv(black, red, blue, white, yellow)

    def blue_colour(self, counter, black, red, blue, white, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 100:
            if randnum <= 5:
                counter += 1
                black += 1
                self.black_colour(counter, black, red, blue, white, yellow)
            elif 6 <= randnum <= 10:
                counter += 1
                red += 1
                self.red_colour(counter, black, red, blue, white, yellow)
            elif 11 <= randnum <= 40:
                counter += 1
                blue += 1
                self.blue_colour(counter, black, red, blue, white, yellow)
            elif 41 <= randnum <= 95:
                counter += 1
                white += 1
                self.white_colour(counter, black, red, blue, white, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, black, red, blue, white, yellow)
        else:
            self.write_to_csv(black, red, blue, white, yellow)

    def white_colour(self, counter, black, red, blue, white, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 100:
            if randnum <= 5:
                counter += 1
                black += 1
                self.black_colour(counter, black, red, blue, white, yellow)
            elif 6 <= randnum <= 10:
                counter += 1
                red += 1
                self.red_colour(counter, black, red, blue, white, yellow)
            elif 11 <= randnum <= 15:
                counter += 1
                blue += 1
                self.blue_colour(counter, black, red, blue, white, yellow)
            elif 16 <= randnum <= 95:
                counter += 1
                white += 1
                self.white_colour(counter, black, red, blue, white, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, black, red, blue, white, yellow)
        else:
            self.write_to_csv(black, red, blue, white, yellow)

    def yellow_colour(self, counter, black, red, blue, white, yellow):
        randnum = random.randint(1, 101)
        blank_string = ''
        if counter < 100:
            if randnum <= 5:
                counter += 1
                black += 1
                self.black_colour(counter, black, red, blue, white, yellow)
            elif 6 <= randnum <= 10:
                counter += 1
                red += 1
                self.red_colour(counter, black, red, blue, white, yellow)
            elif 11 <= randnum <= 15:
                counter += 1
                blue += 1
                self.blue_colour(counter, black, red, blue, white, yellow)
            elif 16 <= randnum <= 70:
                counter += 1
                white += 1
                self.white_colour(counter, black, red, blue, white, yellow)
            else:
                counter += 1
                yellow += 1
                self.yellow_colour(counter, black, red, blue, white, yellow)
        else:
            self.write_to_csv(black, red, blue, white, yellow)
           
if __name__ == '__main__':
    markov = Markov()
    savefile = open('Art.csv', 'w')
    savefile.write(' , Black, Red, Blue, White, Yellow\n')   
    
    for i in range(1, 10):
        savefile.write(str(i) + ',')
        markov.black_colour(markov.counter, markov.black, markov.red, markov.blue, markov.white, markov.yellow)

    savefile.close()
    print('Done.')
