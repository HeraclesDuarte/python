import pairwise.all_pairs2

all_pairs = pairwise.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""

# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [["Painel Beta", "Painel Antigo"]
            , ["SET_BCO = 1 Para Beta", "SET_BCO = 0 Para Beta"]
            , ["Ingles", "Portugues", "Espanhol"]
            , ["Permisão Beta = 1", "Painel de Permisão Beta = 0",
               "Painel de Permisão Beta = 2", "Painel de Permisão Beta = VAZIO"]]


pairwise = all_pairs(parameters)

print("PAIRWISE:")
for i, v in enumerate(pairwise):
    print("%i:\t%s" % (i, str(v)))