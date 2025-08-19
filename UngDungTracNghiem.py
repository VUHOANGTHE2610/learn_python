import quiz
questions = [
    "câu 1: cầu thủ nào là xuất sắc lịch sử bóng đã\nA.Ronaldo \nB.Messi ",
    "câu 2: Ở ấn độ người ta không ăn thịt loài động vật nào \nA. Heo \nB.Bò"
]
quizzes = [
    quiz.Quiz(questions[0], "A")
    , quiz.Quiz(questions[1], "B")
]

def run_Quizzes(quizzes):
    score = 0
    for quiz in quizzes:
        print(quiz.questions)
        user_ip = input("Nhập câu trả lời của bạn: ")
        if user_ip.lower() == quiz.answers.lower():
            score += 5
    print(f"\nBạn đã đạt được số điểm là {score} với {len(questions)} câu hỏi")
run_Quizzes(quizzes)