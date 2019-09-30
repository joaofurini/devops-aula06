def calculaPrimo(n):
  cont_divisores = []
  divisor = 0
  while (len(cont_divisores) < n):
      if divisor == 2 or (divisor != 1 and divisor % 2 == 1):
          cont_divisores.append(divisor)
          divisor +=1
      else:
        divisor +=1
  return cont_divisores
  
print(calculaPrimo(int(input("Digite um numero: "))))


