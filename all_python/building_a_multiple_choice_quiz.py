from Question import Question
question_prompts = [
    "Who created python?\n(A)Akoh inmi\n(B)Ossama Bin Ladin\n(C)John Phillps\n(D)Guido van Rossum\n\n",
    "In what year was python created?\n(A)1200\n(B)2009\n(C)1991\n(D)1999\n\n",
    "What colour are strawberries?\n(A)Yellow\n(B)Blue\n(C)Red\n(D)Purple\n\n"
]

questions = [
    Question(question_prompts[0], "d"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]





def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")
run_test(questions)

