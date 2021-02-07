import mysql.connector

cnx = mysql.connector.connect(user='root', password='ayk123', host='localhost', database='quiz_application')
mycursor = cnx.cursor();


def super_user_ui():
    print("\nSet quiz\n")
    topic = input("Enter the quiz topic: ")
    level = int(input("Enter the diffulty level from 1 - 3, 1 being easy: "))
    mycursor.execute('INSERT INTO quiz(topic, difficulty) VALUES (%s, %s)', (topic, level));
    cnx.commit()
    quizid = mycursor.lastrowid
    for i in range(5):
        que = input("Enter question {}: ".format(i+1))
        mycursor.execute('INSERT INTO questions(question, quizid) VALUES (%s, %s)', (que, quizid));
        cnx.commit()
        questionid = mycursor.lastrowid
        for i in range(4):
            opt = input("Enter option {}: ".format(i+1))
            mycursor.execute('INSERT INTO options(opt, questionid) VALUES (%s, %s)', (opt, questionid));
            cnx.commit()
        ans = input("Enter the correct answer: ")
        mycursor.execute('UPDATE questions SET answer = %s where qid = %s', (ans, questionid));
        cnx.commit()

    print("\nThank you for adding a quiz for", topic, "with difficulty", level,"\n")
            



def user_ui():
    mycursor.execute("SELECT * FROM quiz;")
    quizes = mycursor.fetchall()
    if(len(quizes)>0):
        
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        score = 0
        print("\nAvailable Quizes\n")
        print("ID       Topic     Difficulty")
        for quiz in quizes:
            print(quiz[0],"     ", quiz[1], "     ", quiz[2])
        quiz_choice = int(input("\nSelect a quiz: "))
        for quiz in quizes:
            if quiz[0] == quiz_choice:
                break
        else:
            print("Wrong choice\n")

        mycursor.execute('SELECT * FROM questions where quizid = %s', (quiz_choice,))
        questions = mycursor.fetchall()

        for i in range(len(questions)):
            mycursor.execute('SELECT * FROM options where questionid = %s', (questions[i][0],))
            options = mycursor.fetchall()
            print("\n")
            print("Q.",i+1,questions[i][1])
            for j in range(len(options)):
                print(j+1, options[j][1])

            ans = int(input("Ans: "))
            if(options[ans-1][1] == questions[i][3]):
                print("Correct")
                score += 10

        

        print("\nName: ", name,"\nAge: ", age, "\nScore: ", score, "out of", len(questions)*10,"\n")
        print("Correct answers: ")
        for q in range(len(questions)):
            print(i+1,questions[q][3])

        mycursor.execute('INSERT INTO users(name, age, score, quizid) VALUES (%s, %s, %s, %s)', (name, age, score, quiz_choice));
        cnx.commit()

    else:
        print("No quiz available. Ask the admin to add one")


while (True):
    print("\n\n_________________________Welcome to the Quiz Application_________________________\n\nPlease selecte your role:\n1. Super user(Set quiz)\n2. User(Attempt quiz)\n\nPress 9 to exit")
    user_type = int(input())

    if user_type == 1:
        super_user_ui()

    elif user_type == 2:
        user_ui()

    elif user_type == 9:
        break

    else:
        print("Please enter a valid choice\n")