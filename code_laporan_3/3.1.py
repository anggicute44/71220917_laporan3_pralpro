//deskripsi
var n, i : integer  
var isPrima : boolean  
//deskripsi
INPUT n  
IF (n <= 1) THEN  
    OUTPUT "Bukan Bilangan Prima"  
    STOP  
END IF  
isPrima ← TRUE  
i ← 2  
WHILE (i ≤ sqrt(n)) DO  
    IF (n MOD i = 0) THEN  
        isPrima ← FALSE  
        BREAK  
    END IF  
    i ← i + 1  
END WHILE  
IF (isPrima = TRUE) THEN  
    OUTPUT "Bilangan Prima"  
ELSE  
    OUTPUT "Bukan Bilangan Prima"  
END IF  
