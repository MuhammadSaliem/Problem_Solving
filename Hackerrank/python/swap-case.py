# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# easy
# string

#1- First Solution
# def swap_case(s):
#     swapLst = []
#     for c in s:
#         if c.isalpha():
#             if c.islower():
#                 swapLst.append(c.upper())
#             else:
#                 swapLst.append(c.lower())
#         else:
#             swapLst.append(c)
#     return ''.join(swapLst)
            
#2- Better Solution
# def swap_case(s):
#     return s.swapcase()

#3- List Comprehension
def swap_case(s):
    lst = list(s)
    return ''.join([c.lower() if c.isupper() else c.upper() for c in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)