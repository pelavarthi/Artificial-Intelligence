def string_times(str, n):
  return str*n

def front_times(str, n):
  return n*str[:3]

def string_bits(str):
  return str[::2]

def string_splosion(str):
  return "".join(str[:i] for i in range(len(str)+1))

def last2(str):
  return sum(str[-2:] == str[i:i+2] for i in range(len(str)-2))

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  return 9 in nums[:4]

def array123(nums):
  return " 1 2 3 " in " " + " ".join(str(i) for i in nums) + " "

def string_match(a, b):
  return sum(1 for x in range(len(a)) if a[x:x+2] == b[x:x+2] and len(a[x:x+2]) == 2)

def double_char(str):
  return "".join(str[i]*2 for i in range(len(str)))

def count_hi(str):
  return str.count("hi")

def cat_dog(str):
  return str.count("cat") == str.count("dog")

def count_code(str):
  return sum(str.count('co'+x+'e') for x in set(str))

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def xyz_there(str):
  return bool(sum(1 for i in range(len(str)-2) if str[i:i+3] == "xyz" and str[i-1:i+3] != ".xyz"))

def count_evens(nums):
  return sum(1 for num in nums if num%2==0)

def big_diff(nums):
  return max(nums)-min(nums)

def centered_average(nums):
  return (sum(nums)-(max(nums)+min(nums)))//(len(nums)-2)

def sum13(nums):
  return sum(nums[i] for i in range(len(nums)) if nums[i] != 13 and (nums[i-1] != 13 or i==0))

def has22(nums):
  return (2,2) in zip(nums,nums[1:])

def make_bricks(small, big, goal):
  return goal%5<=small and goal-(5*big)<=small

def lone_sum(a, b, c):
  return sum(num for num in [a,b,c] if [a,b,c].count(num)==1)

def lucky_sum(a, b, c):
  return a*(a!=13) + b*(b!=13)*(a!=13) + c*(c!=13)*(b!=13)*(a!=13)

def no_teen_sum(a, b, c):
  return sum(i*(i<13 or i>19 or i==15 or i==16) for i in [a,b,c])

def close_far(a, b, c):
  return ((abs(a-b)<=1 and abs(a-c)>=2 and abs(b-c)>=2) != (abs(a-c)<=1 and abs(a-b)>=2 and abs(b-c)>=2))

def round_sum(a, b, c):
  return int(round(a+0.1,-1)+round(b+0.1,-1)+round(c+0.1,-1))
  
def make_chocolate(small, big, goal):
  return (goal-5*min(int(goal/5), big) <= small)*(goal-5*min(int(goal/5), big))+(-1*(goal-5*min(int(goal/5), big) >small))  

def sum67(nums):
  return sum(v for i,v in enumerate(nums) if (6 not in nums[:i+1] or (7 in nums[:i] and nums[i::-1].index(6) > nums[i-1::-1].index(7))))


# Pranav Elavarthi, period 5, 2024
