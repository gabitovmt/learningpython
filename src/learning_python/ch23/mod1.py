X = 1
import mod2
print(X, end=' ')       # Собственное глобальное имя X
print(mod2.X, end=' ')  # X из mod2
print(mod2.mod3.X)      # X из вложенного mod3
