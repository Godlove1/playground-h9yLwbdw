#Ne pas oublier de changer le module à importer
from stat_moyenne2 import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
(([1,4,10],[1,1,1]),5.),\
(([4,4,4,4],[1,6,9,2]),4.),\
(([20, 17, 17, 6, 16, 4, 5, 5, 18, 10, 1, 14, 12, 7, 10, 20, 12, 1, 1, 8, 16, 15, 6, 6, 4, 20, 8, 3, 6, 3, 17, 17, 1, 1, 14, 6, 17, 10, 8, 3, 2, 18, 10, 3, 14, 18, 16, 11, 17, 20, 6, 4, 17, 3, 18, 10, 13, 8, 14, 11, 6, 8, 1, 3, 1, 11, 15, 4, 17, 12, 15, 4, 15, 1, 9, 14, 6, 8, 18, 7, 19, 5, 2, 11, 16, 16, 5, 6, 16, 11, 14, 12, 13, 9, 2, 8, 17, 9, 19, 14, 11, 19, 5, 3, 12, 1, 9, 14, 5, 2, 6, 4, 3, 4, 5, 8, 20, 5, 7, 13, 11, 19, 16, 17, 4, 16, 15, 6, 20, 15, 5, 14, 13, 7, 13, 11, 14, 18, 17, 10, 2, 6, 5, 15, 10, 1, 11, 15, 19, 19, 17, 17, 14, 5, 19, 5, 3, 3, 14, 16, 8, 7, 2, 3, 10, 6, 7, 17, 20, 16, 4, 17, 14, 13, 12, 3, 17, 9, 2, 14, 1, 2, 10, 8, 7, 9, 3, 14, 10, 18, 16, 17, 2, 14, 15, 1, 11, 10, 6, 7, 5, 5, 11, 4, 14, 17, 1, 17, 8, 10, 3, 12, 12, 5, 3, 10, 17, 20, 7, 4, 6, 7, 12, 18, 17, 16, 15, 4, 20, 5, 10, 4, 17, 3, 9, 16, 7, 20, 13, 15, 17, 12, 20, 16, 18, 6, 1, 8, 7, 9, 4, 1, 7, 17, 2, 14, 12, 8, 9, 8, 13, 19, 7, 19, 18, 12, 13, 7, 17, 17, 20, 2, 1, 7, 13, 20, 19, 4, 19, 5, 12, 19, 7, 13, 13, 5, 12, 8, 20, 15, 7, 13, 3, 5, 14, 1, 4, 14, 5, 19, 12, 4, 14, 18, 12, 5, 6, 6, 10, 20, 7, 9, 7, 4, 11, 13, 4, 17, 8, 13, 8, 3, 10, 11, 7, 5, 12, 1, 1, 11, 17, 9, 12, 11, 5, 15, 16, 12, 12, 19, 10, 9, 16, 16, 4, 15, 2, 10, 20, 10, 15, 14, 19, 13, 14, 15, 9, 15, 17, 9, 7, 15, 17, 4, 15, 19, 17, 16, 18, 19, 5, 7, 10, 14, 17, 10, 2, 5, 16, 7, 15, 13, 9, 20, 17, 9, 14, 17, 3, 6, 2, 6, 13, 13, 11, 7, 18, 2, 12, 4, 19, 20, 16, 18, 20, 9, 2, 18, 17, 5, 17, 20, 14, 2, 9, 18, 7, 9, 8, 3, 15, 13, 14, 12, 20, 1, 13, 9, 10, 1, 12, 1, 19, 20, 18, 1, 19, 10, 17, 11, 14, 2, 14, 8, 19, 19, 5, 15, 20, 5, 19, 9, 1, 11, 16, 1, 6, 17, 4, 16, 2, 18, 11, 14, 16, 8, 17, 19, 20, 1, 1, 11, 19, 12, 18, 7, 9, 9, 1, 17, 8, 16, 11, 2, 19, 1, 16, 1, 6, 19, 4, 13, 1, 7, 5, 20, 9, 1, 15, 7, 6, 9, 19, 17, 18, 18, 9, 4, 9, 6, 12, 20, 6, 1, 9, 20, 12, 15, 2, 12, 5, 17, 16, 3, 11, 10, 16, 18, 2, 7, 17, 17, 16, 4, 18, 12, 15, 4, 20, 10, 8, 7, 16, 3, 12, 10, 8, 4, 15, 9, 10, 15, 12, 18, 15, 7, 7, 7, 17, 17, 15, 7, 14, 20, 15, 19, 12, 6, 4, 15, 11, 12, 15, 16, 2, 9, 12, 13, 20, 11, 13, 15, 4, 18, 4, 11, 17, 15, 10, 17, 5, 15, 12, 9, 19, 13, 16, 2, 19, 7, 8, 12, 19, 15, 13, 10, 7, 17, 1, 8, 1, 15, 13, 2, 15, 20, 5, 6, 8, 5, 1, 11, 1, 20, 3, 10, 6, 8, 15, 17, 5, 15, 19, 10, 18, 18, 7, 4, 14, 10, 18, 7, 11, 11, 14, 17, 14, 8, 6, 19, 17, 3, 10, 17, 10, 17, 8, 6, 4, 11, 6, 17, 9, 9, 11, 2, 5, 1, 12, 2, 16, 6, 8, 15, 14, 12, 11, 1, 15, 9, 4, 13, 3, 17, 9, 2, 6, 14, 18, 15, 5, 16, 5, 11, 9, 7, 10, 11, 13, 2, 7, 1, 5, 17, 9, 1, 3, 5, 9, 13, 13, 17, 1, 18, 14, 2, 5, 1, 20, 5, 5, 2, 4, 12, 11, 20, 13, 3, 1, 15, 5, 1, 9, 12, 14, 5, 6, 2, 5, 17, 3, 6, 8, 7, 20, 6, 16, 3, 1, 6, 18, 19, 5, 10, 14, 16, 19, 15, 11, 14, 16, 5, 1, 5, 10, 16, 10, 6, 19, 1, 6, 17, 3, 6, 8, 4, 3, 7, 13, 8, 6, 8, 8, 18, 7, 11, 16, 18, 9, 18, 6, 13, 17, 5, 18, 8, 18, 5, 2, 12, 12, 15, 13, 18, 9, 15, 15, 15, 17, 16, 1, 6, 17, 12, 10, 13, 4, 3, 5, 12, 1, 9, 19, 10, 13, 14, 17, 1, 6, 5, 11, 18, 5, 16, 8, 9, 6, 6, 19, 17, 11, 6, 15, 14, 11, 9, 18, 14, 10, 16, 19, 12, 8, 15, 20, 2, 18, 3, 4, 6, 11, 13, 7, 13, 18, 16, 15, 9, 6, 6, 4, 7, 13, 15, 10, 7, 15, 16, 3, 8, 6, 10, 6, 19, 15, 12, 12, 15, 1, 16, 17, 17, 14, 7, 12, 4, 11, 4, 7, 10, 15, 5, 17, 8, 6, 3, 8, 19, 7, 14, 4, 9, 13, 11, 12, 1, 12, 8, 10, 17, 16, 17, 13, 17, 3, 11, 17, 16, 11, 3, 4, 9, 18, 1, 18, 11, 8, 20, 20, 20, 1, 19, 1, 19, 5, 13, 15, 19, 10, 16, 4, 2, 11, 11, 18, 2, 18, 18, 5, 14, 3, 13, 2, 15, 9, 16, 12, 2, 14, 16, 12, 4, 9, 10, 10, 2, 15, 14, 15, 8, 16, 15, 15, 9, 12, 3, 20, 3, 8, 18, 11, 18, 12, 8, 17, 6, 7, 6, 5, 13],[5, 3, 4, 3, 1, 2, 3, 2, 5, 2, 3, 5, 2, 5, 4, 3, 5, 2, 1, 1, 4, 2, 4, 5, 5, 4, 1, 1, 1, 3, 4, 2, 5, 1, 1, 4, 4, 3, 1, 1, 5, 4, 4, 4, 1, 2, 2, 3, 3, 4, 5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 5, 2, 3, 5, 4, 4, 4, 3, 1, 4, 3, 4, 4, 2, 3, 2, 3, 3, 1, 5, 2, 1, 2, 5, 1, 4, 4, 1, 1, 1, 2, 3, 1, 2, 4, 3, 4, 1, 3, 1, 4, 4, 5, 3, 3, 5, 1, 2, 5, 4, 2, 2, 5, 2, 3, 4, 5, 1, 5, 2, 5, 2, 1, 4, 3, 3, 1, 1, 2, 4, 5, 2, 4, 3, 4, 3, 5, 4, 3, 2, 4, 2, 3, 1, 5, 5, 3, 3, 1, 1, 1, 1, 3, 1, 5, 4, 3, 2, 2, 2, 4, 4, 3, 3, 1, 1, 2, 4, 4, 4, 4, 1, 2, 5, 3, 5, 5, 2, 4, 2, 5, 4, 1, 5, 4, 4, 1, 5, 2, 3, 1, 3, 2, 5, 4, 3, 1, 1, 3, 4, 3, 2, 2, 4, 2, 4, 5, 4, 4, 3, 3, 4, 2, 4, 3, 4, 2, 4, 5, 5, 3, 5, 2, 2, 5, 4, 2, 2, 1, 5, 5, 1, 2, 3, 5, 5, 3, 1, 4, 4, 1, 5, 4, 3, 1, 1, 1, 2, 3, 5, 3, 1, 4, 1, 2, 4, 5, 4, 3, 3, 1, 5, 2, 5, 5, 4, 5, 4, 2, 5, 1, 5, 5, 2, 2, 4, 2, 4, 2, 2, 5, 5, 1, 3, 4, 4, 2, 3, 2, 5, 2, 2, 4, 1, 3, 4, 3, 5, 3, 4, 1, 4, 5, 5, 4, 5, 2, 5, 5, 5, 3, 2, 2, 2, 3, 5, 1, 3, 5, 4, 2, 2, 1, 3, 2, 1, 5, 2, 3, 3, 2, 5, 3, 3, 3, 4, 4, 4, 4, 4, 3, 3, 5, 2, 4, 5, 3, 1, 2, 2, 5, 1, 5, 3, 3, 1, 5, 3, 1, 2, 1, 4, 4, 2, 5, 2, 5, 2, 2, 1, 4, 1, 1, 3, 3, 4, 3, 3, 2, 2, 2, 1, 5, 2, 5, 1, 2, 5, 1, 4, 1, 3, 2, 3, 1, 5, 4, 3, 3, 4, 5, 2, 1, 2, 5, 5, 5, 4, 3, 5, 1, 2, 2, 2, 4, 2, 2, 2, 3, 5, 3, 4, 4, 5, 3, 5, 1, 3, 1, 4, 2, 2, 3, 4, 5, 5, 1, 5, 2, 2, 1, 5, 1, 4, 2, 2, 4, 3, 4, 1, 5, 2, 1, 2, 3, 2, 2, 4, 4, 1, 2, 3, 5, 1, 4, 5, 1, 4, 1, 3, 1, 5, 2, 4, 3, 5, 3, 5, 5, 3, 5, 5, 5, 4, 1, 1, 5, 5, 5, 5, 2, 5, 3, 5, 1, 5, 2, 1, 3, 3, 1, 5, 5, 4, 2, 5, 2, 3, 3, 1, 3, 4, 2, 5, 5, 5, 3, 2, 5, 3, 3, 1, 2, 3, 3, 4, 5, 4, 1, 1, 5, 5, 4, 4, 2, 1, 1, 2, 5, 5, 4, 3, 5, 3, 4, 2, 4, 3, 1, 4, 2, 5, 5, 3, 1, 3, 5, 1, 2, 3, 3, 3, 3, 3, 4, 5, 4, 3, 1, 2, 3, 2, 5, 5, 4, 5, 1, 2, 5, 1, 1, 5, 5, 2, 1, 2, 5, 2, 5, 3, 5, 5, 1, 3, 5, 3, 3, 5, 5, 1, 2, 2, 3, 1, 1, 1, 2, 1, 5, 4, 1, 3, 5, 1, 4, 4, 4, 2, 4, 4, 3, 5, 1, 3, 1, 5, 3, 4, 3, 3, 4, 4, 2, 3, 3, 4, 5, 4, 4, 4, 4, 1, 5, 1, 5, 2, 3, 4, 1, 4, 5, 1, 2, 3, 3, 4, 1, 4, 4, 2, 3, 3, 4, 1, 1, 4, 4, 4, 2, 3, 3, 3, 3, 1, 2, 2, 3, 4, 2, 1, 5, 5, 1, 5, 5, 2, 2, 4, 4, 5, 4, 5, 2, 5, 5, 5, 3, 2, 3, 3, 5, 4, 1, 3, 4, 2, 5, 3, 3, 3, 3, 2, 5, 3, 4, 4, 4, 5, 4, 4, 1, 4, 2, 2, 1, 1, 1, 4, 3, 3, 3, 4, 5, 5, 1, 3, 2, 1, 2, 5, 5, 4, 5, 1, 4, 3, 1, 3, 2, 4, 4, 2, 1, 1, 3, 1, 3, 4, 1, 4, 5, 5, 5, 4, 3, 2, 5, 1, 1, 1, 1, 1, 2, 4, 3, 2, 4, 5, 3, 4, 2, 3, 4, 5, 4, 1, 3, 4, 3, 5, 2, 5, 4, 1, 5, 2, 4, 5, 2, 1, 5, 4, 4, 1, 1, 1, 3, 2, 1, 3, 2, 3, 4, 1, 2, 4, 5, 5, 4, 1, 5, 4, 5, 2, 2, 2, 3, 2, 1, 3, 3, 5, 1, 2, 4, 3, 2, 4, 4, 1, 1, 4, 2, 3, 3, 1, 4, 5, 5, 3, 4, 4, 5, 1, 2, 5, 4, 2, 2, 1, 2, 3, 1, 3, 5, 2, 5, 1, 5, 1, 3, 4, 4, 2, 5, 3, 2, 2, 5, 4, 5, 1, 4, 3, 3, 1, 4, 5, 1, 5, 2, 5, 1, 1, 2, 1, 4, 1, 4, 3, 5, 1, 1, 3, 5, 3, 1, 4, 3, 3, 2, 4, 5, 4, 2, 3, 2, 1, 5, 4, 1, 5, 2, 2, 1, 2, 5, 3, 3, 5, 3, 1, 2, 5, 5, 2, 1, 1, 4, 4, 4, 2, 5, 4, 2, 4, 2, 5, 5, 1, 2, 2, 2, 1, 1, 1, 3, 4, 4, 1, 1, 2, 5, 4, 5, 5, 4, 3, 4, 3, 4, 4, 3, 2, 4, 3, 2, 2, 5, 1, 3, 2, 2, 3, 2, 1, 2, 1, 2, 3, 1, 4, 5, 1, 3, 1, 3, 5, 1, 4]),10.709060955518945)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(*inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()