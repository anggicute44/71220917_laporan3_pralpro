# Memasak mie instan
//deskripsi
INPUT air ke panci
kompor_disable ← false  # Nyalakan kompor
IF air == mendidih THEN
    INPUT mie instan ke dalam panci
END IF
IF mie == matang THEN
    kompor_disable ← true  # Matikan kompor
    INPUT bumbu ke dalam panci
END IF
OUTPUT mie instan
