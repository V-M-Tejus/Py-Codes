class Palindrome:
 def _init_(self):
 self.isPalindrome = False
 def chkPalindrome(self, myStr):
 if myStr == myStr[::-1]:
 self.isPalindrome = True
 else:
 self.isPalindrome = False
 return self.isPalindrome
class PaliInt(Palindrome):
 def _init_(self):
 self.isPalindrome = False
 def chkPalindrome(self, val):
 temp = val
 rev = 0
 while temp != 0:
 dig = temp % 10
 rev = (rev * 10) + dig
 temp = temp // 10
 if val == rev:
 self.isPalindrome = True
 else:
 self.isPalindrome = False
 return self.isPalindrome
st = input("Enter a string: ")
stobj = Palindrome()
if stobj.chkPalindrome(st):
 print("Given string is a Palindrome")
else:
 print("Given string is not a Palindrome")
val = int(input("Enter an integer: "))
intobj = PaliInt()
if intobj.chkPalindrome(val):
 print("Given integer is a Palindrome")
else:
 print("Given integer is not a Palindrome")
