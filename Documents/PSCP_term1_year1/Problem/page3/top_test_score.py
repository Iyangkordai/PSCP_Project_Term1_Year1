"""Top Test Score"""

def main():
    """Main"""
    student_n = int(input())
    top_score = 0
    top_student = 0
    for _ in range(student_n):
        score = int(input())
        if score > top_score:
            top_score = score
            top_student = 0
        if score == top_score:
            top_student += 1
    print(top_score)
    print(top_student)

main()
