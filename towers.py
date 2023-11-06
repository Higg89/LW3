n = int(input("Сколько колец у башни? "))
def play(n, a, b, c):
  if n <= 0: return
  play(n - 1, a, c, b)
  print("Переставь диск", n, "со столба", a, "на столб", b)
  play(n - 1, c, b, a)
  
play(n, 'один', 'два', 'три')
