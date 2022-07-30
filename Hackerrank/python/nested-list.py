#problem -> https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
#easy

grades = {}

for _ in range(int(input())):
    name = input()
    score = float(input())
    grades[score] = [name] + grades.get(score, [])

secondLowestGrade = sorted(grades.keys())[1]
[print(name) for name in sorted(grades[secondLowestGrade])]


