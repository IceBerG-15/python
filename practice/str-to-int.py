def myAtoi(self, s: str) -> int:
    s = s.lstrip(' ').rstrip(' ')
    s = s.split()
    ans = ''
    c = False
    for word in s:
        if (word[0]>='a' or word[0]>='A') and (word[0]<='z' or word[0]>='Z'):
            continue
        elif word[0]=='+' or word[0]=='-' or word[0]>='0' or word[0]=='9':
            if word[1]>='0' or word[1]=='9':
                ans = word
                c = True
                break
    if c:
        ans.lstrip('0')
        ans  = int(ans)
        return ans
    return 0

print(myAtoi("0099 is a word"))