####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'BrownTown'
strategy_name = 'DaBullz (dubbles)'
strategy_description = 'we start of with c and after every 2 c/b it changes ex:cc,bb,cc,bb,cc'
    
def move(my_history, their_history, my_score, their_score):
    return 'c'
    n = 0
    while n < 9 & n >= 2:
            if my_history[-2] == 'c' and my_history[-1] == 'c':
                return 'b'
                n += 1	
            if my_history[-2] == 'b' and my_history[-1] == 'b':
		return 'c'
		n += 1
            if my_history[-1] == 'c':
		return 'c'
		n += 1
            if my_history[-1] == 'b':
		return 'b'
		n += 1