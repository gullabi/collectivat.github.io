---
layout: post
title: "SuportMuTu: La resposta de Col·lectivaT a la pandèmia"
ref: suportmutuclose
thumbnail: /img/blog/2020/suportmutu.png
lang: ca
summary: "En aquesta entrada, presentarem la nostra resposta a la pandèmia Covid-19 a Barcelona via el nostre projecte SuportMuTu. SuportMuTu pretenia ampliar l’abast dels canals d’informació i solidaritat durant el període més estricte de la pandèmia, amb una traducció col·laborativa impulsada per la intel·ligència artificial."
---

_En aquesta entrada, presentarem la nostra resposta a la pandèmia Covid-19 a Barcelona via el nostre projecte SuportMuTu. SuportMuTu pretenia ampliar l’abast dels canals d’informació i solidaritat durant el període més estricte de la pandèmia, amb una traducció col·laborativa impulsada per la intel·ligència artificial._

<p align="center"><img src="/img/blog/2020/suportmutu_landscape.png" alt="SuportMuTu logo" width="70%"></p>

## Per i per a què SuportMuTu?

Ja fa més d’un any que la dura realitat de la pandèmia del coronavirus ha entrat a les nostres vides. Per evitar un col·lapse total del sistema, la societat va adaptar-se a les extremes mesures adoptades a nivell local i global. No obstant això, hem vist que sovint les mesures no van tenir els mateixos efectes en diferents sectors de la societat. Un d’aquells sectors són els col·lectius marginats, que han afrontat cada vegada més obstacles socioeconòmics i lingüístics a l'hora d'accedir a la informació, la salut i els serveis socials.

Amb les mesures de confinament, tant les xarxes oficials com les comunitàries van reforçar la seva presència al domini digital. Per exemple, les autoritats sanitàries van augmentar l’ús dels canals informatius i bots de xat en serveis de missatgeria instantània, com Telegram i Whatsapp. Les xarxes de suport als barris també van adaptar-s'hi, traslladant les comunicacions a la línia, per consolidar la solidaritat, ajudar la gent a expressar les seves necessitats i organitzar-se a nivell local.

__Col·lectivaT__ és una cooperativa constituïda per persones d'origen migrant. El nostre enfocament sempre s’ha centrat en les àrees d’exclusió existents a la societat, on, la majoria de les vegades, les realitats dels grups marginats són invisibilitzades. Veient aquests espais digitals recents, no vam tardar gaire en detectar les possibles dificultats que la ciutadania d’origen migrant podria trobar-se per accedir-hi. La llengua principal d’aquests canals és el català, una llengua no sempre dominada per les persones d'origen estranger. Creiem que els diferents origins lingüístics no han de ser una barrera per accedir al coneixement i per donar-se suport mútu en temps de crisi. 

## Què és SuportMuTu?

SuportMuTu pretenia garantir l'accessibilitat dels canals de protocol sanitari de Catalunya i dels grups de solidaritat veïnal de Barcelona, per a algunes de les llengües no llatines més comunes en aquesta ciutat: àrab, urdú i xinès. En combinar la tecnologia lingüística basada en la intel·ligència artificial (IA) amb una xarxa de persones voluntàries, SuportMuTu va ajudar a oferir els canals de Telegram en aquestes llengues en paral·lel a les seves versions originals en català o castellà, perquè tothom pogués informar-se i donar suport mútu durant el confinament.

## Com funciona?

El següent diagrama mostra un exemple del procés a la infraestructura del SuportMuTu. Hi veiem la ruta d'un missatge publicat a [_@SalutCat_, el canal oficial de Departament de Salut de Catalunya][salutcat], arribant al públic de parla àrab. 

<p align="center"><img src="/img/blog/2021/SuportMuTu_diagram_ca.png" alt="SuportMuTu diagram" width="70%"></p>

Tot el procés es gestiona pel nostre bot de Telegram: _SuportMuTuBot_. Quan un missatge es publica al canal SalutCat, SuportMuTuBot l'agafa automàticament. A continuació, el missatge es tradueix a l’àrab mitjançant un sistema de traducció automàtica. Per evitar qualsevol error en la traducció, el missatge traduït automàticament es dirigeix al grup de Telegram de la comunitat voluntària de parla àrab per a la verificació. Poden acceptar la traducció automàtica tal com és, o bé poden corregir-la i enviar-la de nou a SuportMuTuBot. Llavors, SuportMuTuBot dirigeix la traducció verificada a la versió àrab del canal SalutCat, afegint-hi un enllaç del missatge original. Finalment, el missatge en àrab es converteix en àudio mitjançant un sistema de síntesi de veu perquè també es pugui escoltar. 

SuportMuTu és una tecnologia orientada a i impulsada per la gent. Posa les persones al centre i fa que tot el procés depengui de la verificació humana. La logística de missatgeria i la IA s’utilitzen només per fer el procés més eficient i gestionable de manera fàcil per les voluntàries. 

El següent mini-vídeo mostra el funcionament d'un grup de voluntàries que comuniquen amb SuportMuTuBot. SuportMuTuBot redirigeix els missatges com a tasques al grup de voluntàries i qualsevol membre disponible pot encarregar-se d'una tasca que vulgui. El grup comunica amb el bot via ordres bàsiques i senzilles. Per exemple, escriure `/task` (tasques) llista els missatges pendents de traducció. `/take 29` (agafar 29) s'utilitza per agafar la tasca número 29 i rebre la traducció automàtica. `/send` (enviar) verifica la traducció i SuportMuTuBot s'encarrega de difondre-la al canal corresponent.

<p align="center"><a href="/img/blog/2020/suportMuTu_short.gif"><img src="/img/blog/2020/suportMuTu_short.gif" alt="SuportMuTu workflow" width="40%"></a></p>

## Implementació del projecte

Vam dissenyar el projecte SuportMuTu, finançat per el micromecenatge Fons Cooperatiu per l'Emergència Social i Sanitària ([Fons Cooperatiu per l'Emergència Social i Sanitària][goteo]), durant les primeres setmanes del confinament. Vam dedicar les primeres setmanes del projecte a prototipar i poblar grups i canals candidats. En la nostra investigació, vam detectar 40 xarxes de solidaritat organitzades en diversos barris de Barcelona. Podeu accedir a la llista completa d’aquests grups i canals des de [DADESS][dadess].

Vam tenir en compte diversos factors per decidir amb quines llengües iniciar. El factor principal va ser el nombre de parlants que podríem arribar amb cada llengua. Vam enumerar els col·lectius d'orígen estranger més nombrosos de Barcelona i vam identificar-ne aquells que tenen una llengua nacional d’origen no europeu i no llatí. Segons [l'informe de l'Ajuntament][ajuntamentreport], aquests col·lectius per ordre de població eren: xinès (21,658), pakistanès (20,643), marroquí (14,418), i filipí (9,439). Limitant el marc inicial a tres idiomes, vam decidir llançar les llengües oficials més parlades d’aquests col·lectius: xinès, urdú i àrab.

### Avaluació de la qualitat de la traducció automàtica 

Tot i que la traducció automàtica ha avançat força en els darrers anys, no s'apropa gens a ser perfecta. Per determinar la usabilitat en el nostre cas, vam realitzar avaluacions preliminars dels motors de traducció automàtica disponibles. Ho vam fer per preveure el volum de treball de correcció que necessitarien les traduccions automàtiques en aquestes llengües; i sobretot perquè la informació difosa era important, fins i tot crucial, on no hi podria haver cap marge per al menor error o malentès. Vam preparar una enquesta pública amb 5 missatges de diferent complexitat, amb les seves traduccions a l'urdú i l'àrab. Vam demanar al públic participant que valoressin la qualitat de la traducció en general i a quina escala es va transmetre el missatge correctament; les dues coses tant en una escala de 5, 1: pitjor i 5: perfecta. Vam obtenir 4 respostes per l'àrab i 2 per l'urdú. 

<!-- |         |  Mtj. qualitat traducció   |   Mtj. missatge transmès   |
|---------|:--------------------------:|:--------------------------:|
| urdú    |   1.90                     |    1.80                    |
| àrab    |   2.80                     |    3.55                    |
| MITJANA |   3.10                     |    3.31                    |
 -->
<center>
<table class="tg">
<thead>
  <tr>
    <th class="tg-lqy6"></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Mtj. qualitat traducció</span></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Mtj. missatge transmès</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-lqy6">urdú</td>
    <td class="tg-c3ow">1.90</td>
    <td class="tg-c3ow">1.80</td>
  </tr>
  <tr>
    <td class="tg-lqy6">àrab</td>
    <td class="tg-c3ow">2.80</td>
    <td class="tg-c3ow">3.55</td>
  </tr>
  <tr>
    <td class="tg-lqy6"><span style="font-weight:bold">MITJANA</span></td>
    <td class="tg-c3ow">3.10</td>
    <td class="tg-c3ow">3.31</td>
  </tr>
</tbody>
</table>
</center>

Les puntuacions van ser una mica superiors a la mitjana per l'àrab i molt més baixes per l'urdú. En veure aquests resultats, vam confirmar la idea de que la verificació humana era essencial.

### Arribar als grups voluntaris

[La nostra primera crida a les voluntàries][formulari] va ser el 12 de maig del 2020. Tot i rebre diverses voluntàries per a cada llengua, degut a les circumstàncies i al canvi constant de disponibilitat de les persones en tal circumstàncies, al final vam aconseguir reclutar cinc persones voluntàries: dues traductores de la cooperativa [Espai Travinae][travinae] per xinès, dues parlants de l'àrab i una de l'urdú.

Tot l'equip voluntari va rebre una formació pràctica d’almenys una hora sobre com interactuar amb el SuportMuTuBot. Van continuar autoformant-se i practicant en un entorn de proves, un canal _sandbox_ de Telegram, fins sentir-se còmodes amb la interfície i migrar al grup comunitari de SuportMuTu corresponent. Durant aquest període vam assegurar que els seus dubtes sobre el funcionament del bot estiguessin aclarits. A més, vam actualitzar la interfície i les ordres segons els seus comentaris i necessitats, sempre que fos possible, per fer-les més fàcil d'utilitzar.

### Canals SuportMuTu

Ens vam posar personalment en contacte amb els i les administradores d’onze canals de barri demanant-los la aprovació per ampliar els seus canals amb SuportMuTu. Vam rebre dues respostes affirmatives, que era suficient per engegar el projecte: [_SuportMutu Gràcia_ (@suportgracia)][suportgracia] i [_Xarxa de Suport Verdum_ (@XarxadeSuportVerdum)][XarxadeSuportVerdum]. També vam crear versions del canal SalutCat en tres idiomes. A continuació és la cronologia de les dates de marxa de tots els canals de SuportMuTu:

<p align="center"><img src="/img/blog/2021/suportmutu_timeline_en.png" alt="SuportMuTu timeline" width="70%"></p>


## Resultats i observacions

La següent taula exposa en resum el treball de traducció realitzat en el marc del projecte: del 21 d'abril del 2020, quan es crea el primer canal; al 30 de juny del 2020, quan el projecte és finalitzat.

<!-- |                     |  Missatges rebuts |           | Missatges/paraules traduïts |         |
|--------------------:|:-----------------:|:---------:|:-------------------------:|:-------:|
|                     |                   |    àrab   |           xinès           |  urdú   |
|        SuportGracia |         91        |  27/2124  |          16/1282          | 13/1575 |
|            SalutCat |         90        |   12/973  |          18/1375          | 17/1043 |
| XarxadeSuportVerdum |        115        |  26/1938  |          24/2177          |    -    |
|               TOTAL |        296        |           |          153/12487        |         | -->

<center>
<table class="tg">
<thead>
  <tr>
    <th class="tg-dvpl"></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Missatges rebuts</span></th>
    <th class="tg-c3ow" colspan="3"><span style="font-weight:bold">Missatges/paraules traduïts </span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-dvpl"></td>
    <td class="tg-c3ow"></td>
    <td class="tg-dvpl">àrab </td>
    <td class="tg-c3ow">xinès</td>
    <td class="tg-0pky">urdú</td>
  </tr>
  <tr>
    <td class="tg-dvpl">SuportGracia</td>
    <td class="tg-c3ow">91</td>
    <td class="tg-dvpl">27/2124</td>
    <td class="tg-c3ow">16/1282</td>
    <td class="tg-0pky">13/1575</td>
  </tr>
  <tr>
    <td class="tg-dvpl">SalutCat</td>
    <td class="tg-c3ow">90</td>
    <td class="tg-dvpl">12/973</td>
    <td class="tg-c3ow">18/1375</td>
    <td class="tg-0pky">17/1043</td>
  </tr>
  <tr>
    <td class="tg-dvpl">XarxadeSuportVerdum</td>
    <td class="tg-c3ow">115</td>
    <td class="tg-dvpl">26/1938</td>
    <td class="tg-c3ow">24/2177</td>
    <td class="tg-c3ow">-</td>
  </tr>
  <tr>
    <td class="tg-dvpl"><span style="font-weight:bold">TOTAL</span></td>
    <td class="tg-c3ow">296</td>
    <td class="tg-dvpl">153/12487</td>
    <td class="tg-c3ow"></td>
    <td class="tg-c3ow"></td>
  </tr>
</tbody>
</table>

</center>

Podem reflexionar sobre l’eficàcia de SuportMuTu de tres maneres: Funcionalitat del sistema, experiència del voluntariat, i arribada a la comunitat. Vam veure que el SuportMuTuBot va funcionar molt bé en informar les voluntàries sobre l'entrada de missatges recents. La taxa global de traducció va ser 51%, tot i que cal remarcar que alguns missatges no van ser traduïts intencionadament, degut a la falta de text (vídeos, fotos), caducitat, repetició i/o irrellevància.

Els i les voluntàries ens van informar que treballar en traduccions ja fetes va accelerar molt el treball de traducció que calia fer. A més, vam observar que la interfície senzilla era molt fàcil d’agafar, ja que hi havia poques vegades que va ser necessària una intervenció tècnica. 

### Reptes i reflexions

El primer repte del projecte va ser convèncer les comunitats locals de la ciutat perquè integressin els seus canals amb SuportMuTu. Els barris que van mostrar interès, com Gràcia i Nou Barris, estaven molt animats per col·laborar des de l'inici. No obstant, ens va sorprendre molt veure la falta total d’interès per part dels grups de districtes coneguts per la seva diversitat cultural, de col·lectius ´d'origen, com ara El Raval i Badalona. A través d'aquest procés, ens vam adonar de que no totes les comunitat estaven realment interessades en augmentar l'accessibilitat lingüística dels seus canals comunicatius, o bé, podem suposar que tenien altres mitjans més eficaços que l'extensió SuportMutu.

El segon repte va ser a l'hora de reclutar les i les voluntàries per donar suport al projecte. La nostra crida a les xarxes socials i als contactes de les xarxes personals i col·lectives no va poder arribar a les comunitat a les qual preteniem oferir l'eina. No totes les candidates que vam aconseguir arribar estaven segures del seu català, poques tenien una disponiblitat contíua en les circumstàncies, algunes altres van haver d'abandonar el projecte degut als canvis en la seva situació personal, i algunes estaven interessades més amb una feina remunerada tradicional i regular que un treball innovador basat en la comunitat. Al principi no vam poder prometre una compensació econòmica, a causa de l'escala impredictible de la tasca, tot i que al final del project vam remunerar proporcionalment les contribucions de les nostres cinc voluntàries. De l'altra banda, val a dir que gràcies a aquest projecte, encara estem en contacte amb el grup voluntari i seguim col·laborant en altres projectes.

L'última dificultat que vam trobar era atreure les comunitats de parla àrab, xinesa i urdú a seguir els canals traduïts. Ho atribuïm a tres raons principals. La primera és que la majoria dels grups veinals és una minoria d'activistes que operen en un cercle i no sempre són coneguts per les comunitats d'origen migrant _i_ no migrant. Encara que l’interès per arribar altres sectors va créixer durant el confinament, els mateixos grups veinals tampoc no van poder arribar-ne un gran nombre de seguidores.

La segona raó té a veure amb els obstacles tècnics. En el termini disponible, només vam poder configurar el marc d'SuportMuTu en Telegram, per la flexibilitat de programació i les capacitats de creació de bot d'aquesta missatgería. Tot i que la seva base d’usuaris segueix creixent cada cop més, no deixa de quedar darrere de WhatsApp. També vam veure que la comunitat xinesa feia servir de manera més activa l’aplicació WeChat, i no tant el Telegram. Creiem que perquè SuportMutu tingui un impacte real, s'ha d'adaptar als costums tecnològics de les comunitats que s'adreça. 

Finally but most importantly, we believe that the existing gaps between diverse communities made it unattractive for them to integrate to spaces they have little voice in. SuportMuTu showed as an experiment that linguistic accessibility is not the only obstacle in bonding the connection between communities of diverse origins. It would have been naive to expect that a technological tool would be able to organize and transform certain realities of the society without a popular activist support. 

## Conclusions

SuportMuTu has been a unique way of response in a very unique time demanded by the pandemic. For many, the introduction of confinement measures has been a radical change to the digital realm –be it for working, studying, organizing or getting informed. SuportMuTu showed that this change could be made in a way that doesn’t make language a barrier and even serve to create bonds in different sections of the community. We have set up a volunteer network powered by a digital infrastructure in a matter of weeks to address a very specific problem. Although it hasn’t reached a grand impact, we believe that it could be a blueprint for culturally-aware technology development. We are inviting developers, public institutions and activists to collaborate and apply in their own context. For that, we open-source our codebase in [Github][github].

For questions and collaboration please leave us a note at _info-at-collectivat.cat_. 

[goteo]: https://ca.goteo.org/project/fons-cooperatiu-front-l-emergencia-social-i-sanita
[github]: https://github.com/CollectivaT-dev/suport_mt
[formulari]: https://limesurvey.collectivat.cat/index.php?r=survey/index&sid=695434
[salutcat]: https://t.me/salutcat
[salutcat_ur]: https://t.me/salutcat_ur
[salutcat_ar]: https://t.me/salutcat_ar
[salutcat_zh]: https://t.me/salutcat_zh
[suportgracia]: https://t.me/suportgracia
[suportgracia_ur]: https://t.me/suportgracia_ur
[suportgracia_ar]: https://t.me/suportgracia_ar
[suportgracia_zh]: https://t.me/suportgracia_zh
[XarxadeSuportVerdum]: https://t.me/XarxadeSuportVerdum
[XarxadeSuportVerdum_ar]: https://t.me/XarxadeSuportVerdum_ar
[XarxadeSuportVerdum_zh]: https://t.me/XarxadeSuportVerdum_zh
[economiaperlavida]: http://www.economiaperlavida.cat/
[dadess]: https://open.dadess.cat/dataset/suport-mutu-covid19
[travinae]: https://www.travinae.com/
[ajuntamentreport]: https://ajuntament.barcelona.cat/premsa/wp-content/uploads/2019/07/pobest19.pdf


