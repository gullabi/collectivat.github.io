---
layout: post
title: "Síntesi de la parla obert i lliure en català"
ref: sp_release
image: /img/blog/2019/catotron02_bg.png
thumbnail: /img/blog/2019/catotron02_sm.png
lang: ca
summary: Gràcies al projecte subvencionat pel Departament de la Cultura, vam entrenar els models de síntesi de la parla en català amb xarxes neuronals i els vam publicar amb llicències obertes. Volem presentar aquí els resultats, la nostra experiència i els detalls de com integrar aquesta tecnologia.
---

Aquí podeu trobar tota la informació pertinent a Catotron, síntesi de la parla
obert en català, entrenat amb xarxes neuronals. El codi està al [github][catotron] i els
models són descarregables aquí.

* La veu femenina: Ona [[descarregar]][ona]
* La veu masculina: Pau [[descarregar]][pau]

### Resum:

Els últims anys, les tecnologies de síntesi de la parla (SP) van avançar molt
gràcies a les tècniques d’aprenentatge profund. El canvi més important va ser
la introducció dels vocoders (mot creat de l’anglès: voice encoder,
«codificador de veu») entrenats amb xarxes neuronals. El primer exemple va ser
el Wavenet en el 2016 desenvolupat per DeepMind, que forma part de les empreses
de Google.

Avui en dia aquests vocoders s’utilitzen amb els sistemes de SP també entrenats
amb xarxes neuronals, específicament els sistemes de Tacotron i Tacotron2. Es
poden trobar diverses implementacions d’aquestes tecnologies en programari
lliure. Aquestes tecnologies representen l’estat d’art per SP, poden produir
resultats amb millor intel·ligibilitat i naturalitat possible.

Malauradament, per entrenar aquests sistemes, és imprescindible tenir recursos
molt importants com dades o potència computacional. És per això que no hi ha
cap model publicat amb llicències obertes, menys els d’anglès.  Gràcies al
projecte subvencionat pel Departament de la Cultura, vam entrenar els models de
SP en català amb xarxes neuronals i els vam publicar amb llicències obertes.
Volem presentar aquí els resultats, la nostra experiència i els detalls de com
integrar aquesta tecnologia. 

### El codi:

Les tecnologies que vam utilitzar són els repositoris de [Tacotron2][nvidia]
i [Waveglow][waveglow], de l’empresa de NVIDIA publicats amb llicències obertes a github. Un dels
resultats més importants és el codi; és a dir, el nostre fork de [Tacotron2][catotron], que
està modificat per al català, imprescindible per fer servir els models de
català.

### Els models:

Per entrenar els models de català vam aprofitar les dades obertes ja
publicades. Les veus resultants estan entrenades amb les dades de [Festcat][festcat], que
també va ser un projecte de la Generalitat, realitzat pels investigadors de la
UPC. Vam utilitzar les millors veus d’aquest conjunt de dades: les veus de
l’Ona i del Pau.


<br/>

Aquí teniu alguns fitxers de mostra. Les frases escollides venen del conjunt de dades de validació, és a dir no van entrar a l'entrenament dels models de catotron.

<br/>

#### Ona:
<table style="font-size:16px">
  <col width="205">
  <col width="205">
<thead>
<tr>
  <td>Original</td>
  <td>Festcat</td>
  <td>Catotron</td>
</tr>
</thead>
<tbody>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/200214_org.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/200214_festcat.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/200214_catotron.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/700215_org.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/700215_festcat.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/700215_catotron.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/270307_org.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/270307_festcat.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/ona/270307_catotron.mp3"></audio></td>
</tr>
</tbody></table>

#### Pau:
<table style="font-size:16px">
  <col width="205">
  <col width="205">
<thead>
<tr>
  <td>Original</td>
  <td>Festcat</td>
  <td>Catotron</td>
</tr>
</thead>
<tbody>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/410084_org.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/410084_festcat.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/410084_catotron.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/701140_org.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/701140_festcat.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/701140_catotron.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/821065_org.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/821065_festcat.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/pau/821065_catotron.mp3"></audio></td>
</tr>
</tbody></table>


<br/>
<br/>

Durant les nostres proves també vam fer experiments amb el conjunt de dades del
ParlamentParla, i vam produir un model de la parla d’Artur Mas, que era la
persona amb més hores registrades d’aquest conjunt de dades. Vam aprofitar
aquesta prova per fer una estimació del volum i de la qualitat de dades
necessàries per entrenar un model. Per temes de privacitat no publiquem aquests
models, però n’exposem alguns exemples. Les frases venen dels enregistraments de
la validació, és a dir no van entrar a l'entrenament del model.

<br/>

#### Artur Mas:
<table style="font-size:16px">
  <col width="205">
  <col width="205">
<thead>
<tr>
  <td>Original</td>
  <td>Catotron</td>
</tr>
</thead>
<tbody>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/840f2eb3cf16279d5359_441.73_445.01_norm.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/840f2eb3cf16279d5359_catotron_norm.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/62eccef1fcc7a1d4640b_1309.64_1313.35_norm.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/62eccef1fcc7a1d4640b_catotron_norm.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/f17e1565132b3b4f77c5_1168.39_1171.35_norm.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/f17e1565132b3b4f77c5_catotron_norm.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/e2a1601b41e1ff37fb0a_76.81_80.33_norm.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/e2a1601b41e1ff37fb0a_catotron_norm.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/11e58c59192563ce8ab9_165.71_171.42_norm.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/mas/11e58c59192563ce8ab9_catotron_norm.mp3"></audio></td>
</tr>

</tbody></table>

<br/>

Algunes frases de viquipèdia llegides per totes les veus entrenades:

<table style="font-size:16px">
  <col width="205">
  <col width="205">
<thead>
<tr>
  <td>Festcat Ona</td>
  <td>Festcat Pau</td>
  <td>Artur Mas</td>
</tr>
</thead>
<tbody>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain01_ona.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain01_pau.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain01_mas.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain02_ona.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain02_pau.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain02_mas.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain03_ona.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain03_pau.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain03_mas.mp3"></audio></td>
</tr>
<tr>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain04_ona.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain04_pau.mp3"></audio></td>
  <td><audio controls="" preload="none" style="width: 200px">audio not supported<source src="/img/audio/2019/oodomain/outofdomain04_mas.mp3"></audio></td>
</tr>

</tbody></table>


<br/> 
<br/> 

### Com es pot utilitzar:
Per ara, pels usuaris individuals la síntesi és només possible a través de la
interfície del [Google Colaboratory][colab1] on es poden aprofitar els GPUs de Google
gratuïtament. En unes setmanes publicarem  una pàgina en què els visitant
podran sintetitzar paraules curtes.

Com es poden entrenar noves veus: Amb les eines publicades, és a dir el codi i
els models, ja és possible adaptar la veu mitjançant l’aprenentatge per
transferència (transfer learning) a partir dels models publicats i
enregistraments d’un/a locutor/a. El nostre exemple de
[catotron-transfer-learning.ipynb][colab2] explica els passos necessaris de com fer-ho.
En aquesta llibreta específica, s’entrena la veu de Pau a partir dels models
d’Ona, aprofitant els recursos computacionals gratuïts de Google. 

### Pel futur:
Volem que aquests model siguin fàcilment integrables als productes tecnològics.
Un dels obstacles greus és la necessitat d'ús dels GPUs, i l’eficiència
computacional de la síntesi. Per accelerar el procés de síntesi i fer-ho més
eficaç volem canviar el vocoder de Waveglow a [Melgan][melgan]. Aquest treball també
millorarà considerablement la qualitat de les veus masculines, que encara són
força robòtiques degut als models de vocoder que estem utilitzant. 

### Contribuïdors:
* Baybars Külebi (Col·lectivaT)
* Alex Peiro Lilja (UPF)
* Alp Öktem (Col·lectivaT)

---
Aquests recursos van estar desenvolupats gràcies al projecte «síntesi de la
parla contra la bretxa digital» subvencionat pel Departament de la Cultura. Una
part dels fons provenen dels cabals que atorga la Junta d'Herències de la
Generalitat de Catalunya.

<img src="/img/logo_generalitat.png" width="400"/>

[catotron]: https://github.com/CollectivaT-dev/tacotron2
[nvidia]: https://github.com/NVIDIA/tacotron2
[waveglow]: https://github.com/NVIDIA/waveglow/
[tallers]: https://github.com/CollectivaT-dev/TallersParla
[ona]: https://drive.google.com/open?id=1-fdWV-aH5nIRv1rZKQYInsRes2At74xG
[pau]: https://drive.google.com/open?id=1-T2nHQNEE8mXPaT-ulDSAXgdGSzomPMu
[colab1]: https://colab.research.google.com/github/CollectivaT-dev/TallersParla/blob/master/ipynb/catotron_inference.ipynb
[colab2]: https://colab.research.google.com/github/CollectivaT-dev/TallersParla/blob/master/ipynb/catotron_transfer_learn.ipynb
[festcat]: http://festcat.talp.cat/download.php
[melgan]: https://github.com/seungwonpark/melgan
