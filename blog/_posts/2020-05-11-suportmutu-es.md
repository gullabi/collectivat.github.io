---
layout: post
title: "SuportMuTu: Accesibilidad lingüística a los canales públicos y apoyo vecinal "
ref: suportmutu
image: /img/blog/2020/suportmutu_landscape.png
thumbnail: /img/blog/2020/suportmutu.png
lang: es
summary: "Gracias a la iniciativa Economia Per La Vida, hemos creado una infraestructura digital para traducir los canales públicos y de apoyo vecinal a Telegram, a algunos idiomas de las comunidades de origen migrante de Cataluña."
---

Gracias a la iniciativa [Economia Per La Vida] [goteo], _**hemos creado una infraestructura digital para traducir los canales públicos y de apoyo vecinal a Telegram**_, a algunos idiomas de las comunidades de origen migrante de Cataluña.

Si deseas echarnos una mano, por favor ayúdanos a difundir la información sobre los canales de Telegram que hemos implementado hasta ahora:

* [/Salut (urdú)][salutcat_ur]
* [/Salut (àrab)][salutcat_ar]
* [/Salut (xinès)][salutcat_zh]
* [Suport Mutu Gràcia (urdú)][suportgracia_ar]
* [Suport Mutu Gràcia (àrab)][suportgracia_ar]
* [Suport Mutu Gràcia (xinès)][suportgracia_ar]
* [Xarxa de Suport Verdum (àrab)][XarxadeSuportVerdum_ar]

Si tienes un canal informativo de Telegram y deseas incorporar el bot en tu canal en estos idiomas, por favor escribe a: info _arroba_ collectivat.cat

## Contexto

Ante el auge de la crisis causada por la pandemia del **coronavirus** los Estados han adoptado medidas de urgencia muy severas. Sin embargo, también hay carencias en cuanto a la intervención estructural e institucional en otros problemas, que también son graves. Mientras los Estados se han concentrado en acciones que tienen finalidad de evitar el colapso del sistema sanitario, la ciudadanía se ha **auto-organizado** para tejer vías de solidaridad mutua a través de las plataformas digitales en las condiciones del estado de alarma. Hemos observado que las organizaciones vecinales y **diversos grupos antirracistas** han optado por difundir información útil a la ciudadanía en grupos y canales de chat de las aplicaciones, como WhatsApp y **Telegram.** Aparte de difundir información, muchos de estos espacios digitales también sirven para detectar las necesidades de los sectores más vulnerables de la sociedad y auto-organizarse como pueblo para responder las necesidades concretas. _Actualmente en Barcelona hay cerca de 40 redes de apoyo mutuo organizadas en varios barrios de la ciudad._

**Col·lectivaT** es una cooperativa fundada por personas de origen migrante, por lo tanto, nuestra atención siempre está dirigida a los espacios de exclusión que hay en la sociedad, que muchas veces son espacios de invisibilización de las realidades de este colectivo. Por ello, no tardamos mucho en ver los obstáculos que podrían tener **los colectivos migrantes** en el momento de acceder a **la información** que circula en estas plataformas digitales. Por muy fácil que sea el acceso a los canales-, ya que disponer de un teléfono móvil y/o una computadora en los que se puede utilizar una de estas aplicaciones es suficiente- el idioma vehicular de estos canales sabíamos que podría convertirse en una barrera para los colectivos que no dominan el catalán y/o el castellano.

A través de nuestro proyecto **SuportMuTu** queremos garantizar la transmisión de los mensajes de estos **canales de solidaridad y de apoyo vecinal** a algunos idiomas que hablan los colectivos migrantes de Cataluña _no provenientes del continente americà_. El software que desarrollamos garantizará que los canales informativos y canales de apoyo mutuo vecinales funcionen en paralelo con sus versiones en otros idiomas, como en árabe, urdu, chino, etc.

## Detalles

**SuportMuTu** es una infraestructura de software **de inteligencia artificial** que funciona con el apoyo de una **red de voluntarias correctoras.** El bot que hemos desarrollado, en primer lugar, remite los mensajes publicados en los canales de apoyo vecinal a nuestro sistema de traducción automática y este sistema envía los textos traducidos a los grupos de correctoras en idiomas correspondientes. Ellas revisan y, en su caso, corrigen los mensajes traducidos automáticamente. El mismo bot también permite la transmisión automática de los mensajes traducidos y corregidos en la versión en tal idioma del canal de apoyo vecinal, que había publicado anteriormente la versión original en catalán y/o castellano. Además, justo después de cada mensaje en formato texto, también se añade su **versión sintetizada en formato audio** con el fin de hacerlo accesible para las personas con dificultad visual o personas analfabetas.

[El código de SuportMuTu][github] es accesible a GitHub con una licencia libre. Puedes ver abajo cómo funciona SuportMuTu en práctica y cómo se hacen las revisiones, con un ejemplo de traducción del catalán al castellano:

![Como funciona](/img/blog/2020/suportMuTu_long.gif)

## Cómo colaborar

Por muy avanzados que sean los sistemas de la traducción automática, siguen haciendo errores y esto puede provocar riesgos en este tipo de situaciones en qué se traducen mensajes relacionados con la salud pública. Es por eso que las personas voluntarias que revisan y corrigen los mensajes tienen un papel clave.

Por eso estamos actualmente buscando **voluntarias** para cada idioma. Estas personas deben **entender bien el catalán/castellano escrito** (es decir, no es necesario que sepan escribir y/o hablar), y deben ser nativas o saber suficiente el idioma destino **_(árabe/hindi/bengalí/urdu/chino u otro)_** para poder **revisar la traducción automática** y la información clave. Prevemos unos 8 y 10 mensajes/día. Si hay 4 personas correctoras, sería 2-3 mensajes/día/persona (aprox. ~9-12 frases/día).

Al inicio buscamos **voluntarias,** es decir la colaboración no es remunerada. Más adelante si todo funciona bien y cuando se incorporen más grupos, decidiremos entre todas como remunerarlo.

<br/>

_**Si quieres participar como voluntaria para corregir mensajes, preferiblemente en idiomas árabe, urdu, hindi, chino, bengalí, amazigh y tagalog; por favor rellena este [formulario][formulari].**_

_**Si tienes un canal informativo de Telegram y quieres incorporar el bot en tu canal en estos idiomas, por favor escribe a:**_ info _arroba_ collectivat.cat

_**Si conoces personas que tienen dificultad de entender el catalán/castellano, hablan estos idiomas (ver la lista actual de los idiomas incorporados) y que viven en estos barrios (ver la lista actual de los canales de apoyo vecinal), por favor remite la información para que puedan seguir los canales en su propio idioma.**_


---
Para saber más sobre la Economia per la Vida: Fons Cooperatiu ESS, puedes visitar [su página][economiaperlavida] o [su página a Goteo][goteo].

<img src="/img/blog/2020/economiaperlavida.jpg" width="600"/>

[goteo]: https://ca.goteo.org/project/fons-cooperatiu-front-l-emergencia-social-i-sanita
[github]: https://github.com/CollectivaT-dev/suport_mt
[formulari]: https://limesurvey.collectivat.cat/index.php?r=survey/index&sid=383469
[salutcat_ur]: https://t.me/salutcat_ur
[salutcat_ar]: https://t.me/salutcat_ar
[salutcat_zh]: https://t.me/salutcat_zh
[suportgracia_ur]: https://t.me/suportgracia_ur
[suportgracia_ar]: https://t.me/suportgracia_ar
[suportgracia_zh]: https://t.me/suportgracia_zh
[XarxadeSuportVerdum_ar]: https://t.me/XarxadeSuportVerdum_ar
[economiaperlavida]: http://www.economiaperlavida.cat/
