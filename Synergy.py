class Kassa(object):
    __amountMoney = 0

    def to_up(self, money):
        self.__amountMoney += money
    
    def count_1000(self):
        print(f'В кассе {self.__amountMoney // 1000} тысяч')
    
    def take_away(self, money):
        if self.__amountMoney >= money:
            self.__amountMoney -= money
        else:
            raise Exception('В кассе недостаточно средств для выдачи')