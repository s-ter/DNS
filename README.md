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
- test based on a 1000 domain name base to know which ones in the data base use DNSSEC. (to know if DNSSEC is used, I check the presence of the RRSIG message)

Les DNSSEC renforcent l'authentification du DNS en utilisant des signatures numériques basées sur la cryptographie à clé publique. Avec les DNSSEC, les requêtes DNS et les réponses ne sont pas elles-mêmes signées cryptographiquement, ce sont les données DNS qui sont signées par le propriétaire des données.


