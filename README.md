# DNS

## Summary  

>> tests.py
- DNS query to get to IP adress of a domainName
- inverseDNS to get the host name based on the IP adress
- query for trying to get info on a domain 
- query for trying to find the root of a domainName

>> proxy.py
- using free proxies : query to unsure the origin of the query is the adress of the proxy and not the real user's one

>> DNSSEC_test.py
- test based on a 1000 domain name base to know which ones in the data base supporte DNSSEC. (to know if DNSSEC is used, I check the presence of the RRSIG message)
- test based on the same data base to thus verify if DNNSEC is validated (cmd : '+dnssec' to set the DO flag in the query + check if: presence of AD bit)
- For each domain which has been validated; identification of the source country (using the first level domain name such as '.it')

## Validation of DNNSEC 

Les DNSSEC renforcent l'authentification du DNS en utilisant des signatures numériques basées sur la cryptographie à clé publique. 

Le bit AD est visible seulement si toute les données de la réponse ont été cryptographiquement vérifiées et que la réponse correpond aux polices de sécurité du serveur local/propriétaire des données (le résolveur a vérifié les signatures DNSSEC accompagnant les records présentent dans la réponse et section Autorité). Une réponse contenant des données non sécurisés ou un serveur configuré sans les DNSSEC keys ne posséderont pas le bit AD. 

Une application client qui a une relation de confiance avec le serveur performant une requête recursive peut ensuite utiliser la value du bit AD pour déterminer si les données sont sécurisés.

