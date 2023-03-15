import random

from hw10_q1 import Instrument
class Musician:
    def __init__(self, stage_name, gear):
        self.stage_name = stage_name
        self.instruments= gear
        self.number_of_instruments = len(gear)
    def __str__(self):
        str_new = ""
        i = 0
        for string in self.instruments:
            if i < self.number_of_instruments-1:
               str_new += str(string) + ", "
               i += 1
            else:
               str_new += "and " + str(string)
        return "Musician object '{}', owning a {}". format(self.stage_name, str_new)

    def pick_instrument(self,instrument_index):
      if instrument_index is None:
          return self.instruments[random.randint(0, self.number_of_instruments)]
      else:
          if self.number_of_instruments == 0:
            return None
          else:
            if instrument_index > self.number_of_instruments:
                return self.instruments[self.number_of_instruments-1]
            elif instrument_index < self.number_of_instruments:
                return self.instruments[instrument_index]

# Creating our Instrument objects
def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]

# Creating our Musician object
    sad_musician = Musician("Robert Smith", gear)
# Checking the Musician object's attributes
    print(sad_musician.stage_name)
    print(sad_musician.number_of_instruments)
    for instrument in sad_musician.instruments:
      print(instrument)

# 2. Checking the printing result for sad_musician
    print(sad_musician)

# 3.
    instrument = sad_musician.pick_instrument(0)
    print(instrument)
    instrument = sad_musician.pick_instrument(100000000)
    print(instrument)
    instrument = sad_musician.pick_instrument(None)
    print(instrument)

main()