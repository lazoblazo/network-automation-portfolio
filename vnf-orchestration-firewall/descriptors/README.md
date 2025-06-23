# Virtuálny firewall – VNF šablóna pre Telco orchestráciu

Tento projekt simuluje, ako by sa v telco prostredí nasadzovala virtuálna sieťová funkcia (VNF) – v tomto prípade firewall – pomocou šablóny typu YAML.


Skladba:
- vnf-firewall.yaml: hlavná šablóna služby
- firewall-rules.yml: pravidlá firewallu pri nasadení

Scenár:
1. Operátor zaregistruje túto šablónu do orchestrátora (napr. ONAP, OSM)
2. Vytvorí sa VM s 2 CPU, 2 GB RAM, 3 sieťovými rozhraniami
3. Konfigurujú sa pravidlá firewallu
4. Pripojí sa do LAN/WAN/Management siete

Prax:
Takto by operátor vedel automatizovať nasadenie firewallu napríklad medzi core a zákazníckou sieťou bez nutnosti manuálneho nastavovania.

