# Network Automation Portfolio

Toto portfólio obsahuje niekoľko mini-projektov z oblasti sieťovej automatizácie. Projekty sú vytvorené pomocou Pythonu a knižníc ako Netmiko a využívajú GitHub Actions na automatizáciu testovania a CI/CD.

## Projekty

### 1. Device-Version-Check
Skript na pripojenie k sieťovým zariadeniam a získanie verzie operačného systému pomocou Netmiko.

### 2. Network Health Check
Skript na kontrolu dostupnosti zariadení a základný health check cez SSH.

### 3. Device Inventory Generator
Načíta zoznam zariadení zo súboru YAML a vygeneruje jednoduchý textový výstup ako inventár.

### 4. Device Status Monitor
Skript, ktorý testuje dostupnosť zariadení pomocou ICMP (ping).

### 5. Hodnotenie_dodavatelov.csv
Tabuľka na porovnanie technických parametrov a hodnotenie dodávateľov v rámci Telco tendra.
Obsahuje hmotnostné hodnotenie a bodovanie.
Slúži ako jednoduchá ukážka predvýberu partnera na základe technických kritérií.

### 6. vnf-orchestration-firewall/descriptors
YAML deskriptory pre nasadenie virtuálneho firewallu (VNF) v Telco prostredí.
Obsahuje základné šablóny pre VNF, NSD, CP a ich prepojenie v rámci MANO architektúry.
Ukážka základnej VNF orchestrácie v štýle ETSI NFV.

### 7. firewall-automation-cisco
Automatizované generovanie firewall ACL pravidiel pre Cisco zariadenia pomocou Ansible a Jinja2.
Pravidlá sa definujú v YAML, z ktorých sa vytvára výstupný konfiguračný súbor.
