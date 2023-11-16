import random


class Answer:
    def __init__(self, x_color, y_pos):
        self.__x_color = x_color
        self.__y_pos = y_pos

    def random_color(self):
        random_color = []
        for i in range(self.y_pos):
            color = random.randrange(1, self.x_color + 1)
            random_color.append(color)
        return random_color

    def set_x_color(self, x_color):
        self.__x_color = x_color

    def set_y_pos(self, y_pos):
        self.__y_pos = y_pos

    @property
    def x_color(self):
        return self.__x_color

    @property
    def y_pos(self):
        return self.__y_pos


class PLayer:
    def __init__(self, guess, answer):
        self.guess = guess
        self.random_answer = answer

    def play(self):
        for num in range(len(self.guess)):
            if int(self.guess[num]) == self.random_answer[num]:
                print('*', end='')
            elif int(self.guess[num]) in random_answer:
                print('o', end='')
            else:
                pass


input_x = int(input('colors : '))
input_y = int(input('position : '))
input_answer = Answer(input_x, input_y)
random_answer = input_answer.random_color()
# print(random_answer)

rounds = 0
while True:
    player_guess = input('What is your guess?: ')
    player = PLayer(player_guess, random_answer)
    int_player_guess = [int(x) for x in player_guess]
    if int_player_guess == random_answer:
        print('****')
        rounds += 1
        break
    else:
        player.play()
        print('')
        print('')
        rounds += 1

print('')
print(f'You solve it after {rounds} rounds')
