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

SuportMuTu project was designed in the first weeks of the confinement and funded by the crowdsourced Cooperative Social and Health Emergency Fund ([Fons Cooperatiu per l'Emergència Social i Sanitària][goteo]). We have dedicated the first weeks of the project in prototyping and populating candidate groups and channels. In our research, we have detected 40 solidarity networks organized in various neighbourhoods of Barcelona. The complete list of these groups and channels is accessible from [DADESS][dadess].

We have considered a number of factors to decide which languages to launch. Our principal factor was the number of speakers we could reach with each language. We have listed the most numerous foreigner populations of Barcelona and listed those who have national language(s) of non-Latin-origin. According to the [municipality's report][ajuntamentreport], these in the order of population were: Chinese (21,658), Pakistani (20,643), Moroccan (14,418), Filipino (9,439). Limiting the initial scope to three languages, we have decided to launch with the most spoken official languages of these populations: Mandarin Chinese, Urdu and Arabic. 

### Avaluar la qualitat de la traducció automàtica 

Although machine translation has progressed greatly in the last years, it is no way close to being perfect. To assess the usability in our case, we have performed preliminary evaluations of available machine translation engines. We did this to predict how much correction work the automatic translations would need in these languages, especially because the information disseminated was important; even crucial where there could not have been any margin for the smallest error or misunderstanding. We prepared a public survey with 5 messages and their translations in Urdu and Arabic. We asked the participants to rate the general translation quality and to what scale the message was transmitted, both on a scale of 5, 1 being worst and 5 being perfect. We obtained 4 responses for Arabic and 2 for Urdu. 

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

The scores were slightly higher than average for Arabic and way poorer for Urdu. Looking at this results, we have confirmed our idea that human verification was essential.

### Volunteer reach

[Our initial call for volunteers][formulari] was made on May 12th. Even though we received several volunteers for each language, due to the circumstances and the constant change in availability of the people under such circumstances, at the end we managed to recruit five volunteers: two translators from [Travinae cooperative][travinae] for Chinese, two Arabic and one Urdu speakers.

All volunteers were given at least a one-hour-practical training on how to interact with SuportMuTuBot. They continued self-training and practicing in a sandbox Telegram channel until they felt comfortable with the interface and migrated to the corresponding SuportMuTu community group. During this time we made sure to clear their doubts regarding the functioning. We also updated the interface according to their comments and needs, if and when possible, to make it more user friendly.

### Canals SuportMuTu

We have personally contacted the administrators of eleven neighborhood channels asking for their approval in amplifying their channels with SuportMuTu. We received positive responses from two of them, which were good enough to kickstart the project: [_SuportMutu Gràcia_ (@suportgracia)][suportgracia] and [_Xarxa de Suport Verdum_ (@XarxadeSuportVerdum)][XarxadeSuportVerdum]. We also created versions of the SalutCat channel in three languages. Below is the timeline of launch dates of all SuportMuTu channels:

<p align="center"><img src="/img/blog/2021/suportmutu_timeline_en.png" alt="SuportMuTu timeline" width="70%"></p>


## Resultats i reflexions

Below table summarizes the translation work done within the scope of the project: From April 21, when the first channel is opened, until June 30, when the project was terminated.

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

We can reflect on the effectiveness of SuportMuTu in three ways: Functionality of the system, volunteer experience and community reach. We saw that SuportMuTuBot functioned very well in informing volunteers of the incoming messages. We saw an overall translation rate of 51%. Although it has to be noted that some messages were purposefully not translated due to lack of text (videos, photos), expiration, repetition and/or irrelevance.

Volunteers have reported that working on already-made translations sped up greatly the translation work that needed to be done. Also, we noticed that the simple interface was very easy to pick up as there were very few times where technical intervention was necessary. 

### Reptes

First challenge in the project was convincing city’s local communities to integrate their channels with SuportMuTu. The ones that showed interest like Gràcia and Nou Barris were very keen in collaborating from the beginning. However, we were surprised to see a complete lack of interest by groups of districts that are known to have culturally diverse populations like El Raval and Badalona. We realized through this process that not all communities were actually interested in increasing the linguistic accessibility of their communication channels, or we can assume that they had other means more effective than SuportMutu extension. 

Second challenge we faced was in recruiting volunteers to support the project. Our social media calls and personal and collective network contacts failed to penetrate into the communities we intended to serve. From the candidates we have reached, not all were confident with Catalan, few had a rather continuous availability under the circumstances, a few other had to drop out after the changes in their conditions, and some were interested in a traditional constant paid job rather than an innovative community-based work. Due to the unpredictable scale of the work, we weren’t able to promise a payment amount initially. Although, at the end of the project, we paid our five volunteers proportional to the contributions they did. On the other hand, it is worth saying that, thanks to this project, we are still in touch and collaborating with the then volunteers in other projects.

Final difficulty we faced was attracting the Arabic, Chinese and Urdu speaking communities to follow our translated channels. We attribute this to three main reasons. First is that most of the neighborhood communities are a minority of activists that usually operate in a clique and they are not widely known by communities of both migrant _and_ non-migrant origin. Even though interest to these groups grew during the lockdown, they haven’t reached great numbers of followers themselves. 

Second reason is related with technical obstacles. Within the timeframe available, we were only able to set up the SuportMuTu framework on Telegram, due to its programming flexibility and bot-building capabilities. Although its user base is constantly growing, it is still behind WhatsApp. We also saw that the Chinese community were most actively using the WeChat application. We believe that in order for SuportMuTu to be truly impactful, it needs to adapt to the technological habits of the communities addressed. 

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


