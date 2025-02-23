
//Deklarasi:
    var a, b, c, D : float

//Deskripsi:
    INPUT a, b, c
    IF (a = 0) THEN
        OUTPUT "Bukan persamaan kuadrat"
    ELSE
        D ← (b^2 - 4 * a * c)
        IF (D > 0) THEN
            OUTPUT "Akar Real dan Berlainan"
        ELSE IF (D = 0) THEN
            OUTPUT "Akar Real dan Kembar"
        ELSE
            OUTPUT "Akar Imajiner/Tidak Real"
        ENDIF
    ENDIF
END
