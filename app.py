class Kalkulacka:

  @staticmethod
  def secti(a: float, b: float) -> float:
    """Funkce pro scitani cisel"""
    return a + b
  
  @staticmethod
  def odecti(a: float, b: float) -> float:
    """Funkce pro odcitani cisel"""
    return a - b
  
  @staticmethod
  def nasobeni(a: float, b: float) -> float:
    """Funkce pro nasobeni"""
    return a * b

  @staticmethod
  def deleni(a: float, b: float) -> float:
    """Funkce pro deleni"""
    return a / b

  @staticmethod
  def modulo(a, b):
    return a % b

def main():
  assert Kalkulacka.secti(2, 3) == 5

if __name__ == "__main__":
  main()
