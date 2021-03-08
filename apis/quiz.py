import requests

response = requests.get('https://opentdb.com/api.php?amount=5&category=12&difficulty=medium&type=multiple')


class Quiz:
    def __init__(self):
        self.word = ''


    def get_question(self):
        if response.status_code != 200:
            print('Error', response.status_code)
        else:
            data = response.json()
            correct_answers = 0
            for x in range(5):
                self.question = data['results'][x]['question']
                self.options = data['results'][x]['incorrect_answers']
                self.options.append(data['results'][x]['correct_answer'])
                print(self.question)
                answer = self.get_answer()

                if self.answer == data['results'][x]['correct_answer']:
                    correct_answers += 1

            print('You got ' + str(correct_answers) + ' questions correct')

    def get_answer(self):
        for item in self.options:
            print(item + ' ')
        self.answer = input()
        return self.answer



if __name__ == '__main__':
    quiz = Quiz()
    quiz.get_question()


