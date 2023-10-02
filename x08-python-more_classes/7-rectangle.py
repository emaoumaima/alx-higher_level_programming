#!/usr/bin/python3
""" Module for Rectangle class """


class Rectangle:
    """ Rectangle class with width and height attributes """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle

        Args:
            value (int): The new width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle

        Args:
            value (int): The new height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ Returns the printable representation of the rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.width for _ in range(self.height)]
        )

    def __repr__(self):
        """ Returns the string representation of the rectangle """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message  """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
