makeSeqList x y = [x..y]
makeWholeList x = makeSeqList 1 x 
findElem x i =  x !! i
lastElem x = x !! length x
listLength [] = 0 
listLength (x:xs) = 1 + listLength xs 
concatList x y = x ++ y
reverseList [] = []
reverseList (x:xs) = reverseList xs ++ [x]
minList [x] = x
minList (x:y:xs) = if x<y then minList(x:xs) else minList(y:xs)
maxList [x] = x
maxList (x:y:xs) = if x>y then maxList (x:xs) else maxList(y:xs)
evenList [] = []
evenList (x:y:xs) = x : evenList xs 
oddList [x] = []
oddList (x:y:xs) = y : oddList xs 
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys) = if x <= y then x: merge xs (y:ys) else y: merge (x:xs) ys
mergeSort [] = [] 
mergeSort [x] = [x] 
mergeSort xs = let (as, bs) = splitAt (length xs `quot` 2) xs in merge (mergeSort as) (mergeSort bs)