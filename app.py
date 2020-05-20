import sys

class Questionnaire:
    def __init__(self):
        self.name = ""
        self.cocktail = ""
        self.hobby = ""
        self.desired_skill = ""
        self.bucket_list = ""
        self.adjective = ""

    def ask_me_stuff(self):
        print("Hi! I'm going to ask you some questions...\n")
        self.name = input('What is your name?: ')
        self.cocktail = input("Favorite Q-life drink: ")
        self.hobby = input("Favorite thing to do during quarantine?: ")
        self.desired_skill = input("One new skill you have learned during Q-life?: ")
        self.bucket_list = input("What will you do first when Q-life is over?: ")
        self.adjective = input("One word to best describe you: ")

        print("\n\n")

    def about_me(self):
        print(f"Hello! my name is {self.name}")
        print(f"The Q-life has me drinking {self.cocktail}")
        print(f"My favorite thing to do during the quarantine is {self.hobby}")
        print(f"Because I have so much spare time in the Q-life, I've learned how to {self.desired_skill}")
        print(f"when Q-life is over, i will be {self.bucket_list}")
        print(f"Many would describe me as {self.adjective}")

if __name__ == "__main__":
    q = Questionnaire()
    q.ask_me_stuff()
    q.about_me()
    sys.exit(0)