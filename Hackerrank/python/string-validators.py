# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# easy
# string

if __name__ == '__main__':
    s = input()

for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(method(c) for c in s))
