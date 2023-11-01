#!/usr/bin/env python
# coding: utf-8

# In[2]:


def evaluar_notacion_polaca(expresion):
    pila = []
    operadores = set(['+', '-', '*', '/'])
    
    for token in expresion.split():
        if token not in operadores:
            pila.append(float(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("División por cero")
                resultado = a / b
            pila.append(resultado)
    
    if len(pila) == 1:
        return pila[0]
    else:
        raise ValueError("Expresión no válida")

expresion1 = "3 4 + 2 *"
expresion2 = "5 1 2 + 4 * + 3 -"
expresion3 = "2 3 * 5 4 * + 9 -"

resultado1 = evaluar_notacion_polaca(expresion1)
resultado2 = evaluar_notacion_polaca(expresion2)
resultado3 = evaluar_notacion_polaca(expresion3)

print(f"Resultado 1: {resultado1}")
print(f"Resultado 2: {resultado2}")
print(f"Resultado 3: {resultado3}")


# In[4]:


def evaluar_notacion_polaca2(expresion):
    pila = []
    operadores = set(['+', '-', '*', '/'])
    
    for token in expresion.split():
        if token not in operadores:
            pila.append(float(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("División por cero")
                resultado = a / b
            pila.append(resultado)
    
    if len(pila) == 1:
        return pila[0]
    else:
        raise ValueError("Expresión no válida")

expresion1 = "4 5 + 2 3 + *"
expresion2 = "6 7 + 2 3 + * 2 /"
expresion3 = "8 2 / 4 6 - * 3 +"

resultado1 = evaluar_notacion_polaca2(expresion1)
resultado2 = evaluar_notacion_polaca2(expresion2)
resultado3 = evaluar_notacion_polaca2(expresion3)

print(f"Resultado 1: {resultado1}")
print(f"Resultado 2: {resultado2}")
print(f"Resultado 3: {resultado3}")


# In[7]:


def evaluar_notacion_polaca3(expresion):
    pila = []
    operadores = set(['+', '-', '*', '/'])
    
    for token in expresion.split():
        if token not in operadores:
            pila.append(float(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("División por cero")
                resultado = a / b
            pila.append(resultado)
    
    if len(pila) == 1:
        return pila[0]
    else:
        raise ValueError("Expresión no válida")


expresion1 = "3 4 + 5 6 - *"
expresion2 = "2 7 / 3 8 + *"
expresion3 = "9 2 * 4 5 - /"

resultado1 = evaluar_notacion_polaca3(expresion1)
resultado2 = evaluar_notacion_polaca3(expresion2)
resultado3 = evaluar_notacion_polaca3(expresion3)

print(f"Resultado 1: {resultado1}")
print(f"Resultado 2: {resultado2}")
print(f"Resultado 3: {resultado3}")


# In[ ]:




