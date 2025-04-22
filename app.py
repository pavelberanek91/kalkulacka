class Kalkulacka:

  @staticmethod
  def secti(a, b):
    return a + b
  
  @staticmethod
  def odecti(a, b):
    return a - b
  
  @staticmethod
  def nasobeni(a, b):
    return a * b

  @staticmethod
  def deleni(a, b):
    return a / b

  @staticmethod
  def modulo(a, b):
    return a % b

def main():
  assert Kalkulacka.secti(2, 3) == 5

if __name__ == "__main__":
  main()