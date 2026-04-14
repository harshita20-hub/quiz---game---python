questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    ans = input("Enter answer: ").upper()

    if ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("Final Score:", score)
