import json
from random import shuffle


def main():
    mode = input("(p)lay trivia\n(v)iew credits\n(q)uit\n")
    if(mode == "p"):
        with open("questions.json", 'r') as questions_file:
            questions = json.load(questions_file)
        shuffle(questions)
        play(questions)
    elif(mode == "v"):
        print("\nTrivia made by William Rogers and Kile Driscoll\n")
        main()
    elif(mode == "q"):
        print("Thanks for playing!")
    else:
        print("\nPlease enter a valid mode.\n")
        main()


def prompt_question(question, correct, total):
    print(question["prompt"])
    index = 0
    while index < len(question["answers"]):
        choice = question["answers"][index]
        print(f"{index + 1}. {choice}")
        index += 1
    answer = input("Choose an answer 1−4: ")
    try:
        if((int(answer) <= len(question["answers"])) & (int(answer) > 0)):
            pass
        else:
            prompt_question(question, correct, total)
    except ValueError:
        prompt_question(question, correct, total)
    if answer == question["correct"]:
        print("Goodjob! *Confettifalls in the background*")
        correct += 1
        print(f"Score: {correct}/{total}\n")
    else:
        print("Not correct. *The audience boos*\n")
        print(f"Score: {correct}/{total}\n")
    return correct


def play(questions):
    print("\nWelcome to our CS126 Trivia Game")
    print("Win MILLIONS!!\n")
    correct = 0
    total = len(questions)
    for question in questions:
        correct = prompt_question(question, correct, total)
    print(f"You got {correct}/{total} correct!\n")
    main()


if __name__ == "__main__":
    main()
