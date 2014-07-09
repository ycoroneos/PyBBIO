
from bbio import *
from RotaryEncoder import RotaryEncoder

encoder = RotaryEncoder(RotaryEncoder.EQEP2b)

def setup():
  encoder.setAbsolute()
  encoder.zero()
  
def loop():
  print encoder.getPosition()
  delay(1000)
  
run(setup, loop)