---
layout: post
title: "Eines per auditar el PAM de decidim.barcelona"
ref: decidim
image: /img/blog/2017/kapak.png
#thumbnail: /img/blog/2017/metadecidim_sm.png
lang: ca
summary: Vam classificar els missatges de rebuig a les propostes al Pla d'Acció Municipal (PAM) i vam crear un <a href="http://decidim.collectivat.cat">un panell de control interactiu</a> per mostrar els nostres resultats. Aquest treball és un seguiment detallat de la <a href="https://bcnparticipa.cat/JornadesMetadecidim/ca/index.php">hackató del metadecidim</a>, específicament de la sessió d'anàlisi de dades per a la democràcia. 
---
Aquest treball és un seguiment detallat de la <a href="https://bcnparticipa.cat/JornadesMetadecidim/ca/index.php">hackató del #metadecidim</a>, específicament de la sessió d'anàlisi de dades per a la democràcia. Hem classificat els missatges de rebuig a les propostes al Pla d'Acció Municipal (PAM) i hem posat les dades relacionades en un panell de control interactiu, incloent les nostres pròpies categoritzacions. El panell de control és accessible en <a href="http://decidim.collectivat.cat">http://decidim.collectivat.cat</a>.

La hackató del decidim.barcelona va tenir lloc el 25 i 26 del novembre del 2016
al Convent dels Àngels i l'Auditori del MACBA. Aquest esdeveniment va unir
totes les parts interessades per treballar en col·laboració amb
decidim.barcelona, la plataforma digital de la participació de l'Ajuntament de
Barcelona. Els objectius del taller de dades eren analitzar i visualitzar les
dades generades dins de la plataforma. Un resum i la xerrada final sobre la
secció de dades es poden trobar al <a
href="https://elaragon.wordpress.com/2016/11/26/metadecidim/">blog</a> del
Pablo Aragon i el conjunt de dades en
[aquest repositori](https://github.com/elaragon/metadecidim).

La plataforma decidim va ser utilitzada per a què la ciutadania pogués presentar propostes per ratificar el PAM. Es va dur a terme entre el gener i l'abril de l'any 2016. També es pot trobar un bon <a href="https://decidim.barcelona/pam/6/dataviz/summary">resum visual</a> (*enllaç trencada*) del procés. Pel que fa el taller de dades, Col.lectivaT va assumir la tasca de classificar els missatges de rebuig a les propostes al PAM, per tal d'auditar el treball de l'Ajuntament.

Per comprendre els motius de rebuig i sintetitzar-los, vam vectoritzar cada missatge amb un TfidfTransformer, i després vam agrupar aquests vectors amb l'algoritme de kmeans. Per al procés de algoritme k-means, vam utilitzar el valor ad-hoc de 30 per al nombre de grups. El codi, les dades inicials i les dades enriquides es poden trobar a <a href="https://bitbucket.org/bkulebi/metadecidim_postprocess">bitbucket</a>. Els nostres resultats van poder agrupar els missatges en funció del seu lèxic, però per agrupar-los conceptualment vam revisar manualment aquestes 30 categories i els vam agrupar en 5 conceptes. El nostre treball va resultar amb una categorització de 77% de les propostes rebutjades, la resta es va quedar com "altres".

Les sis categories que vam descobrir són:

* <strong>Proposta duplicada:</strong> 0,77% 21/2718
* <strong>L'Ajuntament no té recursos:</strong> 7.65% 208/2718
* <strong>No és competència municipal:</strong> 7.98% 217/2718
* <strong>L'Ajuntament no està treballant en aquesta línia:</strong> 11.03% 300/2718
* <strong>Proposta no concreta:</strong> 12.28% 334/2718
* <strong>Altres:</strong> 22.33% 607/2718
* <strong>Serà tinguda en compte:</strong> 37.93% 1031/2718

<br/>

La majoria de les categories s'explica per si mateix, menys el més comú "serà tinguda en compte". L'agrupació és el resultat de l'ús habitual de "No podem comprometre’ns a desenvolupar aquesta proposta al nivell de concreció que es proposa, però serà tinguda en compte en el moment de la planificació corresponent". En molts casos (per excepcions vegeu abaix) una raó més específica segueix la frase plantilla, en relació amb la proposta específica i s'explica com el municipi està tractant de resoldre el problema a través d'altres mitjans. Per tant, aquest tipus de rebuig està més relacionat amb la forma en què està escrit sintàcticament, que no pas amb la pròpia raó conceptual.

A més de la classificació, vam construir un <a href="http://decidim.collectivat.cat/">panell de control interactiu</a> per a les dades. A través d'aquesta categorització i visualització esperem que els temes proposats arribin al PAM i que les respostes dels municipis siguin encara més accessibles pel públic. Un altre ús d'aquest treball seria ajudar als ciutadans a formular millor les seves propostes en les possibles accions de decidim. Finalment, des de la perspectiva del desenvolupament de programari, les nostres categories es poden implementar com a possibles opcions dins dels missatges de rebuig, ajudant a la feina dels avaluadors en el futur. Això podria ser una altra característica integrada per a la millor comprensió i l'auditoria de les dades.

Com assenyalat anteriorment, un dels nostres objectius més importants era auditar l'avaluació de l'ajuntament. Sumat a les visualitzacions, les noves categories fan que les dades finals siguin més transparents per la ciutadania. La diferència principal del nostre panell de control, comparat amb la visualització de l'ajuntament, és que nosaltres fem servir el resultat final de tot el procés. A més, el nostre panell proporciona filtres transversals entre els districtes, les categories i les fonts de les propostes, a diferència de la visualització jeràrquica sunburst a la web de decidim, on les dades a les vores resulten cada vegada més difícil de llegir. Al nostre panell de control de dades, les dades són relacionals, per tant és més fàcil de veure la importància de la font de les propostes o el pes de les categories temàtiques en general de la PAM.

Per donar un exemple de com es poden utilitzar els resultats i les visualitzacions, ens agradaria explicar alguns dels resultats de la nostra anàlisi.

La proporció mitjana de rebuig pels districtes en total és al voltant del 25%. Cada districte compleix aquesta proporció, tots resten per sota el 38% de denegació, menys un: el districte de Sarrià-Sant Gervasi, que té la proporció més alta de rebuig amb el 53%.

<br/><br/>

| ![](/img/blog/2017/all.png) | | ![](/img/blog/2017/sarria.png)|
| *Totes les propostes* | |  *Sarrià-Sant Gervasi*|


<br/><br/>

No obstant això, la major diferència de Sarrià-Sant Gervasi es presenta en les categories de rebuig, on la categoria de "serà tinguda en compte" domina totes les altres. Mentre una mitjana del 38% de totes les categories de rebuig per tots els districtes és "serà tinguda en compte", per Sarrià aquesta categoria ocupa el 90% dels missatges de rebuig.

<br/><br/>

|![](/img/blog/2017/all_rejection.png) | | ![](/img/blog/2017/sarria_rejection.png) |
|*Totes les propostes* || *Sarrià-Sant Gervasi*|

<br/><br/>

Per entendre millor les raons d'aquesta incongruència, vam mirar els detalls dels missatges de rebuig, cas per cas. No obstant això, vam descobrir que només hi havia 5 missatges específics dins dels 225 missatges de rebuig en total. Aquí teniu els 4 missatges de rebuig especificats i els enllaços a les seves propostes respectives:

* **Beques estudi** [(*enllaç trencat*)](https://decidim.barcelona/pam/proposals/beques-estudi) : No podem comprometre’ns a desenvolupar aquesta proposta al nivell de concreció que es proposa, però serà tinguda en compte en el moment de la planificació corresponent.Les beques d'estudi són competència de la Generalitat però tindrem en compte la proposta i la traslladarem a les reunions mixtes de coordinació amb la Generalitat.
* **Un centre soci sanitari en l'antiga clinica Sant Josep** [(*enllaç trencat*)](https://decidim.barcelona/pam/proposals/un-centre-soci-sanitari-en-l-antiga-clinica-sant-josep): No podem comprometre’ns a desenvolupar aquesta proposta al nivell de concreció que es proposa, però serà tinguda en compte en la planificació dels serveis socials i habitatges tutelats.
* **Connexió directa xarxa d'autobusos barris del centre** [(*enllaç trencat*)](https://decidim.barcelona/pam/proposals/connexio-directa-xarxa-autobusos-barris-centre): No podem comprometre’ns a desenvolupar aquesta proposta al nivell de concreció que es proposa, però serà tinguda en compte en el moment de la planificació corresponent, en el Pla de mobilitat urbana.
* **Limitar l'acces amb vehicle privat al Tibidabo** [(*enllaç trencat*)](https://decidim.barcelona/pam/proposals/limitar-l-acces-amb-vehicle-privat-al-tibidabo): No podem comprometre’ns a desenvolupar aquesta proposta al nivell de concreció que es proposa, però serà tinguda en compte en el Pla de mobilitat del districte.

Els restants 221 missatges de rebuig tenen la mateixa plantilla de "No podem comprometre’ns a desenvolupar aquesta proposta al nivell de concreció que es proposa, però serà tinguda en compte en el moment de la planificació corresponent."

Com a resultat, ens hem adonat que el districte amb el major nombre de rebutjos alhora manca d'una explicació detallada de la majoria de les seves propostes rebutjades. Això pot ser problemàtic des del punt de vista dels ciutadans del districte i pot provocar una insatisfacció.

Per l'anàlisi més profunda dels nostres resultats i les dades de PAM en general, si us plau, doneu un cop d'ull al <a href="http://decidim.collectivat.cat">panell de control</a> dels resultats.


[catotron]: https://github.com/CollectivaT-dev/tacotron2
[catotron-cpu]: https://github.com/CollectivaT-dev/catotron-cpu
[nvidia]: https://github.com/NVIDIA/tacotron2
[waveglow]: https://github.com/NVIDIA/waveglow/
[tallers]: https://github.com/CollectivaT-dev/TallersParla
[ona]: https://drive.google.com/open?id=1-fdWV-aH5nIRv1rZKQYInsRes2At74xG
[pau]: https://drive.google.com/open?id=1-T2nHQNEE8mXPaT-ulDSAXgdGSzomPMu
[colab1]: https://colab.research.google.com/github/CollectivaT-dev/TallersParla/blob/master/ipynb/catotron_inference.ipynb
[colab2]: https://colab.research.google.com/github/CollectivaT-dev/TallersParla/blob/master/ipynb/catotron_transfer_learn.ipynb
[festcat]: http://festcat.talp.cat/download.php
[melgan]: https://github.com/seungwonpark/melgan
[waveglow_model]: https://drive.google.com/open?id=1WsibBTsuRg_SF2Z6L6NFRTT-NjEy1oTx
[melgan_model]: https://drive.google.com/file/d/1U3LeuaMIVoRvMvfwlHjsRJPWhgTzeIBh
[demo]: http://catotron.collectivat.cat/
