from selenium.webdriver.common.by import By


def find_10_posts(driver):
    els = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_body")
    if len(els) == 10:
        return els
    else:
        return False


# def find_N_elements_located(locator, number):
#     def func(driver):
#         els = driver.find_elements(*locator)
#         if len(els) == number:
#             return els
#         else:
#             return False
#     return func


class find_N_elements_located:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        els = driver.find_elements(*self.locator)
        if len(els) == self.number:
            return els
        else:
            return False


if __name__ == "__main__":
    class A:
        def __init__(self, n):
            self.n = n

        def __call__(self, x):
            return self.n ** x


    pow_of_10 = A(10)
    print(pow_of_10(2))
    pow_of_10(5)

    b = A(2)
    print(b(10))
    print(b(5))
