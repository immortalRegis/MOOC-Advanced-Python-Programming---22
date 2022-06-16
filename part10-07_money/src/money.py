# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another: 'Money'):
        first = self.__convert_money(self)
        second = self.__convert_money(another)
        return first == second
    
    def __ne__(self, another: 'Money'):
        if self.__eq__(another):
            return False
        return True

    def __lt__(self, another:'Money'):
        first = self.__convert_money(self)
        second = self.__convert_money(another)
        return first < second
    
    def __gt__(self, another:'Money'):
        first = self.__convert_money(self)
        second = self.__convert_money(another)
        return first > second

    
    def __add__(self, another:'Money'):
        first_amount = self.__convert_money(self)
        second_amount = self.__convert_money(another)

        sum = first_amount + second_amount
        euro_part = sum // 100
        cent_part = sum % 100
        return Money(euro_part, cent_part)
    
    def __sub__(self, another:'Money'):
        first_amount = self.__convert_money(self)
        second_amount = self.__convert_money(another)

        if first_amount > second_amount:
            diff = first_amount - second_amount
            euro_part = diff // 100
            cent_part = diff % 100
            return Money(euro_part, cent_part)
        else:
            raise ValueError(f"a negative result is not allowed")

        


    def __convert_money(self, amount:'Money'):
        euro = amount.__euros * 100
        cent = amount.__cents
        return euro + cent


