import math

K = 1.0

a1 = 2.0
a2 = 3.0

T = -4.605 / min(a1, a2)

e_ss = 1.0 / K

print(f"Tempo de assentamento: {T:.2f}s")
print(f"Erro estacionário: {e_ss:.2f}")