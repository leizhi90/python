# -*- conding:utf-8 -*-
class Box:
      def __init__(self, length, width, height):
            self.length = length
            self.width = width
            self.height = height

      # def __init__(self, box):

      @classmethod
      def copy(cls, box):
            return cls(box.length, box.width, box.height)
#****************TypeError: __init__() missing 1 required positional argument: 'height'

b1 = Box(5, 3, 2)
b2 = Box.copy(b1)
