"""Calculator"""

def main():
    """Main"""
    n = int(input())
    cnt = 0
    if n <= 1:
        print(1)
    else:
        for i in range(1, n + 1):
            cnt += len(str(i)) + 1
        print(cnt)
  
main()
