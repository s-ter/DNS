import subprocess
import shlex




def DNSSEC_supported(name):


    cmd = 'dig DS ' + name +' +trace @1.1.1.1'
    #print(cmd)
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    out, err = proc.communicate()
    s = out.decode('UTF-8')


    if "RRSIG" in s:
        print(name + ': DNSSEC is supported')
        return(1)
    else:
        return (0)

def DNSSEC_valid(name):

    cmd = 'dig +dnssec ' + name
    #print(cmd)
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    out, err = proc.communicate()
    s = out.decode('UTF-8')

    if "ad" in s:
        print(name + ' : DNSSEC is valid')
        return(1)
    else:
        return(0)

def get_origin(name):

    for i in range(len(name)-1):
        if name[len(name) - i - 1] == '.':
            name = name[-i-1:]
            #print(name)
            return(name)
            break





if __name__ == '__main__':

    compteur_DNSSEC_supported = 0
    compteur_DNSSEC_valid = 0
    l = list()


    file_coord = "dataBase"
    temp = file_coord.splitlines()
    temp = open(file_coord, 'r')
    temp = [line[:-1] for line in temp]

    file_coord2 = "pays.txt"
    temp2 = file_coord.splitlines()
    temp2 = open(file_coord2, 'r')
    temp2 = [line[:-1] for line in temp2]

    for i in range(200):
        s = DNSSEC_supported(temp[i])

        if s==1:
            compteur_DNSSEC_supported += 1

        s = DNSSEC_valid(temp[i])

        if s==1:

            compteur_DNSSEC_valid += 1
            current = get_origin(temp[i])
            for j in range(len(temp2)):
                if current == temp2[j]:
                    if current not in l:
                        l.append(temp2[j+1])


    print('Nombre de domain qui supportent DNSSEC :', compteur_DNSSEC_supported)
    print('Nombre de domain qui valident DNSSEC :', compteur_DNSSEC_valid)
    print('Les pays dont les domains valident DNSSEC sont :', l)








    print(compteurDNSSEC)
