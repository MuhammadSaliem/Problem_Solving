#problem -> https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
#easy

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = {}

    for i in arr:
        scores[i] = i

    
    print(sorted(scores.keys())[-2])
