# Test script Ver 1.0
from datetime import datetime


def current_dt():
    """
    Function returns current datetime as "mm/dd/yyyy HH:MM:SS" format
    :return: String of formatted datetime
    """
    return datetime.now().strftime("%m/%d/%y %H:%M:%S")


def greeting(target_dt):
    """
    Function prints greeting sentences
    :param target_dt: String of formatted datetime
    :return: None
    """
    print(f"Hi, there! This is test script for 'basic-algorithm-python' running!")
    print(f"Current datetime is {target_dt}")
    print("I hope you enjoy your day!")
    print("HAPPY CODING:)")


if __name__ == "__main__":
    greeting(current_dt())
