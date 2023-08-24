# Data Engineer Challenge
 
## Damavis 2023

### Introducción

Se plantea un problema donde se debe recorrer con una barra de tamaño `1x3` desde la esquina superior izquierda de un laberinto hasta la esquina inferior derecha. La barra puede moverse en las direcciones básicas y rotar sobre su punto medio. Hemos empleado una estrategia BFS para explorar las posibles soluciones, validando cada movimiento y rotación según las reglas establecidas por la actividad.

### Variables 

- `rows` y `cols`: Representan las dimensiones del laberinto. 
- `visited`: Un conjunto que guarda los nodos que hemos visitado. 
- `q`: Una cola (`deque`) que contiene los nodos pendientes de procesar. Cada nodo tiene información sobre la posición actual de la barra, su orientación y el número de movimientos realizados para llegar allí.

### Estructuras de Datos Utilizadas

1. **Conjunto (`set`)**: Esencial para operaciones de inserción y búsqueda en tiempo constante. Garantiza que no procesemos el mismo estado múltiples veces.
2. **Cola (`deque`)**: Proporciona operaciones en los extremos en tiempo constante. Esencial para la estrategia BFS, donde insertamos estados para procesar y los eliminamos una vez procesados.

### Funciones

1. `valid_move`: Verifica si una posición (r, c) dada es válida para una orientación específica de la barra.
2. `can_rotate`: Determina si es posible rotar la barra en una posición y orientación dadas.

### Estrategia

1. **Evitar procesamiento redundante**: Utilizamos el conjunto `visited` para no procesar un nodo repetidamente. 
2. **Validaciones tempranas**: Hacemos comprobaciones iniciales, como ver si una posición está fuera de los límites. Estas comprobaciones rápidas previenen cálculos innecesarios.
3. **Búsqueda BFS**: Usamos Búsqueda en Amplitud porque buscamos el camino más corto en un espacio sin ponderaciones.

---

### Output

```
nordin@wsl: /mnt/c/Users/nordi/Documents/GitHub/Damavis_Challenge
$ python3 main.py
11 expected: 11
-1 expected: -1
2 expected: 2
16 expected: 16
```

---

Realizado por: Nordin El Balima Cordero