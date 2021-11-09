---
layout: asr_base
ref: asr
lang: en
permalink: asr
---
<style>
table {
    width:100%;
}
</style>

# Resources for Speech Technologies

As a part of our mission, we provide open data and resources on speech technologies, specifically automatic speech recognition (ASR) and text-to-speech synthesis (TTS) in Catalan. You can find a detailed list here with short explanations and further references to get more information. 
  
| Name                                    | Language | Type           | License       | Download     |
|---------------------------------------  | -------- | -----------    | --------      | ------------ |
| [TV3Parla][2]                      v0.3 | Catalan  | acoustic model | GNU AGPL-3.0  | [link][M0.3] |
| [TV3Parla+ParlamentParla][2]       v0.2 | Catalan  | acoustic model | GNU AGPL-3.0  | [link][M0.4] |
| [TV3Parla Corpus][4]               v0.3 | Catalan  | audio corpus   | CC-BY-NC 4.0  | [link][Ctv3] |
| [ParlamentParla Corpus][3]         v2.0 | Catalan  | audio corpus   |  CC-BY 4.0    | [link][Cp2.0]|
| [ParlamentParla Corpus - clean][3] v1.0 | Catalan  | audio corpus   |  CC-BY 4.0    | [link][CpC]  |
| [ParlamentParla Corpus - other][3] v1.0 | Catalan  | audio corpus   |  CC-BY 4.0    | [link][CpO]  |
| [ParlamentParla Corpus - old][3]   v0.3 | Catalan  | audio corpus   |  CC-BY 4.0    | [link][Cp0.3]|
| [Catotron - Ona][6]                     | Catalan  | TTS model      | CC-BY 4.0     | [link][TTSOnaModel] |
| [Catotron - Pau][6]                     | Catalan  | TTS model      | CC-BY 4.0     | [link][TTSPauModel] |
| [UPC FestCat Ona - optimized][5]        | Catalan  | TTS audio corpus |  CC BY-SA 3.0 ES   | [link][TTSOna]|
| [UPC FestCat Pau - optimized][5]        | Catalan  | TTS audio corpus |  CC BY-SA 3.0 ES   | [link][TTSPau]|
| OpenSubtitles LM                   v1.0 | Catalan  | language model |  CC-BY 4.0    | [link][LMos] |
 
<br/>

## Acoustic corpora

During various projects, we have gathered publicly available speech data and converted them into acoustic training corpora. These data sets are available for download with varying open licenses.

### TV3Parla

This corpus includes 240 hours of Catalan speech from broadcast material. The details of segmentation, data processing and also model training are explained in [Külebi, Öktem; 2018](https://www.isca-speech.org/archive/iberspeech_2018/kulebi18_iberspeech.html). The content is owned by Corporació Catalana de Mitjans Audiovisuals, SA (CCMA); we processed their material and hereby making it available under their [terms of use](http://www.ccma.cat/avis-legal/condicions-utilitzacio-del-portal/).

The corpus can be reached [here][Ctv3] under a [CC BY-NC 4.0][ccbync] license.  

*This project was supported by the [Softcatalà Association](https://www.softcatala.org/).*

### ParlamentParla

We have gathered this audio corpus from the recordings and the transcripts of the Catalan Parliament ([Parlament de Catalunya](https://www.parlament.cat/)) plenary sessions, which took place between 2007 and 2018. We aligned the transcriptions with their respective recordings and segmented them optimal for ASR development. The content belongs to the Catalan Parliament and the data is released conforming [their terms of use](https://www.parlament.cat/pcat/serveis-parlament/avis-legal/).

The [version 0.3 corpus][Cp0.3] includes per-intervention full text aligned with audio links.

As of version 1.0, the corpus can be reached in two parts; 90 hours of [clean][CpC] and 230 hours of [other][CpO] quality segments. 

As of [version 2.0][Cp2.0], the corpus is extended and separated into 211 hours of clean and 400 hours of other quality segments. Furthermore, each speech segment is tagged with its speaker and each speaker with their gender.

*Preparation of this corpus was partly supported by the [Department of Culture of the Catalan autonomous government](http://cultura.gencat.cat/), and the v2.0 was supported by the Barcelona Supercomputing Center, within the framework of the project [AINA](http://aina.gencat.cat/) of the [Department of Digital Policies](https://politiquesdigitals.gencat.cat/).*

### UPC FestCat TTS Corpora

[FestCat corpus](http://festcat.talp.cat/en/) was developed by TALP Research Center, Polytechnic University of Barcelona in 2007 for building open source TTS systems for Catalan. We reprocessed this corpus by optimizing it to build our neural-network based TTS [Catotron][catotron]. Long segments were split or either discarded to have a maximum audio length of 12 seconds. The male voice corpus [Pau][TTSPau] contains 6 hours 54 minutes and female voice corpus [Ona][TTSOna] contains 6 hours 12 minutes. Both of them are released with [Attribution-ShareAlike 3.0 Spain (CC BY-SA 3.0 ES) license][ccsaes]. 

*Preparation of this corpus was supported by the [Department of Culture of the Catalan autonomous government](http://cultura.gencat.cat/)*

## ASR models

These are the ASR models that we trained with [CMUSphinx](https://cmusphinx.github.io/) speech recognition toolkit, using the aforementioned corpora. We continue our work on maintaining and bettering the models in our [repository](https://github.com/collectivat/cmusphinx-models). You can find installation and configuration guides, including tutorials on basic use-cases in the [wiki][wiki].

* [TV3Parla v0.3][M0.3]: `sphinxtrain` 5pre-alpha continuous model
* [TV3Parla+ParlamentParla v0.2][M0.4]: `sphinxtrain` 5pre-alpha continuous model

## TTS models

[Catotron][catotron] is the first free, open speech synthesis system based on neural networks. Col·lectivaT has lead the development with funding from [Department of Culture of the Catalan autonomous government](http://cultura.gencat.cat/) with the participation of researchers from [Natural Language Processing research group (TALN)][taln] of Pompeu Fabra University and [Language and Speech Technologies and Applications Center of Polytechnic University of Catalonia (UPC-TALP)][talp].

- [Official page][catotron]
- [Project blog](/blog/2019-12-05-speech-synthesis-dl/) with links to models (Ona, Pau, Waveglow, MelGAN) and samples
- [Source code for GPU](http://github.com/CollectivaT-dev/catotron) and [CPU](http://github.com/CollectivaT-dev/catotron-cpu)
- [Jupyter notebooks](http://github.com/CollectivaT-dev/TallersParla) for inference and speaker adaptation

For more information, you can refer to [our paper published in Interspeech 2020][interspeech2020].

  <br/>  
  <br/> 

*The preparation of this page was supported by the [Culture Department](http://cultura.gencat.cat/) of the Catalan autonomous government.*

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
[1]: #acoustic-corpora
[2]: #asr-models
[3]: #parlamentparla
[4]: #tv3parla
[5]: #upc-festcat-tts-corpora
[6]: #tts-models

