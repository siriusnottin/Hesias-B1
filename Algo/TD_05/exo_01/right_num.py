import random

def play_game(difficulty_level):
  def guess_number(num_to_guess,max_tries):
    correct_answer = False
    user_tries_count = 1
    while correct_answer == False:
      if user_tries_count > max_tries:
        print('Game over!')
        print('The number was: ', num_to_guess)
        return end_game()
      arg = int(input('Your guess: '))
      if arg > num_to_guess:
        print('Too high')
        user_tries_count +=1
      elif arg < num_to_guess:
        print('Too low')
        user_tries_count +=1
      elif arg == num_to_guess:
        print('Correct!')
        print('Number of tries:', user_tries_count)
        correct_answer = True
        return None

  if difficulty_level == 'normal':
    s = 10 #upper bound for guessing range
    d = random.randint(1, s) #number to guess
    e = 6 #max attempts
    print('[Level normal] Find the number between', 1, 'and', s, '(you have', e, 'tries)')
    guess_number(d,e)
  elif difficulty_level == 'hard':
    s = 20 #upper bound for guessing range
    d = random.randint(1, s) #number to guess
    e = 3 #max attempts
    print('[Level hard] Find the number between', 1, 'and', s, '(you have', e, 'tries)')
    guess_number(d,e)

def start_game():
  def ask_diff_level():
    arg = input('Difficulty level (normal|hard) : ')
    if arg == 'normal' or arg == 'hard':
      return arg
    elif arg == '': # default arg
      return 'normal'
  difficulty_level = ask_diff_level()
  play_game(difficulty_level)

def end_game():
  arg = int(input('Play again? (0=no, 1=yes): '))
  if arg == 1:
    print('Restarting the game…')
    return start_game()
  elif arg == 0:
    print('Exiting…')
    return None

start_game()
