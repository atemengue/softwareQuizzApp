def next_question(questions, question_number):
    """Get the next question by incrementing the question number"""
    question = questions[question_number]
    idQuestion = question[3]
    description = question[1]
    return f"Q.{idQuestion}: {description}"
