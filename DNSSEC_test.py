import subprocess
import shlex


def testDNSSEC(name):

    cmd = 'dig DS ' + name + ' +trace @8.8.8.8'
    print(cmd)
    # cmd='dig @ns1.netnames.net www.rac.co.uk CNAME'
    proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    out, err = proc.communicate()
    s = out.decode('UTF-8')
    #print( name + ': \n' + s)

    if "RRSIG" in s:
        print(name + ': DNSSEC valid')
        return(1)

    else:
        #print(name + ' : DNSSEC not valid')
        return(0)


if __name__ == '__main__':

    compteurDNSSEC = 0
    file_coord = "dataBase"
    temp = file_coord.splitlines()
    temp = open(file_coord, 'r')
    temp = [line[:-1] for line in temp]
    print(temp)
    for i in range(len(temp)):
        s = testDNSSEC(temp[i])
        if s==1 :
            compteurDNSSEC +=1

    print(compteurDNSSEC)