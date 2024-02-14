score = int(input("Enter the score"))

if score >= 90:
    print(f"Your score is a grade of A")
elif 80 <= score < 90:
    print(f"Your score is a grade of B")
elif 70 <= score < 80:
    print(f"Your score is a grade of C")
elif 60 <= score < 70:
    print(f"Your score is a grade of D")
elif 50 <= score < 60:
    print(f"Your score is a grade of F")
