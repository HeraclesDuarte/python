import pairwise.all_pairs2

all_pairs = pairwise.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""

# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [["Performance_Antigo", "Performance_NOVO"]
            , ["Os_dois_HABILITADOS", "Os_Dois_DESABILITADOS", "Apenas_Novo_habilitado", "Apenas_Antigo_Habilitado"]
            , ["Ingles", "Espanhol", "Portugues"]
            , ["Mozila", "EDGE", "Chrome"]
             , ['ADM, KEY_USER, SINGLE_USER']]

pairwise = all_pairs(parameters)

print("PAIRWISE:")
for i, v in enumerate(pairwise):
    print("%i:\t%s" % (i, str(v)))