# Pranav Elavarthi
# Aug 26, 2022

def sleep_in(weekday, vacation):
  return (not weekday) or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile
  
def sum_double(a, b):
  return a+b if a != b else 2*(a+b)

def diff21(n):
  return abs(n-21) if n < 21 else 2*abs(n-21)

def parrot_trouble(talking, hour):
  return True if talking and (hour < 7 or hour > 20) else False

def makes10(a, b):
  return True if (a == 10 or b == 10 or a+b == 10) else False

def near_hundred(n):
  return True if (abs(n-100) <= 10 or abs(n-200) <= 10) else False

def pos_neg(a, b, negative):
  return True if (negative and a < 0 and b < 0) else (not negative and ((a < 0 and b > 0) or (a > 0 and b < 0)))

def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag +">"
# Fix this
def make_out_word(out, word):
  return out[:len(out)//2] + word + out[len(out)//2:]

# Fix this
def extra_end(str):
  return str[len(str)-2:] * 3
  
def first_two(str):
  return str if len(str) <= 2 else str[0:2]

def first_half(str):
  return str[0:len(str)//2] if len(str) != 1 else str

def without_end(str):
  return str[1:len(str)-1]

def cigar_party(cigars, is_weekend):
  return cigars >= 40 if is_weekend else 40<=cigars<=60
  
def date_fashion(you, date):
  return 0 if (you <= 2 or date <= 2) else 2 if (you >= 8 or date >=8) else 1

def squirrel_play(temp, is_summer):
  return 60<=temp<=100 if is_summer else 60<=temp<=90
  
def caught_speeding(speed, is_birthday):
  return 0 if speed <= 60 + (int(is_birthday)*5) else 2 if speed > 80 + 5*int(is_birthday) else 1

def sorta_sum(a, b):
  return a+b if (a+b > 19 or a+b<10) else 20

def alarm_clock(day, vacation):
  return "off" if (vacation and (day == 0 or day == 6)) else "10:00" if ((1<=day<=5 and vacation == True) or (vacation == False and (day == 0 or day == 6))) else "7:00"

def love6(a, b):
  return True if (a+b==6 or a-b==6 or b-a == 6 or a==6 or b==6) else False

def in1to10(n, outside_mode):
  return True if (outside_mode and n not in range(2,10)) else True if (not outside_mode and n in range(1,11)) else False

def first_last6(nums):
  return nums[0] ==6 or nums[-1] == 6

def same_first_last(nums):
  return len(nums) >=1 and nums[0] == nums[-1]

def make_pi(index):
  return [3,1,4,1,5,9,2,6,5,3,5][0:index]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  return nums[1:] + nums[0:1]

def reverse3(nums):
  return nums[::-1]

def max_end3(nums):
  return nums if (len(nums) == 1) else [max(nums), max(nums)] if len(nums)==2 else nums[0:1]*len(nums) if (nums[0] > nums[-1]) else nums[len(nums)-1:]*len(nums)

