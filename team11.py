def move(my_history, their_history, my_score, their_score):
choices = ['c','b']
    if len(my_history) == 0:
      return 'c'
    elif their_history [-4:] == 'bbbb':
      return 'c'
    elif their_history [-2:] == 'bb':
      return 'b'
    elif their_history [-1] == 'c':
      return 'c'
    elif their_history [-1] == 'b':
      return 'b'
    elif their_score < my_score:
      return 'b'
    elif their_score > my_score:
      return 'c'
