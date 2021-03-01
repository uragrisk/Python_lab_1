class Cup:
    location = "on the table"

    @staticmethod
    def getLocation():
        return Cup.location

    def __init__ (self, volume = 250, material = "plastic", color = "red"):
      self.volume = volume
      self.material = material
      self.color = color

    def __del__ (self):
      pass

    def __str__(self):
     return("There is " + self.material  + " " + self.color  \
     + " cup, with a volume of " + str(self.volume) + " milliliters ")




