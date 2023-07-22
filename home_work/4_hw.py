class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
# S=a*b

s = Rectangle(2, 3)
print("Площадь " + str(s.height * s.width))

# P=a+b+c+d, P=2(a+b)

print("Периметр " + str(2*(s.height + s.width)))


s1 = Rectangle(3, 4)
print("Площадь " + str(s1.height * s1.width))
print("Периметр " + str(2*(s1.height + s1.width)))


s2 = Rectangle(12, 37)
print("Площадь " + str(s2.height * s2.width))
print("Периметр " + str(2*(s2.height + s2.width)))



# task2



class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

c = Math(20, 5)

print(c.a + c.b)
print(c.a * c.b)
print(c.a // c.b)
print(c.a - c.b)



#task_3


class Button:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)


text_box = Button('Text Box ', 'Кнопка', ' ')
check_box = Button('Check Box ', 'Кнопка', ' ')
radio_button = Button('Radio Button ', 'Кнопка', ' ')
web_tables = Button('Web Tables ', 'Кнопка', ' ')
buttons = Button('Buttons ', 'Кнопка', ' ')
links = Button('Links ', 'Кнопка', ' ')
broken_links_images = Button('Broken Links - Images ', 'Кнопка', ' ')
upload_and_download = Button('Upload and Download ', 'Кнопка', ' ')
dynamic_properties = Button('Dynamic Properties ', 'Кнопка', ' ')




print(text_box.text, text_box.type, text_box.loc)
print(text_box.click())
print(check_box.text, check_box.type, check_box.loc)
print(check_box.click())
print(radio_button.text, radio_button.type, radio_button.loc)
print(radio_button.click())
print(web_tables.text, web_tables.type, web_tables.loc)
print(web_tables.click())
print(buttons.text, buttons.type, buttons.loc)
print(buttons.click())
print(links.text, links.type, links.loc)
print(links.click())
print(broken_links_images.text, broken_links_images.type, broken_links_images.loc)
print(broken_links_images.click())
print(upload_and_download.text, upload_and_download.type, upload_and_download.loc)
print(upload_and_download.click())
print(dynamic_properties.text, dynamic_properties.type, dynamic_properties.loc)
print(dynamic_properties.click())










