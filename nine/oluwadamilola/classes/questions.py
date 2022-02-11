from question_class import Questions
answers = []
question_prompt = [
    """
    Question 1:
                A expend energy, enjoy groups
                B conserve energy, enjoy one-on-one
    """,
    """
     Question 2:
                A interpret literally
                B look for meaning and possibilities
    """,
    """
     Question 3:
                A logical, thinking, questioning
                B empathetic, feeling, accommodating
    """,
    """
    Question 4:
                A organized, orderly
                B flexible, adaptable
    """,
    """
     Question 5:
                A more outgoing, think out loud
                B more reserved, think to yourself
    """,
    """
     Question 6:
                A practical, realistic, experimental
                B imaginative, innovative, theoretical
    """,
    """
    Question 7:
                A candid, straight forward, frank
                B tactful, kind, encouraging
    """,
    """
    Question 8:
                A plan, schedule
                B unplanned, spontaneous
    """,
    """
    Question 9:
                A seek many tasks,public activities, interaction with others
                B seek private, solitary activities with quiet to concentrate
    """,

    """
    Question 10:
                A standard, usual, conventional
                B different, novel, unique

    """,
    """
     Question 11:
                A firm, tend to criticize, bold the line
                B gentle, tend to appreciate, concillate
    """,
    """
     Question 12:
                A regulated structured
                B easygoing, "live" and "let live"
    """,
    """
    Question 13:
                A external, communicative, express yourself
                B internal, reticent, keep it to yourself
    """,
    """
    Question 14:
                A focus on here-and-now
                B look to the future, global perspective, "big picture"
    """,
    """
    Question 15:
                A tough-minded,just
                B tender-hearted, merciful
    """,
    """
    Question 16:
                A preparation, plan ahead
                B go with the flow, adapt as you go
    """,
    """
    Question 17:
                A active, initiate
                B reflective, deliberate
    """,
    """
    Question 18:
                A facts, things, "What is"
                B ideas, dreams, "What could be", philosophical
    """,
    """
    Question 19:
                A matter of fact, issue - oriented
                B sensitive, people-oriented, compassionate
    """,
    """
    Question 20:
                A control, govern
                B latitude, freedom
    """

]

questions = [
    Questions(question_prompt[0]),
    Questions(question_prompt[1]),
    Questions(question_prompt[2]),
    Questions(question_prompt[3]),
    Questions(question_prompt[4]),
    Questions(question_prompt[5]),
    Questions(question_prompt[6]),
    Questions(question_prompt[7]),
    Questions(question_prompt[8]),
    Questions(question_prompt[9]),
    Questions(question_prompt[10]),
    Questions(question_prompt[11]),
    Questions(question_prompt[12]),
    Questions(question_prompt[13]),
    Questions(question_prompt[14]),
    Questions(question_prompt[15]),
    Questions(question_prompt[16]),
    Questions(question_prompt[17]),
    Questions(question_prompt[18]),
    Questions(question_prompt[19])
 
]

def get_questions():
    print("""
        Check your personality here!
        choose either A or B on your  best personality:
    """)
    for question in questions:
        answer = input(question)
        answers.append(answer)
       
def extrovert_or_introvert():
    result_for_a = 0
    result_for_b = 0

    for i in range(0, len(questions), 4):
        if answers[i] == "A".casefold():
            result_for_a +=1
        if answers[i] == "B".casefold():
            result_for_b +=1
    if result_for_a > result_for_b:
            print("Extrovert")
    else:
            print("Introvert") 

def sensor_or_intuition():
    result_for_a = 0
    result_for_b = 0

    for i in range(1, len(questions), 4):
        if answers[i] == "A".casefold():
            result_for_a +=1
        if answers[i] == "B".casefold():
            result_for_b +=1
    if result_for_a > result_for_b:
            print("Sensor")
    else:
            print("Intuition") 

def thinkers_or_feelers():
    result_for_a = 0
    result_for_b = 0

    for i in range(2, len(questions), 4):
        if answers[i] == "A".casefold():
            result_for_a +=1
        if answers[i] == "B".casefold():
            result_for_b +=1
    if result_for_a > result_for_b:
            print("Thinker")
    else:
            print("Feeler")

def judger_or_perciever():
    result_for_a = 0
    result_for_b = 0

    for i in range(3, len(questions), 4):
        if answers[i] == "A".casefold():
            result_for_a +=1
        if answers[i] == "B".casefold():
            result_for_b +=1
    if result_for_a > result_for_b:
            print("Judger")
    else:
            print("Perciever") 

def personality():
    print("Your Personalities are: ")
    extrovert_or_introvert()
    sensor_or_intuition()
    thinkers_or_feelers()
    judger_or_perciever()

get_questions()
print()
personality()