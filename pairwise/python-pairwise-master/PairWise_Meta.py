import pairwise.all_pairs2

all_pairs = pairwise.all_pairs2.all_pairs2

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""

# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html


parameters = [["Performance_Antigo", "Performance_Beta"]
            , ["Ingles", "Espanhol", "Portugues"]
            , ["Mozila", "EDGE", "Chrome"]
            , ["TODOS_PARAMETROS_HABILITADOS", "TODOS_PARAMETROS_DESABILITADOS"]
 #           , ['ADM, USER, BASICO']
            , ['APENAS_PERFORMANCE_ANTIGO_LIGADO, APENAS_PERFORMANCE_BETA_LIGADO']]

pairwise = all_pairs(parameters)

print("PAIRWISE:")
for i, v in enumerate(pairwise):
    print("%i:\t%s" % (i, str(v)))