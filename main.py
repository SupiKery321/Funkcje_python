#1 sposób z pomocą kolegi
def reverse(word):
    for i in range(0,len(word)-1):
     if word[i] != word[len(word)-i-1]:
      return(False)
    return(True)

word = "kajak"

print(reverse(word))


#2 sposób- własny pomysł

def palindrom(s):
    return s == s[::-1]

s = "kajak"
es = palindrom(s)
 
if es:
 print(True)
else:
    print(False)


