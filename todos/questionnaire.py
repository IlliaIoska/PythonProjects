import json

with open("questions.json", "r") as json_questions:
    json_questions_content = json_questions.read()

data = json.loads(json_questions_content)

continue_questionnaire = True

while(continue_questionnaire):
    print("Questionnaire:")
    for question in data:
        print(question["question_text"])

    question_num = int(input("Enter 1, 2 , or 3 for the number of the question you want to answer\n"))
    question_index = question_num - 1
    print(data[question_index]["question_text"])

    for possible_answer in data[question_index]["possible_answers"]:
        print(possible_answer)
    answer = input("Enter your answer")
    if (answer.strip() == data[question_index]["correct_answer"]):
        print("Correct")
    else:
        print("Incorrect")

    continue_questionnaire = input("Wish to continue? Y/y (yes) or N/n (no)")
    if (continue_questionnaire.strip() == "y" or continue_questionnaire.strip() == "Y"):
        continue_questionnaire = True
    else:
        continue_questionnaire = False
