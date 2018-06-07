def split(string):
   run = []
   for char in string:
      run.append(char)
   return run

def binary(num, dec_inp = True):
   '''Converts decimal into binary (or Vice Versa)'''
   if dec_inp:
      run = ''
      while num > 0:
         run += '01'[int(num%2)]
         num = (num - num%2) / 2
      return int(run[::-1])
   else:
      run = 0
      num = split(str(num))
      runB = 1
      while len(num) > 0:
         poof = int(num.pop())
         run += poof*runB
         runB *= 2
      return run

if __name__ == '__main__':
   print(binary(10011, False))
