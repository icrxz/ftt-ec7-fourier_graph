#Comunicação de Dados - N1 - 1° Bimestre
#Igor Cruz Avelino
#RA: 081170008
#EC-7

import numpy as np
import matplotlib.pyplot as plt


class FourierFunction(object):

  def __init__(self, terms):
    RA = 8
    self._f0 = 100 * RA
    self._w0 = 2 * np.pi * self._f0
    self._terms = terms - 1
    self._ticks = self.def_ticks()
    self.x = []
    self.y = []
    self.def_xy()

  def def_xy(self):
    for t in self._ticks:
      self.x.append(t)
      self.y.append(self.calc_y(t))

  def def_ticks(self):
    min_freq = 1 / (self._f0)
    max_freq = 5 / (self._f0)
    step_freq = (max_freq - min_freq) / 1000
    return np.arange(min_freq, max_freq, step_freq)

  def calc_y(self, t):
    first_term = 1 / 2
    sum = 0
    for x in range(1, self._terms * 2, 2):
      sum += self.get_terms(x, t)
    return first_term + ((2 / np.pi) * sum)

  def get_terms(self, x, t):
      return (1 / x) * np.sin(x * self._w0 * t)


def initialize():
  while True:
    terms = int(input("Quantidade de termos: "))
    if terms <= 0:
      return 0
    plt.title(f"Função com {terms} termo(s)")
    func = FourierFunction(terms)
    plt.plot(func.x, func.y)
    plt.xlabel("Frequência")
    plt.show()

initialize()
