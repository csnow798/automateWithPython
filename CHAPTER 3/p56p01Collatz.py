def collatz(number):
              if number%2==1:
                            num=3*number+1
                            print(num)
                            return num
              elif number % 2 == 0:
                            num=number//2
                            print(num)
                            return num
              
n = int(input('Enter a number: \n'))  
while True:
              #try:
              n=collatz(n)
              #except ValueError:
              #              print('Tpye error, please input integer only.')
              if n==1:
                            break
#input verification not  unimplemented
              
