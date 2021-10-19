---
layout: post
title: "SuportMuTu: Col·lectivaT’s response to the pandemic"
ref: suportmutuclose
thumbnail: /img/blog/2020/suportmutu_landscape.png
lang: en
summary: "In this post, we will report on our response to the Covid-19 pandemic in Barcelona with our project SuportMuTu. SuportMuTu aimed to extend the reach of information and solidarity channels during the strictest period of the pandemic, with artificial intelligence-powered collaborative translation."
---

_In this post, we will report on our response to the Covid-19 pandemic in Barcelona with our project SuportMuTu. SuportMuTu aimed to extend the reach of information and solidarity channels during the strictest period of the pandemic, with artificial intelligence-powered collaborative translation._

<p align="center"><img src="/img/blog/2020/suportmutu_landscape.png" alt="SuportMuTu logo" width="70%"></p>

## Why SuportMuTu?

It has been over a year now since the harsh reality of the Coronavirus pandemic has entered our lives. In order to avoid a total system collapse, the society adapted to extreme measures taken on local and global level. However, we have seen that many times the measures developed didn’t have the same effects on different sectors of the society. One of them is marginalized populations who have faced increasing socio-economic and linguistic obstacles in accessing information, healthcare and social services. 

With the social distancing measures, both official and community networks have strengthened their presence in the digital domain. For example, health authorities have augmented the use of informative channels and chatbots in instant messaging services like Telegram and Whatsapp. Neighbourhood support networks have also adapted by moving their communications online for building solidarity, helping people voice their needs and to organize locally. 

__Col·lectivaT__ is a cooperative founded by persons of migrant origin. Our focus has always been on exclusion areas existing in the society, where, most of the time, the realities of the marginalized are made invisible. Looking at these newly created digital spaces, we haven’t taken much time to detect the possible difficulties that citizens of migrant origins could face in accessing them. The main language in these channels is Catalan, which is not always dominated by persons of non-European and non-American origin. We believe that different linguistic backgrounds shouldn’t be a barrier in accessing knowledge and supporting each other in a time of crisis. 

## What is SuportMuTu?

SuportMuTu aimed to guarantee the accessibility of Catalonia’s health protocol channels and Barcelona’s neighbourhood solidarity groups into some of the most common non-Latin migrant languages of Barcelona: Arabic, Urdu and Chinese. By combining AI-based language technology with a volunteer network, SuportMuTu helped serve Telegram channels in these languages in parallel to their original versions so that everyone can get informed and support each other during the lockdown. 

## How does it work?

The diagram below demonstrates a sample process of the SuportMuTu framework. In this example, you see the path of a message published in [_@SalutCat_, the official channel of Catalonia’s Health Department][salutcat], reaching to the Arabic speaking public. 

<p align="center"><img src="/img/blog/2021/SuportMuTu_diagram_en.png" alt="SuportMuTu diagram" width="70%"></p>

The whole process is managed by our Telegram bot: _SuportMuTuBot_. Once a message is published in SalutCat channel, SuportMuTuBot picks it automatically. Next, the message is translated into Arabic using a machine translation system. In order to avoid any errors in the translation, automatically translated message is directed to the community group of volunteer Arabic speakers for verification. They can either accept this translation as it is, or edit and send it back to SuportMuTuBot. SuportMuTuBot then directs the verified translation into the Arabic version of SalutCat channel, adding a link to the original message. Finally, the message is converted to audio using a speech synthesis system so that it can be listened to as well. 

SuportMuTu is a people-facing and people-powered technology. It places human in the centre by making the whole process dependent on human verifiers. Message logistics and artificial intelligence is used only to make the process more efficient and easily-manageable by the volunteers. 

The animation below demonstrates the functioning of a volunteer group communicating with SuportMuTuBot. SuportMuTuBot redirects the messages to the volunteer group as tasks and they can be taken by any volunteer who is available. Volunteers communicate with the bot with simple commands. For example typing `/task` lists the messages pending translation. `/take 29` is used to take the task number 29 and get its machine translated version. `/send` verifies the translation and SuportMuTuBot takes care of disseminating it to the correct channel.

<p align="center"><a href="/img/blog/2020/suportMuTu_short.gif"><img src="/img/blog/2020/suportMuTu_short.gif" alt="SuportMuTu workflow" width="40%"></a></p>

## Project implementation

SuportMuTu project was designed in the first weeks of the confinement and funded by the crowdsourced Cooperative Social and Health Emergency Fund ([Fons Cooperatiu per l'Emergència Social i Sanitària][goteo]). We have dedicated the first weeks of the project in prototyping and populating candidate groups and channels. In our research, we have detected 40 solidarity networks organized in various neighbourhoods of Barcelona. The complete list of these groups and channels is accessible from [DADESS][dadess].

We have considered a number of factors to decide which languages to launch. Our principal factor was the number of speakers we could reach with each language. We have listed the most numerous foreigner populations of Barcelona and listed those who have national language(s) of non-Latin-origin. According to the [municipality's report][ajuntamentreport], these in the order of population were: Chinese (21,658), Pakistani (20,643), Moroccan (14,418) and Filipino (9,439). Limiting the initial scope to three languages, we have decided to launch with the most spoken official languages of these populations: Mandarin Chinese, Urdu and Arabic. 

### Evaluating quality of machine translation 

Although machine translation has progressed greatly in the last years, it is no way close to being perfect. To assess the usability in our case, we have performed preliminary evaluations of available machine translation engines. We did this to predict how much correction work the automatic translations would need in these languages, especially because the information disseminated was important; even crucial where there could not have been any margin for the smallest error or misunderstanding. We prepared a public survey with 5 messages and their translations in Urdu and Arabic. We asked the participants to rate the general translation quality and to what scale the message was transmitted, both on a scale of 5, 1 being worst and 5 being perfect. We obtained 4 responses for Arabic and 2 for Urdu. 


<!-- |         |  Avg. translation quality  |  Avg. message transmitted  |
|---------|:--------------------------:|:--------------------------:|
| Urdu    |   1.90                     |    1.80                    |
| Arabic  |   2.80                     |    3.55                    |
| AVERAGE |   3.10                     |    3.31                    | -->

<center>
<table class="tg">
<thead>
  <tr>
    <th class="tg-lqy6"></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Avg. translation quality</span></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Avg. message transmitted</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-lqy6">Urdu</td>
    <td class="tg-c3ow">1.90</td>
    <td class="tg-c3ow">1.80</td>
  </tr>
  <tr>
    <td class="tg-lqy6">Arabic</td>
    <td class="tg-c3ow">2.80</td>
    <td class="tg-c3ow">3.55</td>
  </tr>
  <tr>
    <td class="tg-lqy6"><span style="font-weight:bold">AVERAGE</span></td>
    <td class="tg-c3ow">3.10</td>
    <td class="tg-c3ow">3.31</td>
  </tr>
</tbody>
</table>
</center>

The scores were slightly higher than average for Arabic and way poorer for Urdu. Looking at this results, we have confirmed our idea that human verification was essential.

### Volunteer reach

[Our initial call for volunteers][firstblogcall] was made on May 12th. Even though we received several volunteers for each language, due to the circumstances and the constant change in availability of the people under such circumstances, at the end we managed to recruit five volunteers: two translators from [Travinae cooperative][travinae] for Chinese, two Arabic and one Urdu speakers.

All volunteers were given at least a one-hour-practical training on how to interact with SuportMuTuBot. They continued self-training and practicing in a sandbox Telegram channel until they felt comfortable with the interface and migrated to the corresponding SuportMuTu community group. During this time we made sure to clear their doubts regarding the functioning. We also updated the interface according to their comments and needs, if and when possible, to make it more user friendly.

### SuportMuTu channels

We have personally contacted the administrators of eleven neighborhood channels asking for their approval in amplifying their channels with SuportMuTu. We received positive responses from two of them, which were good enough to kickstart the project: [_SuportMutu Gràcia_ (@suportgracia)][suportgracia] and [_Xarxa de Suport Verdum_ (@XarxadeSuportVerdum)][XarxadeSuportVerdum]. We also created versions of the SalutCat channel in three languages. Below is the timeline of launch dates of all SuportMuTu channels:

<p align="center"><img src="/img/blog/2021/suportmutu_timeline_en.png" alt="SuportMuTu timeline" width="70%"></p>


## Results and reflections

Below table summarizes the translation work done within the scope of the project: From April 21, when the first channel is opened, until June 30, when the project was terminated.

<!-- |                     | Messages received |           | Messages/words translated |         |
|--------------------:|:-----------------:|:---------:|:-------------------------:|:-------:|
|                     |                   |  Arabic   |          Chinese          |   Urdu  |
|        SuportGracia |         91        |  27/2124  |          16/1282          | 13/1575 |
|            SalutCat |         90        |   12/973  |          18/1375          | 17/1043 |
| XarxadeSuportVerdum |        115        |  26/1938  |          24/2177          |    -    |
|               TOTAL |        296        |           |          153/12487        |         | -->

<center>
<table class="tg">
<thead>
  <tr>
    <th class="tg-dvpl"></th>
    <th class="tg-c3ow"><span style="font-weight:bold">Messages received</span></th>
    <th class="tg-c3ow" colspan="3"><span style="font-weight:bold">Messages/words translated </span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-dvpl"></td>
    <td class="tg-c3ow"></td>
    <td class="tg-dvpl">Arabic </td>
    <td class="tg-c3ow">Chinese</td>
    <td class="tg-0pky">Urdu</td>
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

### Challenges

First challenge in the project was convincing city’s local communities to integrate their channels with SuportMuTu. The ones that showed interest like Gràcia and Nou Barris were very keen in collaborating from the beginning. However, we were surprised to see a complete lack of interest by groups of districts that are known to have culturally diverse populations like El Raval and Badalona. We realized through this process that not all communities were actually interested in increasing the linguistic accessibility of their communication channels, or we can assume that they had other means more effective than SuportMutu extension. 

Second challenge we faced was in recruiting volunteers to support the project. Our social media calls and personal and collective network contacts failed to penetrate into the communities we intended to serve. From the candidates we have reached, not all were confident with Catalan, few had a rather continuous availability under the circumstances, a few other had to drop out after the changes in their conditions, and some were interested in a traditional constant paid job rather than an innovative community-based work. Due to the unpredictable scale of the work, we weren’t able to promise a payment amount initially. Although, at the end of the project, we paid our five volunteers proportional to the contributions they did. On the other hand, it is worth saying that, thanks to this project, we are still in touch and collaborating with the then volunteers in other projects.

Final difficulty we faced was attracting the Arabic, Chinese and Urdu speaking communities to follow our translated channels. We attribute this to three main reasons. First is that most of the neighborhood communities are a minority of activists that usually operate in a clique and they are not widely known by communities of both migrant _and_ non-migrant origin. Even though interest to these groups grew during the lockdown, they haven’t reached great numbers of followers themselves. 

Second reason is related with technical obstacles. Within the timeframe available, we were only able to set up the SuportMuTu framework on Telegram, due to its programming flexibility and bot-building capabilities. Although its user base is constantly growing, it is still behind WhatsApp. We also saw that the Chinese community were most actively using the WeChat application. We believe that in order for SuportMuTu to be truly impactful, it needs to adapt to the technological habits of the communities addressed. 

Finally but most importantly, we believe that the existing gaps between diverse communities made it unattractive for them to integrate to spaces they have little voice in. SuportMuTu showed as an experiment that linguistic accessibility is not the only obstacle in bonding the connection between communities of diverse origins. It would have been naive to expect that a technological tool would be able to organize and transform certain realities of the society without a popular activist support. 

## Conclusion

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
[firstblogcall]: /blog/2020-05-11-suportmutu-ca/


<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-dvpl{border-color:inherit;text-align:right;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
