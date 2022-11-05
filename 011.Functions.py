# How to write a function
def add(num1, num2):
    ans = num1 + num2
    return ans

print(add(2,4)) #returns 6

# calling a function
def sub(num1, num2):
    ans = num1 - num2
    print(ans) 

sub(8,4) #prints 4

# Variable Length Arguments(Non Keyword Arguments)

def purchase_games(min_game,*args):
    print(f"You have purchased {min_game}")
    print(args)

purchase_games("GTA","COD","R6S") # except GTA all the games will be stored in a tuple, here in args


#Variable Length Arguments(Keyword Arguments)
def games(*args, **kwargs):
    print(args) #prints a tuple
    print(kwargs) #prints a dictionary

games(1,2,4, COD = "MW",GTA = "5")