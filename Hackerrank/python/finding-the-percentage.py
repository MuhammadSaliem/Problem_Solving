#Problem -> https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
#easy
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
print("{:.2f}".format(sum(student_marks[input()])/len(student_marks[input()])))
