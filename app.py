from math import inf

def vynasob(a: float, b: float) -> float:
  return a * b

def vydel(a: float, b: float) -> float:
  if b == 0:
    return inf
  else:
    return a/b

def odecti(a: float, b: float) -> float:
  return a - b

def secti(a: float, b: float) -> float:
  return a + b

def main():
  print(secti(a=5, b=3))

# git commit -am "Pridal funkci na odecitani"
# git push

#git fetch origin 
#git checkout 1-deleni-neni-bezpecne

# git branch
# git switch main