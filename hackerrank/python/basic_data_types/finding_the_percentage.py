if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # Get the marks list of the queried student name
    score_list = student_marks.get(query_name)
    #Calculating average
    average = sum(score_list)/len(score_list)
    print('{:.2f}'.format(average))