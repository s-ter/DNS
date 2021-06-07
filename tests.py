import dns.reversename
import dns.resolver
import requests


#https://sitereport.netcraft.com/?url=http://text-lb.esams.wikimedia.org.

n = dns.name.from_text('wikitech-static.wikimedia.org')



try:
    while True:
        try:
            #On envoie une requête de type NS :
            answer = dns.resolver.resolve(n,'A')
        except dns.resolver.NoAnswer:
            #On a pas trouvé d'enregistrement, on ignore l'exception et on continue
            print("Aucun enregistrement NS trouvé pour "+n.to_text()+", tentative avec le parent.")
        else:
            #Aucune exception levée, on a trouvé un enregistrement NS
            print("Enregistrement NS trouvé pour le domaine "+n.to_text()+" :")

            for rdata in answer:
                print(rdata.to_text())

            break;
        #Si on arrive ici, c'est qu'on a pas trouvé, on réessaie avec le parent:
        n = n.parent()
except dns.name.NoParent:
    #Cette exception est levée si le domaine n'a plus de parent, on a atteint la racine du DNS
    print("Aucun serveur NS trouvé")


#test pour retrouver nameServer à partir d'une adresse IP = PTR record
no = dns.reversename.from_address(rdata.to_text())
answers = dns.resolver.resolve(no, 'PTR')
for rdata in answers:
    print("ReverseDNS sur l'adresse IP trouvée, nameHost : ")
    print(rdata.target)




# requête qui demande des racines
myResolver = dns.resolver.Resolver() #La création d'un résolveur personnalisé permet d'utiliser l'adresse de notre cible comme résolveur
myResolver.timeout = 5
myResolver.lifetime = 5
myResolver.nameservers = [rdata.to_text]

print("Requete avec dns.resolver.Resolver pour trouver les domaines racines :")
try:
    answer = myResolver.resolve('.')
except:
    print("Requête refusée par le serveur (arrive souvent car aujourd'hui les racines sont protégées)")
else:
    print("Le serveur a répondu :")
    for rdata in answer:
        print(rdata.to_text())

#demander des infos
print("Demande d'infos sur le serveur :")
myResolver2 = dns.resolver.Resolver() #La création d'un résolveur personnalisé permet d'utiliser l'adresse de notre cible comme résolveur
myResolver2.timeout = 5
myResolver2.lifetime = 5
myResolver2.nameservers = ['192.168.1.1']
try:
    answer = myResolver2.resolve('version.bind','TXT','CH') #Le troisième paramètre "CH" permet d'utiliser la classe CHAOS
except:
    print("Impossible de récupérer la version du serveur (arrive souvent également car plus de sécurité)")
else:
    print("Réponse du serveur :")
    for rdata in answer:
        print(rdata.to_text())