input
//Deklarasi:
    var n, hasil, i: integer

//Deskripsi:
    INPUT n
    IF (n < 0) THEN
        OUTPUT "Bilangan harus ≥ 0"
    ELSE
        hasil ← 1
        FOR i ← 1 TO n DO
            hasil ← hasil * i
        ENDFOR
        OUTPUT "Nilai faktorial dari ", n, " adalah ", hasil
    ENDIF
