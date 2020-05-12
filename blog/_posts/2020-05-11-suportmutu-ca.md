---
layout: post
title: "SuportMuTu: Accessibilitat lingüística als canals públics i suport veïnal"
ref: suportmutu
image: /img/blog/2020/suportmutu_landscape.png
thumbnail: /img/blog/2020/suportmutu.png
lang: ca
summary: "Gràcies a la iniciativa Economia Per La Vida, hem creat una infraestructura digital per traduir els canals públics i de suport veïnal a Telegram, a algunes llengües de les comunitats d’origen migrant de Catalunya."
---

Gràcies a la iniciativa [Economia Per La Vida][goteo], _**hem creat una infraestructura digital per traduir els canals públics i de suport veïnal a Telegram**_, a algunes llengües de les comunitats d’origen migrant de Catalunya.

Si voleu donar un cop de mà, si us plau feu córrer la veu sobre els canals de Telegram que hem implementat fins ara:

* [/Salut (urdú)][salutcat_ur]
* [/Salut (àrab)][salutcat_ar]
* [/Salut (xinès)][salutcat_zh]
* [Suport Mutu Gràcia (urdú)][suportgracia_ur]
* [Suport Mutu Gràcia (àrab)][suportgracia_ar]
* [Suport Mutu Gràcia (xinès)][suportgracia_zh]
* [Xarxa de Suport Verdum (àrab)][XarxadeSuportVerdum_ar]

Si teniu un canal informatiu de Telegram i voleu incorporar el bot al vostre canal en aquests idiomes, si us plau escriviu a: info@collectivat.cat

## Context

Davant de l’auge de la crisi causada per la pandèmia del **coronavirus** els Estats han adoptat mesures d’urgència molt severes. No obstant això, també hi ha mancances pel que fa a la intervenció estructural i institucional en altres problemes que també són greus. Mentre que els Estats han estat concentrades en accions que tenen finalitat d’evitar el col·lapse del sistema sanitari, la ciutadania s’ha **auto-organitzat** per teixir vies de solidaritat mútua a través de les plataformes digitals en les condicions de l’estat d’alarma. Hem observat que les organitzacions veïnals i **diversos grups antiracistes** han optat per difondre informació útil a la ciutadania en grups i canals de xat de les aplicacions com WhatsApp i **Telegram.** A part de difondre informació, molts d’aquests espais digitals també serveixen per detectar les necessitats dels sectors més vulnerables de la societat i auto-organitzar-se com a poble per respondre aquestes necessitats concretes. _Actualment a Barcelona hi ha prop de 40 xarxes de suport mutu organitzades en diverses barris de la ciutat._

**Col·lectivaT** és una cooperativa fundada per persones d’origen migrant, per tant, la nostra atenció sempre està dirigida als espais d’exclusió que hi ha en la societat que moltes vegades són espais d’invisibilització de les realitats d’aquest col·lectiu. Per això, no vam tardar gaire en veure els obstacles que podrien tenir **els col·lectius migrants** en el moment d’accedir a **la informació** que circula en aquestes plataformes digitals. Per molt fàcil que sigui l’accés als canals—, ja que disposar un telèfon mòbil i/o una computadora en què es pot servir una d’aquestes aplicacions és suficient—l’idioma vehicular d’aquests canals sabíem que podria convertir-se en una barrera per col·lectius que no dominen el català i/o el castellà.

A través del nostre projecte **SuportMuTu** volem garantir la transmissió dels missatges d’aquests **canals de la solidaritat i del suport veïnal** a algunes llengües que parlen els col·lectius migrants de Catalunya _no provinents del continent americà_. El software que desenvolupem garantirà que els canals informatius i canals de suport mutu veïnals funcionin en paral·lel amb les seves versions en altres llengües com ara l’àrab, urdú, xinès, etc.

## Els detalls


**SuportMuTu** és una infraestructura de programari **d’intel·ligència artificial** que funciona amb el suport d’una **xarxa de voluntàries correctores.** El bot que hem desenvolupat, en primer lloc, remet els missatges publicats en els canals de suport veïnal al nostre sistema de traducció automàtica i aquest sistema envia els textos traduïts als grups de correctores en idiomes corresponents. Elles revisen i, si s’escau, corregeixen els missatges traduïts automàticament. El mateix bot també permet la transmissió automàtica dels missatges traduïts i corregits a la versió en tal idioma del canal de suport veïnal, que havia publicat anteriorment la versió original en català i/o castellà. A més a més, just després de cada missatge en text, també s’afegeix la seva **versió sintetitzada en format àudio** per tal de fer-ho accessible per a les persones amb dificultat visual o persones analfabetes.

[El codi de SuportMuTu][github] és accessible a github amb una llicència lliure. Podeu veure com funciona SuportMuTu en pràctica, i com es fan les revisions, amb un exemple de traducció del català al castellà:

![Com funciona](/img/blog/2020/suportMuTu_long.gif)

## Com col·laborar

Per molt avançats que siguin els sistemes de la traducció automàtica, segueixen fent errors i això pot provocar riscos en aquests tipus de situacions en què es tradueixen  missatges relacionats amb la salut pública. És per això que les persones voluntàries que revisen i corregeixen els missatges tenen un paper clau. 

Per això estem actualment buscant **voluntàries** per cada idioma. Aquestes persones han d'**entendre bé el català/castellà escrit** (és a dir, no cal que sàpiguen escriure i/o parlar), i han de ser natives o saber suficient l’idioma objectiu **_(àrab/hindi/bengalí/urdú/xinès o altre)_** per poder **revisar la traducció automàtica** i la informació clau. Preveiem uns 8 i 10 missatges/dia. Si hi ha 4 persones revisores, seria 2-3 missatges/dia/persona (~9-12 frases).

A l'inici busquem **voluntàries,** és a dir la col·laboració no és remunerada. Més endavant si tot funciona bé i quan s'incorporin més grups, decidirem entre totes com remunerar-ho.

<br/>

_**Si voleu participar com a voluntària per corregir missatges, preferiblement en les llengües àrab, urdú, hindi, xinès, bengalí, amazic i tagalog; si us plau ompliu aquest [formulari][formulari].**_

_**Si teniu un canal informatiu de Telegram i voleu incorporar el bot al vostre canal en aquests idiomes, si us plau escriviu a:**_ info@collectivat.cat

_**Si coneixeu persones que tenen dificultat d’entendre el català/castellà, parlen aquestes llengües (vegeu la llista actual de les llengües incorporades) i que viuen en aquests barris (vegeu la llista actual dels canals de suport veïnal), si us plau fer-los arribar la informació perquè puguin seguir els canals en el seu propi idioma.**_

---
Per saber més sobre la Economia per la Vida: Fons Cooperatiu ESS, podeu visitar [la seva pàgina][economiaperlavida] o [la seva pàgina a Goteo][goteo].

<img src="/img/blog/2020/economiaperlavida.jpg" width="600"/>

[goteo]: https://ca.goteo.org/project/fons-cooperatiu-front-l-emergencia-social-i-sanita
[github]: https://github.com/CollectivaT-dev/suport_mt
[formulari]: https://limesurvey.collectivat.cat/index.php?r=survey/index&sid=695434
[salutcat_ur]: https://t.me/salutcat_ur
[salutcat_ar]: https://t.me/salutcat_ar
[salutcat_zh]: https://t.me/salutcat_zh
[suportgracia_ur]: https://t.me/suportgracia_ur
[suportgracia_ar]: https://t.me/suportgracia_ar
[suportgracia_zh]: https://t.me/suportgracia_zh
[XarxadeSuportVerdum_ar]: https://t.me/XarxadeSuportVerdum_ar
[economiaperlavida]: http://www.economiaperlavida.cat/
