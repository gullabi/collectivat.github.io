---
layout: asr_base
ref: asr
lang: en
permalink: asr_en
---
<style>
table {
    width:100%;
}
</style>

# Resource for Speech Technologies

As a part of our mission we provide open data and resources to the public 
concerning speech technologies. You can find a detailed list here with short 
explanations and further references to get more information.
  
<br /> 

| Name                    | Type              | Version | License  | Download |
|-------------------------|-----------        |---------|----------| -------- |
| TV3Parla                | sphinx cont model | v0.3    | AGPL-3.0 | [link]() |
| TV3Parla+ParlamentParla | sphinx cont model | v0.2    | AGPL-3.0 | [link]() |
| TV3Parla Corpus         | audio corpus      | v0.3    | CC-BY-NC 4.0 | [link]() |
| ParlamentParla Corpus   | audio corpus      | v0.2    | CC-BY 4.0 | [link]() |
| OpenSubtitles LM        | language model    | v1.0    | CC-BY 4.0 | [link]() |
| Viquipèdia LM           | language model    | v1.0    | CC-BY 4.0 | [link]() | 
 
<br />
<br />

## CMUSphinx models

[CMUSphinx](https://cmusphinx.github.io/) is a speech recognition toolkit, 
that is the result of over 20 years of research in Carnegie Mellon University. 
Although currently the state-of-the-art is hybrid Hidden Markov Model (HMM) and
Neural Networks (NN) technologies such as Kaldi, `pocketsphinx` tool is still 
the leader in offline decoding for resource limited environments such as 
handheld devices.

Throughout different projects we have gathered data and trained CMUSphinx models with them, you can download the latest models and related files from the following list:

* [TV3Parla (continous) v0.3]()
* [TV3Parla+ParlamentParla v0.2 (continous)]()

## Acoustic corpus

For the two project we finished successfully, we have gathered publicly 
available speech data and converted them into acoustic training corpus for
speech recognition systems. The data sets are available for download with 
varying open licences.

* **TV3Parla**

  This corpus includes 240 hours of Catalan speech from broadcast material. The details of segmentation, data processing and also model training is explained in detail in [Külebi, Öktem; 2018](). The content is owned by Corporació Catalana de Mitjans Audiovisuals, SA (CCMA); we processed their material and hereby making it available under their [terms of use]().

  This project was supported by the [Softcatalà Foundation]().

  * [TV3Parla Corpus]() ([CC BY-NC 4.0][ccbync])  
  <br/>


* **ParlamentParla**

  We have gathered this audio corpus from the recordings and the transcripts of the Catalan Parliament([Parlament de Catalunya](https://www.parlament.cat/)) plenary sessions. We have aligned the transcriptions with the recordings and extracted the cleanest 320 hours for training speech models. The content belongs to the Catalan Parliament and the data is released conforming their [terms of use](https://www.parlament.cat/pcat/serveis-parlament/avis-legal/).

  The ParlamentParla project and the preparation of this page was supported by the Culture Department ([Departament de Cultura](http://cultura.gencat.cat/)) of the Catalan autonomous government.

  * [ParlamentParla Corpus]() ([CC BY 4.0][ccby])  
  <br/>

[ccby]: https://creativecommons.org/licenses/by/4.0/
[ccbync]: https://creativecommons.org/licenses/by-nc/4.0/
<img src="/img/logo_generalitat.png" width="400"/>
