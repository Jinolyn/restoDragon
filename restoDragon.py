#!/usr/bin/env python3
from abc import ABC, abstractmethod

# Class Menu
#
class Menu(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass


#subject class
class SubjectObservable(ABC):
    @abstractmethod
    def attach(self, observer_type):   # add an observer
        pass
	
    @abstractmethod
    def detach(self, observer_type):  # remove an observer
        pass
	
    @abstractmethod
    def order(self, number_command):
        pass
		

# Observer class
class Observer(ABC):
    @abstractmethod
    def notify_boss(self):
        pass



# RamenSoup
#
class RamenSoup(Menu, SubjectObservable):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.description = "Ramen Soup"
            cls._instance.price = 10
            cls._instance.quantity = 10
            cls._instance.observers_lists = []
        return cls._instance

    def get_description(self):
        return self.description

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def attach(self, observer_type):
        self.observers_lists.append(observer_type)

    def detach(self, observer_type):
        self.observers_lists.remove(observer_type)
    
    def order(self, number_command):
        cond1 = (number_command >= self.quantity) and (self.quantity >0)
        cond2 = (number_command < self.quantity) 
        if cond1:
            self.quantity -= number_command
            if self.quantity <= 0:
                return send_nofitication(self.observers_lists)

        elif cond2:
            self.quantity -= number_command  
            print(f"Commande passe: {number_command} {self.description}. Price: ${self.price * number_command}")
            print(f"stock: {self.quantity}")
            

# Sushi
#
class Sushi(Menu, SubjectObservable):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.description = "Sushi"
            cls._instance.price = 75   # price in dollar
            cls._instance.quantity = 15
            cls._instance.observers_lists = []
        return cls._instance

    def get_description(self):
        return self.description

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def attach(self, observer_type):
        self.observers_lists.append(observer_type)

    def detach(self, observer_type):
        self.observers_lists.remove(observer_type)
    
    def order(self, number_command):
        cond1 = (number_command >= self.quantity) and (self.quantity >0)
        cond2 = (number_command < self.quantity) 
        if cond1:
            print(f"Commande passe_Tems: {number_command} {self.description}. Price: ${self.get_price() * number_command}")
            if self.quantity <= 0:
                return send_nofitication(self.observers_lists)
        elif cond2:
            self.quantity -= number_command  
            print(f"Commande passe: {number_command} {self.description}. Price: ${self.get_price() * number_command}")
            print(f"stock: {self.quantity}")
            
# Accompagnement
#
class Accompagnement(Menu):
    def __init__(self, menu):
        self.menu = menu

    def get_description(self):
        return self.menu.get_description()

    def get_price(self):
        return self.menu.get_price()

    def get_quantity(self):
        pass

    def command(self):
        if self.menu.quantity <= 0:
            print(f"{self.menu.description} is sold out")
        else:
            self.menu.quantity -=1
            print(f"Commande passe: {self.get_description()}. Price: {self.get_price()}")

class Rice(Accompagnement):
    def get_description(self):
        return super().get_description() + " with Rice"
    def get_price(self):
        return f"${super().get_price() + 1}"
    def get_quantity(self):
        return super().get_quantity()


class Noodle(Accompagnement):
    def get_description(self):
        return super().get_description() + ' with noodle'

    def get_price(self):
        return f"${super().get_price() + 2}"


    def get_quantity(self):
        pass


class Vegetables(Accompagnement):
    def get_description(self):
        return super().get_description() + ' with vegetables'

    def get_price(self):
        return f"${super().get_price() + 2}"

    def get_quantity(self):
        pass

# class 
class SMSObserver(Observer):
    def notify_boss(self):
        print("SMS sent to Boss : 'This menu is sold out.'")

class EmailObserver(Observer):
    def notify_boss(self):
        print("Email send to Boss : 'This menu is sold out.")


#
def send_nofitication(receivers:list):
    for receiver in receivers:
        receiver.notify_boss()


if __name__ == "__main__":
    ramen_soup = RamenSoup()
    sushi = Sushi()
    sms_observer = SMSObserver()
    email_observer = EmailObserver()

    ramen_soup.attach(sms_observer)
    ramen_soup.attach(email_observer)
    sushi.attach(sms_observer)
    sushi.attach(email_observer)

    # simple command
    ramen_soup.order(3)
    ramen_soup.order(5)
    sushi.order(5)

    print('')
    accNoodleRamenSoup = Noodle(ramen_soup)
    accNoodleSushi = Noodle(sushi)

    accRiceRamenSoupe = Rice(ramen_soup)
    accRiceSushi = Rice(sushi)

    accVegetableRamenSoup = Vegetables(ramen_soup)
    accVegetableSushi = Vegetables(sushi) 

    # command with accompaniment
    accRiceRamenSoupe.command()
    accRiceSushi.command()
    accNoodleRamenSoup.command()
    accNoodleSushi.command()
    accVegetableRamenSoup.command()
    accVegetableSushi.command()
    

# TODO : review logic in order bloc    
    
