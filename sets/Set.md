Em Python, **`set`** é um tipo de dado embutido que representa um **conjunto**. Ele é usado para armazenar coleções de itens **únicos** e **não ordenados**. Um conjunto pode ser útil para evitar duplicatas e realizar operações matemáticas de conjuntos, como interseção, união e diferença.

### Características de um `set`:
1. **Elementos únicos:** Um conjunto não pode conter itens duplicados.
2. **Não ordenado:** A ordem dos elementos não é garantida.
3. **Mutável:** Você pode adicionar ou remover elementos de um conjunto.
4. **Iterável:** Pode ser percorrido em um loop.

---

### Criando um `set`

1. **Usando chaves `{}`:**
   ```python
   meu_set = {1, 2, 3, 4}
   print(meu_set)  # {1, 2, 3, 4}
   ```

2. **Usando a função `set()`:**
   ```python
   meu_set = set([1, 2, 3, 4])  # A partir de uma lista
   print(meu_set)  # {1, 2, 3, 4}
   ```

3. **Criando um conjunto vazio:**  
   Use `set()` (não `{}` — isso cria um dicionário vazio):
   ```python
   vazio = set()
   print(vazio)  # set()
   ```

---

### Operações Comuns com `set`

#### 1. Adicionar e Remover Elementos
```python
meu_set = {1, 2, 3}
meu_set.add(4)       # Adiciona um elemento
print(meu_set)       # {1, 2, 3, 4}

meu_set.remove(2)    # Remove um elemento (gera erro se não existir)
print(meu_set)       # {1, 3, 4}

meu_set.discard(5)   # Remove um elemento (não gera erro se não existir)
print(meu_set)       # {1, 3, 4}
```

#### 2. Verificar Presença de Elementos
```python
meu_set = {1, 2, 3}
print(2 in meu_set)   # True
print(5 in meu_set)   # False
```

#### 3. Operações de Conjuntos
```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # União: {1, 2, 3, 4, 5}
print(A & B)  # Interseção: {3}
print(A - B)  # Diferença: {1, 2}
print(A ^ B)  # Diferença simétrica: {1, 2, 4, 5}
```

#### 4. Tamanho de um Conjunto
```python
meu_set = {1, 2, 3, 4}
print(len(meu_set))  # 4
```

---

### Conjuntos Imutáveis: `frozenset`

Se você precisar de um conjunto que não pode ser modificado, pode usar o tipo **`frozenset`**:
```python
fs = frozenset([1, 2, 3])
print(fs)  # frozenset({1, 2, 3})

# fs.add(4)  # Isso geraria um erro, pois o frozenset é imutável.
```

---

### Aplicações de `set`

1. **Remover duplicatas de uma lista:**
   ```python
   lista = [1, 2, 2, 3, 4, 4, 5]
   unicos = set(lista)
   print(unicos)  # {1, 2, 3, 4, 5}
   ```

2. **Filtrar itens únicos em dados:**
   ```python
   nomes = ["Ana", "João", "Ana", "Carlos"]
   nomes_unicos = set(nomes)
   print(nomes_unicos)  # {'Ana', 'João', 'Carlos'}
   ```

3. **Verificar interseções em coleções:**
   ```python
   convidados1 = {"Ana", "Carlos", "Pedro"}
   convidados2 = {"Carlos", "João", "Ana"}
   comuns = convidados1 & convidados2
   print(comuns)  # {'Ana', 'Carlos'}
   ```

---
