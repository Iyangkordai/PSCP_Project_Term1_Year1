"""Grade Calculator"""

def grade():
    """Calculate"""
    score = int(input())
    if score >= 80:
        print("Very Good")
    elif score >= 50:
        print("Average")
    else:
        print("Failed")

grade()
