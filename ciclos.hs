



--funcion multipĺicar por 5 todos los elementos
multiplicar5 :: [Int] -> [Int]
--Defino el caso base para cuando la lista sea vacia
multiplicar5 [] = []
-- defino la funcion que divide la lista en Cabeza "X" y Cola "XS"
-- Luego del = toma la cabeza y la multiplica por 5, luego lo agrega a la lista resultante de la cola
multiplicar5 (x:xs) = (x * 5) : (multiplicar5 xs)




soloPares :: [Int] -> [Int] 
-- defino la funcion soloPares, que recibe una lista de enteros y devuelve una lista de enteros
soloPares [] = [] 
-- defino Caso base, cuando "soloPares" reciba una lista [], devuelve una lista vacia
soloPares (x:xs)
--(x:xs) corta la lista, x es la cabeza, xs el resto de la lista
    | even x    = x : soloPares xs  -- | se llama guard y se usa para evaluar condiciones
    -- en este caso llama a even x, si devuelve true, mete a x en la lista de lacola
    | otherwise = soloPares xs      
-- si no se cupmle la condicion de arriba, descarta a x y vuelve a llamar a la funcion para la cola (xs)


sumarListas :: [Int] -> [Int] -> [Int]
sumarListas [] [] = []  -- Caso base: si ambas listas son vacías, la suma es una lista vacía
sumarListas (x:xs) (y:ys) = (x + y) : sumarListas xs ys
sumarListas _ _ = []  -- Si una lista es más larga que la otra, corta la suma
-- Los "_" son COMODINES, no importa el valor de esos parametrs

-- SumarLista caso x = lo que devuelve
-- SumarLista caso y = lo que devuelve
-- cuando los 2 casos, el base y el (x:xs)(y:ys), no se cumplan, se va a ejecutar el ultimo, esto significa que
-- ya se llego al final de 1 de las 2 listas entonces, una es vacia
-- entonces no se cumple ni el primer caso ni el segundo, entonces llega al ultimo
-- y ejecuta sin importar lo que tenga, devuelve lista vacia

--Ejercicios
-- 1)
-- A)
pares :: [Int] -> [Int]
pares [] = []
pares (x:xs)
    | (mod x 2) == 0 = x : pares xs
    | otherwise =  pares xs


-- B)
mayores10 :: [Int] -> [Int]
mayores10 [] = []
mayores10 (x:xs) 
    | (x > 10) = x : mayores10 xs
    | otherwise = mayores10 xs
-- divido la lista que vino como parametro en cabeza y cola, y hago un if x > 10, else


-- C)
mayoresQue :: Int -> [Int] -> [Int]
mayoresQue n [] = [] --(*1)
mayoresQue n (x:xs)
    | x > n = x : mayoresQue n xs --(*2)
    | otherwise = mayoresQue n xs --(*3)
-- Compilacion escrita?
--mayoresQue 3 [5,2,10]
-- = por definicion de (*2), n := 3, x:= 5, xs := [2,10] *(porque  5 > n)
--  5 : mayoresQue 3 [2,10]
-- = por definicion de (*3), n := 3, x:= 2, xs := [10] *(porque  2 < n)
--  5 : mayoresQue 3 [10]
-- = por definicion de (*2), n := 3, x:= 10, xs := [] *(porque  10 > n)
--  5 : 10 : mayoresQue 3 []
-- = por definicion de (*1),5:10:[]
-- = por defiicion de ":", 10:[] = [10]
-- = por defincion de ":", 5:[10] = [5,10]





--Se puede hacer una funcion parfa calcular el factorial de un numero
fact :: Int -> Int
fact 1 = 1
fact n = n * fact (n - 1)

-- 4)

-- a)

-- Funcion sumar 1 a cada elemnto de la lista
sumar1 :: [Int] -> [Int]
sumar1 [] = []
sumar1 (x:xs) = (x + 1) : (sumar1 xs)

--b) duplica
duplica :: [Int] -> [Int]
duplica [] = []
duplica (x:xs) = x * 2 : duplica xs

--c) Multiplica una lista por n
multi :: Int -> [Int] -> [Int]
multi n [] = []
multi n (x:xs) = x * n : multi n xs

--5)
--a) menores a 10
todosMenores :: [Int] -> Bool
todosMenores [] = True
todosMenores (x:xs) 
    | x < 10 = todosMenores xs
    | otherwise = False 

--b) hay ceros
hay0 :: [Int] -> Bool
hay0 [] = False
hay0 (x:xs)
    |x==0 = True
    |otherwise= hay0 xs

--c)sumatoria
sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs


--6) 
repartir :: [String] -> [String] -> [(String,String)]
repartir [] [] = []
repartir (x:xs) (y:ys) = (x,y) : repartir xs ys
repartir _ _ = [] 
