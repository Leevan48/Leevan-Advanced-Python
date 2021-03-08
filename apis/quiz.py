import requests
import random

response = requests.get('https://opentdb.com/api.php?amount=5&category=12&difficulty=medium&type=multiple')


class Quiz:
    def __init__(self):
        self.correct_answers = 0


    def get_question(self):
        if response.status_code != 200:
            print('Error', response.status_code)
        else:
            self.data = response.json()
            correct_answers = 0
            for x in range(5):
                self.question = self.data['results'][x]['question']
                self.options = self.data['results'][x]['incorrect_answers']
                self.options.append(self.data['results'][x]['correct_answer'])
                random.shuffle(self.options)
                print(self.question)
                self.answer = self.get_answer()
                self.check_answer(x)

            self.display_score()


    def get_answer(self):
        for item in self.options:
            print(item + ' ')
        self.answer = input()
        return self.answer

    def check_answer(self,x):
        if self.answer == self.data['results'][x]['correct_answer']:
            self.correct_answers += 1
            print('Correct!')

    def display_score(self):
        print('You got ' + str(self.correct_answers) + ' questions correct')


if __name__ == '__main__':
    quiz = Quiz()
    quiz.get_question()


