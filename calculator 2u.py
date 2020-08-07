#calculator
while True:
   try:
      user_input=input('\nNumber: ')
      print('\n')
      tt=user_input.split(' ')
      if tt[1] == '+': print(f'{tt[0]} + {tt[2]} = {int(tt[0]) + int(tt[2])}')
      elif tt[1] == '-': print(f'{tt[0]} - {tt[2]} = {int(tt[0]) - int(tt[2])}')
      elif tt[1] == '*': print(f'{tt[0]} * {tt[2]} = {int(tt[0]) * int(tt[2])}')
      elif tt[1] == '/':
         for x in range(2,3):
            ttl=int(tt[0]) / int(tt[2])
            if ttl % x == 0:
               print(f'{tt[0]} / {tt[2]} = {int(ttl)}')
               break
            else:
               print(f'{tt[0]} / {tt[2]} = {float(ttl)}')
               break
   except IndexError: print(f'input number, for example 34 + 5')