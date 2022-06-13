# Q03
# 로그 파일 재정렬

# 로그의 가장 앞 부분은 식별자다.
# 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 식별자를 제외한 문자가 동일한 경우 식별자 순으로 한다.
# 숫자 로그는 입력 순서대로 한다.

def reorderLogFiles(logs):
    # letters : 문자로 구성된 로그 / digits 숫자 로그
    letters, digits = [], []
    # 숫자 로그이면, digits 리스트에 삽입
    # 문자로 구성된 로그이면, letters 리스트에 삽입
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 문자로 구성된 로그를 재정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


if __name__ == "__main__":
    logs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dog",
        "let3 art zero"
    ]
    print(reorderLogFiles(logs))
    """
    [
        'let1 art can', 
        'let3 art zero', 
        'let2 own kit dog', 
        'dig1 8 1 5 1', 
        'dig2 3 6'
    ]
        """
