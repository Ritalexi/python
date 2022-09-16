class Square:
    """nstantiation with optional size
       raising exceptions
    """
    
    @property
    def size(self):
        """Getter that gets the integer size
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter that sets
        """
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Getter for the function position
        """
        return self.__size

    @position.setter
    def position(self, value):
        """Setter for the function position
        """
        self.__position = value
        for i in self.__position:
            if i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """Square instantiation and rise exxcetions
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Finding the area
        """
        return(self.__size * self.__size)

    def my_print(self):
        """function to print symbol
        """
        space = " "
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(space * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
