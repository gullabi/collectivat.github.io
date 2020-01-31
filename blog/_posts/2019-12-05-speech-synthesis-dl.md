---
layout: post
title: "Free and open speech synthesis for Catalan"
ref: sp_release
image: /img/blog/2019/catotron_bg.png
thumbnail: /img/blog/2019/catotron_sm.png
lang: en
summary: Thanks to a project supported by the Department of Culture of the Catalan government, we trained a text-to-speech system in Catalan with neural networks, and published them with an open license. Here we want to present our results, our experience and further details concerning the integration of this technology. 
---

Here you can find all the information related to Catotron, the open and free
text-to-speech system in Catalan that has been trained with neural networks.
The open source code is available in github [here][catotron] and [here][catotron-cpu]
and the models can be downloaded here.

* Female voice: Ona [[download]][ona]
* Male voice: Pau [[download]][pau]
* El vocoder Waveglow: [[download]][waveglow_model]
* El vocoder MelGAN: [[download]][melgan_model]

You can try the Ona voice via our [demo page][demo].

### Summary:

Thanks to the application of deep learning methods, text-to-speech systems
(TTS) have advanced considerably in the recent years. The most important change has
been the introduction of the vocoders (voice encoders) that are trained by neural
networks. The first example of such technology was Wavenet, which was published
in 2016 and developed by DeepMind, one of the companies owned by Google.

Currently, these vocoders that are being used in the TTS architectures such as
Tacotron and Tacotron2 are trained by neural networks. Various implementations 
of these technologies can be found as open source. These technologies represent
the state-of-the-art in TTS technologies and can produce the best possible results 
with respect to the intelligibility and the naturalness of synthesized speech.

Unfortunately, in order to train these systems, it is absolutely necessary to have 
access to resources such as data and computational power. That is why there is no
published model with open licenses for languages other than English. Thanks to a
project funded by the Ministry of Culture of the Catalan Government (Departament
de Cultura), we trained the TTS models in Catalan with neural networks and published
them with open licenses. We want to present here the results, our experience and the
details of how to integrate this technology.

### The code:

For building Catatron we used are the repositories [Tacotron2][nvidia]
and [Waveglow][waveglow] of the company NVIDIA and are published with
open-source licences in github. One of the most important results of the
project is the code itself, namely our fork of [Tacotron2][catotron]. It has been
modified for the Catalan language and it is indispensable for using the 
Catalan models.

<br/>

Here we present some example recordings. The chosen phrases belong to the
validation data set and therefore were not used for the training of
Catotron models.

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

We also made experiments with the ParlamentParla data set and created a model
of Artur Mas, who was the person with most recorded hours in
the data set. We took advantage of this test in making an estimation
of the quantity of data that is needed for training a model. Due to privacy
concerns, we do not publish this model, but we present some inference examples. The
phrases belong to the recordings used for the validation and were therefore not
used for the training of the model.

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

Different phrases that are being read by all the model voices:

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

### How can it be used:
Non-developers can only synthesize speech via the [Google Colaboratory][colab1] interface for now.
With this online ipython notebook, the Google GPUs can be used
free of charge. In a few weeks, we will publish a demo web page in which visitors can
synthesise short sentences.

How to train new voices: It is already possible to adapt the currently published models
to synthesize any voice. It can be done with
the help of transfer learning and using the published models and recordings of
the new speaker. Our example of [catotron-transfer-learning.ipynb][colab2] gives a
step-by-step guide on how to do it. In this specific guide, the model of Ona is
adapted to the voice of Pau, with the use of computing resources
of Google.

### Contributions:
* Baybars Külebi (Col·lectivaT)
* Santiago Pascual (Universitat Politècnica de Catalunya)
* Alex Peiro Lilja (Universitat Pompeu Fabra)
* Alp Öktem (Col·lectivaT)

---
These resources have been developed thanks to the project «síntesi de la
parla contra la bretxa digital» (Speech synthesis against the digital gap)
that was subsidised by the Department of Culture. A part of the funding 
comes from the financing administered by the inheritance board of the 
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
[waveglow_model]: https://drive.google.com/open?id=1WsibBTsuRg_SF2Z6L6NFRTT-NjEy1oTx
[melgan_model]: https://drive.google.com/file/d/1U3LeuaMIVoRvMvfwlHjsRJPWhgTzeIBh
[demo]: http://catotron.collectivat.cat/
