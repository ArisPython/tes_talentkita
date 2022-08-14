# Program mengecek apakah input string merupakan palindrom atau tidak

def isPalindrome(s):
    # loop dari 0 sampai len/2 
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

# Input string
string = input('Masukkan string: ')

# memanggil fungsi dan menampilkan hasil
reverse = isPalindrome(string)
if reverse:
    print(string,'adalah Palindrome')
else:
    print(string,'Bukan Palindrome')
