# Definición de estados
q0 : INICIO
q1 : CALCULAR_FIBONACCI
q2 : ESCRIBIR_FIBONACCI
q3 : FIN

# Definición de símbolos
0
1
2
3
4
5
6
7
8
9
a : número impar
b : número par
+ : suma
- : resta
* : multiplicación
_ : espacio vacío
x : marca

# Definición de transiciones
q0, 0 -> q1, b, >
q0, 1 -> q2, 1, >
q1, 0 -> q1, a, >
q1, 1 -> q1, b, >
q1, 2 -> q1, a, >
q1, 3 -> q1, b, >
q1, 4 -> q1, a, >
q1, 5 -> q1, b, >
q1, 6 -> q1, a, >
q1, 7 -> q1, b, >
q1, 8 -> q1, a, >
q1, 9 -> q1, b, >
q1, _ -> q2, 0, <
q2, 1 -> q2, 1, <
q2, a -> q2, a, <
q2, b -> q2, b, <
q2, + -> q3, +, <
q3, a -> q0, a, >
q3, b -> q0, b, >
q3, + -> q3, +, <
