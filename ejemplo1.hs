sumar3 :: Int -> Int -> Int -> Int
sumar3 x y z = x+y+z

promedio :: Fractional a => a -> a -> a
promedio x y = (x+y)/2

signo :: Int -> Int 

signo x |(x>0) = 1
        |(x<0) = (-1)
        |(x==0) = 0
