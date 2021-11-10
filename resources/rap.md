---
layout: asr_base
ref: asr
lang: ca
permalink: rap
---
<style>
table {
    width:100%;
}
</style>

# Recursos per les tecnologies de la parla

Com a part de la nostra missió, proporcionem dades i recursos oberts al públic sobre tecnologies de parla, sobre tot reconixement automàtic de parla (RAP) i síntesi de text a veu (SDV) en català. Podeu trobar una llista detallada aquí amb explicacions breus i altres referències per obtenir més informació. 
  

| Nom                                     | Llengua | Tipus          | Llicència     | Descarregar    |
|---------------------------------------- | ------- | -----------    | --------      | -----------    |
| [TV3Parla][2]                      v0.3 | català  | model acústic  | GNU AGPL-3.0  | [enllaç][M0.3] |
| [TV3Parla+ParlamentParla][2]       v0.2 | català  | model acústic  | GNU AGPL-3.0  | [enllaç][M0.4] |
| [TV3Parla Corpus][4]               v0.3 | català  | corpus d'àudio | CC-BY-NC 4.0  | [enllaç][Ctv3] |
| [ParlamentParla Corpus][3]         v2.0 | català  | corpus d'àudio |  CC-BY 4.0    | [enllaç][Cp2.0]|
| [ParlamentParla Corpus - clean][3] v1.0 | català  | corpus d'àudio |  CC-BY 4.0    | [enllaç][CpC]  |
| [ParlamentParla Corpus - other][3] v1.0 | català  | corpus d'àudio |  CC-BY 4.0    | [enllaç][CpO]  |
| [ParlamentParla Corpus - old][3]   v0.3 | català  | corpus d'àudio |  CC-BY 4.0    | [enllaç][Cp0.3]|
| [Catotron - Ona][6]                     | català  | model de SDV   | CC-BY 4.0     | [enllaç][TTSOnaModel] |
| [Catotron - Pau][6]                     | català  | model de SDV   | CC-BY 4.0     | [enllaç][TTSPauModel] |
| [UPC FestCat Ona - optimitzat][5]       | català  | corpus d'àudio |  CC BY-SA 3.0 ES   | [enllaç][TTSOna]|
| [UPC FestCat Pau - optimitzat][5]       | català  | corpus d'àudio |  CC BY-SA 3.0 ES   | [enllaç][TTSPau]|
| OpenSubtitles LM                   v1.0 | català  | model d'idioma |  CC-BY 4.0    | [enllaç][LMos] |
 
<br/>

## Corpora acústics

Durant diversos projectes, vam recollir enregistraments de veu disponibles públicament i els vam convertir en corpora acústics per entrenament dels sistemes de RAP. Aquests conjunts de dades es poden descarregar amb diferents llicències obertes.

### TV3Parla

  Aquest corpus inclou 240 hores de parla catalana de material audiovisual. Els detalls de la segmentació, el processament de dades i l'entrenament del model s'expliquen en [Külebi, Öktem; 2018](https://www.isca-speech.org/archive/IberSPEECH_2018/abstracts/IberS18_P1-2_Kulebi.html). El propietari del contingut original és la Corporació Catalana de Mitjans Audiovisuals, SA (CCMA); vam processar el seu material i estem fent-lo disponible aquí sota els seus [termes d'ús](http://www.ccma.cat/avis-legal/condicions-utilitzacio-del-portal/).

  El corpus es pot trobar [aquí][Ctv3] sota la llicència [CC BY-NC 4.0][ccbync].  

  *Aquest projecte va ser possible gràcies al suport [d'Associació Softcatalà](https://www.softcatala.org/).*


### ParlamentParla

Vam recollir aquest corpus a partir dels enregistraments i les transcripcions dels plens del [Parlament de Catalunya](https://www.parlament.cat/). Vam alinear les transcripcions amb els enregistraments i vam extreure les 320 hores més netes per a entrenar els models de parla. El contingut pertany al Parlament de Catalunya i les dades es publiquen conforme a les seves [condicions d'ús](https://www.parlament.cat/pcat/serveis-parlament/avis-legal/).

El [corpus antic de la v0.3][Cp0.3] inclou els enllaços del text sencer i l'àudio, per intervenció. 

A partir de la versió 1.0 actual, podeu trobar els fitxers d'àudio segmentats i les transcripcions en dues parts; 90 hores de qualitat [neta][CpC] i 230 hores de qualitat [altra][CpO], ambdues sota la llicència [CC BY 4.0][ccbync].

A partir de la versió 2.0 actual, el corpus s'amplia i se separa en 211 hores de qualitat neta i 400 hores de qualitat altra. A més, cada segment de la parla està etiquetat amb el seu parlant i cada parlant amb el seu gènere.

*Versió 1.0 de aquest corpus va ser possible gràcies al suport del [Departament de Cultura](http://cultura.gencat.cat/) de la Generalitat. Versió 2.0 va ser finançat pel Centre Nacional de Supercomputació, en el marc del projecte [AINA](http://aina.gencat.cat/) del [Departament de Polítiques Digitals](https://politiquesdigitals.gencat.cat/).*

### Corpus UPC FestCat SDV

[Corpus FestCat](http://festcat.talp.cat/en/) va ser desenvolupat pel Centre de Recerca TALP de la Universitat Politècnica de Barcelona l'any 2007 per construir sistemes SDV de codi obert per al català. Hem reprocessat aquest corpus optimitzant-lo per construir el nostre SDV [Catotron][catotron] basat en la xarxes neuronals. Els segments llargs es van dividir o es van descartar per tenir una durada màxima d'àudio de 12 segons. El corpus de veu masculina [Pau][TTSPau] conté 6 hores 54 minuts i el corpus de veu femenina [Ona][TTSOna] conté 6 hores 12 minuts. Tots dos es publiquen amb llicència [Reconeixement-CompartirIgual 3.0 Espanya (CC BY-SA 3.0 ES)][ccsaes].

*La preparació d'aquest corpus va comptar amb el suport del [Departament de Cultura de la Generalitat de Catalunya](http://cultura.gencat.cat/)*

## Models de RAP

Aquí teniu els models de RAP que vam entrenar nosaltres a partir dels corpora mencionats abans. Per ara vam utilitzar el toolkit de reconeixement de la parla, [CMUSphinx](https://cmusphinx.github.io/). Continuem el nostre treball de manteniment i millora dels models en el nostre [repositori](https://github.com/collectivat/cmusphinx-models). Podeu trobar guies d'instal·lació i configuració, i tutorials dels casos d'ús bàsic al nostre [wiki][wiki].

* [TV3Parla v0.3][M0.3]: `sphinxtrain` 5pre-alpha continuous model
* [TV3Parla+ParlamentParla v0.2][M0.4]: `sphinxtrain` 5pre-alpha continuous model
 
## Models de SDV

[Catotron][catotron] és el primer sistema de síntesi de veu lliure i obert basat en xarxes neuronals. Col·lectivaT ha liderat el desenvolupament amb el finançament del [Departament de Cultura de la Generalitat de Catalunya](http://cultura.gencat.cat/) amb la participació d'investigadors del [Grup de recerca en Tractament del Llenguatge Natural (TALN)][taln] de la Universitat Pompeu Fabra i [Centre de Tecnologies i Aplicacions del Llenguatge i de la Parla de la Universitat Politècnica de Catalunya (UPC-TALP)][talp].

- [Pàgina oficial][catotron]
- [Blog del projecte](/blog/2019-12-05-speech-synthesis-dl/) amb enllaços a models (Ona, Pau, Waveglow, MelGAN) i mostres
- [Codi font per a GPU](http://github.com/CollectivaT-dev/catotron) i [CPU](http://github.com/CollectivaT-dev/catotron-cpu)
- [Quaderns Jupyter](http://github.com/CollectivaT-dev/TallersParla) per a inferència i adaptació de parlants

Per obtenir més informació, podeu consultar [el nostre article publicat a Interspeech 2020][interspeech2020].


<br/>  
<br/> 
<br/>

*La preparació d'aquesta pàgina va ser possible amb el suport del [Departament de Cultura](http://cultura.gencat.cat/) de la Generalitat.*

<img src="/img/logo_generalitat.png" width="400"/>

[wiki]: https://github.com/collectivat/cmusphinx-models/wiki
[catotron]: http://catotron.cat/
[interspeech2020]: https://www.isca-speech.org/archive/interspeech_2020/kulebi20_interspeech.html
[taln]: https://www.upf.edu/web/taln
[talp]: https://www.talp.upc.edu/
[ccby]: https://creativecommons.org/licenses/by/4.0/
[ccbync]: https://creativecommons.org/licenses/by-nc/4.0/
[ccsaes]: https://creativecommons.org/licenses/by-sa/3.0/
[gapgl]: https://www.gnu.org/licenses/agpl-3.0.html
[Ctv3]: http://laklak.eu/share/tv3_0.3.tar.gz
[CpC]: http://laklak.eu/share/parlament_v1.0_clean.tar.gz
[CpO]: http://laklak.eu/share/parlament_v1.0_other.tar.gz
[Cp0.3]: http://laklak.eu/share/parlament_0.2.tar.gz
[Cp2.0]: https://zenodo.org/record/5541827
[M0.3]: https://cloud.laklak.eu/s/MY0SYpTap8w0WuK
[M0.4]: https://cloud.laklak.eu/s/4o2b5MrHckMYCXo
[LMos]: https://cloud.laklak.eu/s/zY7J2jGD8Hgnzpj
[LMvq]: https://cloud.laklak.eu/s/dXCsjqSfjk6Eo7R
[TTSOna]: http://laklak.eu/share/upc_ona_data.tar.gz
[TTSPau]: http://laklak.eu/share/upc_pau_data.tar.gz
[TTSOnaModel]: https://drive.google.com/open?id=1-fdWV-aH5nIRv1rZKQYInsRes2At74xG
[TTSPauModel]: https://drive.google.com/open?id=1-T2nHQNEE8mXPaT-ulDSAXgdGSzomPMu
[1]: #corpora-acústics
[2]: #models-de-rap
[3]: #parlamentparla
[4]: #tv3parla
[5]: #corpus-upc-festcat-sdv
[6]: #models-de-sdv
