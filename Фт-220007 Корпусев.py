from num2words import num2words
class Numbers():
    def __init__(self):
        self.number = input('Введите число: ')

    def add_numbers(self):
        rub = ''
        n = ''
        while True:
            if 1<=int(self.number)<=100000:
                if int(self.number)%10==1:
                    rub ='рубль'
                elif int(self.number)%10==2 or int(self.number)%10==3 or int(self.number)%10==4:
                    rub ='рубля'
                elif (int(self.number)%10==5 or int(self.number)%10==6 
                or int(self.number)%10==7 or int(self.number)%10==8 
                or int(self.number)%10==9 or int(self.number)%10==0):
                    rub ='рублей'
                n = num2words(self.number, lang='ru')+' '+rub
                print(n.capitalize())
                break
            else:
                self.number = input('Вы ввели неверное число. Введите число, входящее в диапозон от 1 до 100000: ')
                continue  
a = Numbers()
a.add_numbers()
