#problem -> https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
#easy

def count_substring(string, sub_string):
    count = 0
    stringlen = len(string)
    sublen = len(sub_string)
    for i in range(stringlen):       
        if string[i:len(sub_string)+i] == sub_string:
            count += 1
            
        if stringlen == i + sublen:
            return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)