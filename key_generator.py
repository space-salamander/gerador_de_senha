import string as st

import numpy as np

letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
juncao = (letras+numeros+especial)
senha = np.random.choice(list(juncao), 12)
print(''.join(senha))


'''print(letras)
print(numeros)
print(especial) '''