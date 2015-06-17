__author__ = 'Joel'
'''
Functions created in Code Academy Python Course
'''
#Function for determining if a number is an integer(including xx.0)
def is_int(x):
    if x%1==0:
        return True
    else:
        return False

print is_int(17)
print is_int(17.6)
print '--------'
#Alternate for determining integers(EXCLUDES xx.0)
def is_int_alt(x):
    if isinstance(x,int):
        return True
    else:
        return False

print is_int_alt(17)
print is_int_alt(17.0)
print is_int_alt('test')
print '--------'
#Function for calculating the factorial of a number
def factorial(x):
    b=x
    result=x
    while b>1:
        result*=(b-1)
        b-=1
    return result

print factorial(5)
print factorial(25)
print '--------'
#Function for testing if number is prime
def is_prime(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:
        for i in range (2,x):
            if x%i==0:
                return False
                break
        return True

print is_prime(2)
print is_prime(5)
print is_prime(4)
print is_prime(12)
print '--------'

#Function that reverses a string
def reverse(text):
    a=len(text)-1
    result=''
    while a>=0:
        result+=text[a]
        a-=1
    return result

print reverse('Joel')
print '--------'

#Function strips vowels from a string
def anti_vowel(text):
    result=''
    for i in range(len(text)):
        if text[i] not in ('a','e','i','o','u','A','E','I','O','U'):
            result+=text[i]
    return result

print anti_vowel('Hello friend!')
print '--------'

#Function that calculates a Scrabble score of a word
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    result=0
    for i in word.lower():
        result+=score[i]
    return result

print scrabble_score('Joel')
print '--------'

#Function that replaces a word in a string with asterisks
def censor(text,word):
    lst=text.split()
    result=''
    for a in lst:
        if a==word:
            result+=str('*'*len(word))+' '
        else:
            result+=str(a)+' '
    return result[:-1]

print censor('This is a test','test')
print '--------'

#Alternate function to replace word in string with asterisks
def censor_alt(text,word):
    repl='*'*len(word)
    return text.replace(word,repl)

print censor_alt('This is a test','test')
print '--------'

#Function that counts the number of times an item shows in a list
def count(sequence,item):
    cnt=0
    for i in sequence:
        if i == item:
            cnt+=1
    return cnt

print count(['a','b','c','a'],'a')
print count([1,1,2,1],1)
print '--------'

#Alternate function that counts the number of times an item shows in a list
def count2(sequence,item):
    for i in range(len(sequence)):
        sequence[i]=str(sequence[i])
    f=''.join(sequence)
    return f.count(str(item))

print count2([1,1,2,1],1)
print count2(['a','b','c','a'],'a')
print '--------'

#Function that takes a list of numbers and returns a new list with odds removed
def purify(lst):
    lst2 = []
    for i in lst:
        if i % 2 == 0:
            lst2.append(i)
    return lst2

print purify([1,2,3,4,5])
print '--------'

#Function that takes a list of integers and returns the product of all elements
def product(lst):
    result=1
    for i in lst:
        result*=i
    return result

print product([4,5,6])
print '--------'

#Function that takes a list and returns a new list with duplicates removed
def remove_duplicates(lst):
    lst2=[]
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return lst2

print remove_duplicates([1,2,3,1,2,3,4])
print '--------'

#Alternate function that takes a list and returns new list with dupes removed
def remove_duplicates2(lst):
    return list(set(lst))

print remove_duplicates2([1,2,3,1,2,3,4])
print '--------'

#Function that calculates the median from a list of numbers
def median(lst):
    srt=sorted(lst)
    lng=len(srt)
    if lng % 2 != 0:
        return srt[lng/2]
    else:
        acc1 = lng/2-1
        acc2 = acc1+1
        return (srt[acc1]+srt[acc2])/2.0

print median([1,3.25,4,5])
print median([1,2,3,4,5])
print '--------'

#PROGRAM: Calculates the sum, average, variance and std deviation of list of grades
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

print grades_sum(grades)

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

print grades_average(grades)

def grades_variance(scores):
    average=grades_average(scores)
    variance=0
    for score in scores:
        variance+=(average-score)**2
    return variance/len(scores)

print grades_variance(grades)

def grades_std_deviation(variance):
    return variance **.5

print grades_std_deviation(grades_variance(grades))
print '--------'


'''
LIST COMPREHENSIONS & LAMBDA FUNCTIONS
'''

#List comprehension that looks for even squares in a range of 1 to 11
even_squares = [x**2 for x in range(1,12) if x%2==0]

print even_squares
print '--------'

#List comp that looks for cubes divisible by 4 in a range of 1 to 10
cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]

print cubes_by_four
print '--------'

#List comp that looks for numbers between 1 to 15 range that are divisible by 3 or 5
threes_and_fives = [x for x in range(1,16) if x%3==0 or x%5==0]
print threes_and_fives
print '--------'

#List comp grabs squares in range 1 to 10 and Lambda function filters squares in range 30-70
squares = [x**2 for x in range(1,11)]
print filter(lambda x: x in range(30,71),squares)
print '--------'

'''
BITWISE OPERATIONS

print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND ...Both bits =1
print 9 | 4   # Bitwise OR ...either bits =1
print 12 ^ 42 # Bitwise XOR ...either bits =1 but not both
print ~88     # Bitwise NOT ...add 1 and make negative
'''
#Function that checks if the fourth bit is on or off
def check_bit4(input):
    mask=0b1000
    if input & mask >0:
        return 'on'
    else:
        return 'off'

print check_bit4(0b1000)
print check_bit4(0b11)
print '--------'

#Function that uses shift left to create bit mask that helps flip the nth bit in number
def flip_bit(number,n):
    mask = 0b1 << n-1  #this creates a mask with a particular bit turned on
    result =number^mask  #this then uses the mask to flip that particular bit in the number
    return bin(result)

print flip_bit(0b1100,6)
print '--------'

'''
Class coding -- Defining classes, inheritance, and instantiating (also the use of super())
'''
class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1,self.angle2,self.angle3 = self.angle,self.angle,self.angle
    def check_angles(self):
        if (self.angle1+self.angle2+self.angle3)/3 == 60:
            return True,'Checks out to 180, sir!'
        else:
            return False
    def check_angles2(self):
        return super(Equilateral,self).check_angles()

test=Equilateral()
print test.number_of_sides
print test.angle
print test.check_angles()
print test.check_angles2()

'''
FILE/INPUT OUTPUT STUFF
remember to close file objects as they buffer....open,read/write,close
with open('text.txt','w') as my_file:
    my_file.write('The boy goes in, the boy goes out!')

if not my_file.closed:
    my_file.close()

print my_file.closed
'''
