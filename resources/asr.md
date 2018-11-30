---
layout: asr_base
ref: asr
lang: ca
permalink: asr
---
<style>
table {
    width:100%;
}
</style>

# Recursos per les tecnologies de la parla

Com a part de la nostra missió, proporcionem dades i recursos oberts al públic sobre tecnologies de parla. Podeu trobar una llista detallada aquí amb explicacions breus i altres referències per obtenir més informació. També, visiteu la nostra [wiki][wiki] per a més informació sobre les tecnologies de la parla i els models que mantenim.
  
<br /> 

| Name                              | Language | Type           | License    | Download |
|---------------------------------  | -------- | -----------    | --------   | -------- |
| [TV3Parla][2]                v0.3 | Catalan  | model acústic  |  AGPL-3.0  | [link]() |
| [TV3Parla+ParlamentParla][2] v0.2 | Catalan  | model acústic  |  AGPL-3.0  | [link]() |
| [TV3Parla Corpus][1]         v0.3 | Catalan  | corpus d'àudio | CC-BY-NC 4.0 | [link]() |
| [ParlamentParla Corpus][1]   v0.3 | Catalan  | corpus d'àudio |  CC-BY 4.0 | [link]() |
| OpenSubtitles LM             v1.0 | Catalan  | model d'idioma |  CC-BY 4.0 | [link]() |
| Viquipèdia LM                v1.0 | Catalan  | model d'idioma |  CC-BY 4.0 | [link]() | 
 
<br />
<br />

## Corpora acústics

Per als dos projectes que vam dur a terme amb èxit, vam recollir enregistraments de veu disponibles públicament i els vam convertir en corpora acústics per entrenament dels sistemes de RAP. Aquests conjunts de dades estan disponibles per descarregar amb diverses llicències obertes.

* **TV3Parla**

  Aquest corpus inclou 240 hores de parla catalana de material audiovisual. Els detalls de la segmentació, el processament de dades i l'entrenament del model s'expliquen en [Külebi, Öktem; 2018](https://www.isca-speech.org/archive/IberSPEECH_2018/abstracts/IberS18_P1-2_Kulebi.html). El propietari del contingut original és la Corporació Catalana de Mitjans Audiovisuals, SA (CCMA); vam processar el seu material i estem fent-lo disponible aquí sota els seus [termes d'ús](http://www.ccma.cat/avis-legal/condicions-utilitzacio-del-portal/).

  El corpus es pot trobar [aquí]() sota la llicència [CC BY-NC 4.0][ccbync].  
  <br/>

  Aquest projecte va ser possible gràcies al suport [d'Associació Softcatalà](https://www.softcatala.org/).


* **ParlamentParla**

  Vam recollir aquest corpus a partir dels enregistraments i les transcipcions dels plens del [Parlament de Catalunya](https://www.parlament.cat/). Vam alinear les transcripcions amb els enregistraments i vam extreure les 320 hores més netes per a entrenar els models de parla. El contingut pertany al Parlament de Catalunya i les dades es publiquen conforme a les seves [condicions d'ús](https://www.parlament.cat/pcat/serveis-parlament/avis-legal/).

  Podeu trobar el corpus [aquí]() sota la llicència [CC BY-NC 4.0][ccbync]. A més dels fitxers d'àudio segmentats i les transcripcions, el corpus inclou els enllaços del text sencer i l'àudio, per intervenció. En un futur proper publicarem també la forma estructurada de les sessions del Parlament (id sessió, intervinent, text d'intervenció, durada d'intervenció, etc.).  
  <br/>

  Aquest projecte va ser possible gràcies al suport del [Departament de Cultura](http://cultura.gencat.cat/) de la Generalitat.

## Models de RAP

Aquí teniu els models de RAP que vam entrenar nosaltres a partir dels corpora mencionats abans. Per ara vam utilitzar el toolkit de reconeixement de la parla, [CMUSphinx](https://cmusphinx.github.io/), que és el resultat de més de 20 anys de recerca a la Universitat Carnegie Mellon. Encara que actualment l'estat-de-l'art és la tecnologia híbrida de Hidden Markov Models (HMM) i les xarxes neuronals (NN) com Kaldi, l'eina `pocketsphinx` segueix sent rellevant per descodificar offline en entorns limitats de recursos, com els dispositius móbils. Continuem el nostre treball de manteniment i millora dels models en el nostre [repositori](https://github.com/collectivat/cmusphinx-models). Podeu trobar guies d'instal·lació i configuració, i tutorials dels casos d'ús bàsic al nostre [wiki][wiki].

Aquí teniu la llista dels nostres models de CMUSphinx més recents:

* [TV3Parla v0.3](): `sphinxtrain` 5pre-alpha continuous model
* [TV3Parla+ParlamentParla v0.2](): `sphinxtrain` 5pre-alpha continuous model
  <br/>  
  <br/> 
  <br/>

La preparació d'aquesta pàgina va ser possible amb el suport del [Departament de Cultura](http://cultura.gencat.cat/) de la Generalitat.

<img src="/img/logo_generalitat.png" width="400"/>

[wiki]: https://github.com/collectivat/cmusphinx-models/wiki
[ccby]: https://creativecommons.org/licenses/by/4.0/
[ccbync]: https://creativecommons.org/licenses/by-nc/4.0/
[2]: #asr-models
[1]: #acoustic-corpora
