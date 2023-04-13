<!--
-------------------------------------------------------------------------------
This file defines the contents of each slide.
The reveal.js configuration can be found in index.html
-------------------------------------------------------------------------------
-->

<!-- .slide: class="slide-title" data-background-image="../assets/title-slide.svg" data-background-color="#000000" data-background-size="contain" -->

<!-- Place the content at the bottom of the slide -->
<div class="r-stretch">
</div>

<h1 id="talk-title">
  Isostasia, flexura e gravidade
</h1>
<p id="talk-authors">
  <a href="https://www.leouieda.com" id="talk-speaker">Leonardo Uieda</a>
</p>

<!-- Place location and date side-by-side with affiliation logos -->
<div class="row talk-info">
<div class="col-large">


<!-- Permission to reuse and CC-BY license logo -->
<i class="fa fa-camera" style="margin: 0 10px 0 0"></i>
Feel free to screenshot/share/reuse this presentation
<span style="margin: 0 20px"></span>
<a href="https://creativecommons.org/licenses/by/4.0/"><i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by" style="margin: 0 10px 0 2px"></i>CC-BY 4.0 License</a>

</div>
<div class="col-medium">

<!-- Add logos here. Need these wrappers to align them to the bottom right -->
<div class="talk-logos-container">
<div class="talk-logos">
  <a href="https://www.compgeolab.org"><img src="../assets/compgeolab-banner-light.svg" alt="Computer-Oriented Geoscience Lab"></a>
</div>
</div>

</div>
</div>

===============================================================================

# Distúrbio da gravidade $\delta g$

<div class="row">
<div class="col-large">
<img src="../assets/disturbio.png">
</div>
<div class="col">

* <!-- .element: class="fragment" --> Geralmente menor que +- 50 mGal
* <!-- .element: class="fragment" --> Maiores valores associados a ilhas e subducção
* <!-- .element: class="fragment" --> Indica que a maioria da Terra está em <strong>equilíbrio isostático</strong>
* <!-- .element: class="fragment" --> Por quê?

</div>
</div>

===============================================================================

# Equilíbrio isostático

<div class="row">
<div class="col-medium">

* <!-- .element: class="fragment" --> Pressão litoestática na <strong>profundidade de compensação</strong> deve ser constante
* <!-- .element: class="fragment" --> <strong>Modelo de Airy:</strong> topografia/batimetria compensadas por uma raiz/anti-raiz
* <!-- .element: class="fragment" --> Determinar a raiz $r$ a partir da topografia $h$

<div class="fragment text-left">

$ r = \dfrac{\rho_c}{\rho_m - \rho_c} h \qquad $ (continentes)

$ r = \dfrac{\rho_c - \rho_w}{\rho_m - \rho_c} h \qquad  $ (oceanos)

</div>

</div>
<div class="col">
<img src="../assets/airy-concept-names.png">
</div>
</div>

===============================================================================

# Equilíbrio isostático

<div class="row">
<div class="col-medium">

* <strong>Modelo de Pratt:</strong> topografia/batimetria compensadas por mudanças na densidade
* <!-- .element: class="fragment" --> Determinar a densidade $\rho$ a partir da topografia $h$

<div class="fragment text-left">

$ \rho_1 = \rho_c \dfrac{D}{h_1 + D} \qquad $ (continentes)

$ \rho_2 = \dfrac{\rho_c D - \rho_w h_2}{D - h_2}  \qquad  $ (oceanos)

</div>
<div class="fragment text-left">

**🧘 Tarefa:** Deduza as equações acima aplicando os mesmos princípios
utilizados para o modelo de Airy.

</div>

</div>
<div class="col">
<img src="../assets/pratt-concept-names.png">
</div>
</div>

===============================================================================

# Distúrbio da gravidade no modelo Airy

Efeitos presentes no distúrbio:
<br>
topografia $h$, raiz $r$ e heterogeneidades (ignoradas)

<div class="fragment">

Utilizando a equação do platô de Bouguer ($g \approx 2 \pi G \rho h$):

</div>

<div class="fragment">

$$
g_h = 2 \pi G \rho_c h
$$

</div>
<div class="fragment">

$$
g_r = 2 \pi G (\rho_c - \rho_m) r = - 2 \pi G \rho_c h
$$

</div>
<div class="fragment">

**Efeitos da raiz e topografia se anulam**

</div>
<div class="fragment">

**🧘 Tarefa:** Mostre que o mesmo se aplica aos oceanos e ao modelo de Pratt

</div>

===============================================================================

# Anomalia Bouguer no modelo Airy

Efeito da topografia foi removido

Sobra somente a raiz

<div class="fragment">

$$
\delta g_{bg} = - 2 \pi G \rho_c h
$$

</div>
<div class="fragment">

**A anomalia Bouguer tem uma relação linear com a topografia**

</div>
<div class="fragment">

Gráficos de anomalia Bouguer X topografia relevam equilíbrio isostático

</div>
<div class="fragment">

**🧘 Tarefa:** Mostre que o mesmo se aplica aos oceanos e ao modelo de Pratt

</div>

===============================================================================

# Flexura e ilhas oceânicas

<div class="row">
<div class="col-large">
<img src="../assets/disturbio.png">
</div>
<div class="col">

* <!-- .element: class="fragment" --> Distúrbio grande <br>(> 100 mGal)
* <!-- .element: class="fragment" --> Não compensadas por Airy ou Pratt
* <!-- .element: class="fragment" --> <strong>Como as ilhas são sustentadas?</strong>
* <!-- .element: class="fragment" --> Pela rigidez da placa oceânica

</div>
</div>

===============================================================================

# Flexura da placa oceânica

<img src="../assets/flexure-seamount-load.png">

===============================================================================

# Equação da flexura

$$
D \left( \dfrac{\partial^4}{\partial x^4} + 2\dfrac{\partial^4}{\partial x^2 \partial y^2} + \dfrac{\partial^4}{\partial y^4} \right)
w + g (\rho_m - \rho_w) w = -g(\rho_c - \rho_w) t_0
$$

<div class="fragment">

A carga $t_0$ é a diferença entre a topografia e a flexura $t_0 = t - w$

</div>
<div class="fragment">

$$
D \left( \dfrac{\partial^4}{\partial x^4} + 2\dfrac{\partial^4}{\partial x^2 \partial y^2} + \dfrac{\partial^4}{\partial y^4} \right)
w + g (\rho_m - \rho_w) w = -g(\rho_c - \rho_w) (t - w)
$$

</div>
<div class="fragment">

Aplicando a Transformada de Fourier dos dois lados da equação

</div>
<div class="fragment">

$$
W(k_x, k_y) = \dfrac{-(\rho_c - \rho_w)}{(\rho_m - \rho_c)}\left[1 + \dfrac{D(2\pi k)^4}{g(\rho_m - \rho_c)}\right]^{-1} T(k_x, k_y)
$$

</div>

===============================================================================

# Distúrbio da gravidade causada pela flexura

<img src="../assets/disturbance-flexure-model.png">

===============================================================================

# Efeito gravitacional de uma interface

$$
g (k_x, k_y) = 2 \pi G \rho\ e^{-2 \pi k s}\ T(k_x, k_y)
$$

<div class="fragment">

Aplicando ao modelo conceitual do distúrbio causado pela flexura

</div>
<div class="fragment">

$$
\delta g (k_x, k_y) = 2 \pi G (\rho_c - \rho_w) e^{-2 \pi k s}\ T(k_x, k_y) +
2 \pi G (\rho_m - \rho_c) e^{-2 \pi k (s + d)}\ W(k_x, k_y)
$$

</div>
<div class="fragment">

Substituindo $W$ pela equação da flexura

</div>
<div class="fragment">

$$
\delta g (k_x, k_y) = 2 \pi G (\rho_c - \rho_w) e^{-2\pi k s} \left\( 1 -  \left[1 + \dfrac{D(2\pi k)^4}{g(\rho_m - \rho_c)}\right]^{-1}e^{-2\pi k d} \right\) \ T(k_x, k_y)
$$

</div>
<div class="fragment">

Calcular $\phi(k_x, k_y)  = \delta g (k_x, k_y) / T (k_x, k_y)$ para dados
observados
<br>
**proporciona informações sobre o filtro $\phi$ e a rigidez $D$**

</div>

===============================================================================

# 💻 Prática

<div class="large">

1. <!-- .element: class="fragment" --> Dados de gravidade e topografia
1. <!-- .element: class="fragment" --> Verificar se Bouguer X topografia é linear
1. <!-- .element: class="fragment" --> Calcular a flexura causada por ilhas
1. <!-- .element: class="fragment" --> Verificar a relação distúrbio X topografia no domínio da frequência

</div>

===============================================================================

# Bibliografia

Braitenberg (2015). https://doi.org/10.1016/j.jag.2014.01.013

Fowler (1990). The solid earth: an introduction to global geophysics.

Sandwell (2022). Advanced Geodynamics.

===============================================================================

<!-- .slide: class="slide-contact" data-background-image="../assets/contact-slide.svg" data-background-size="contain" data-background-color="#000000" -->

<div class="r-stretch centered">
<div>

<i class="fas fa-comments"></i>
<br>
Contato:
<a href="https://www.leouieda.com">www.leouieda.com</a>

<i class="fab fa-github"></i>
<br>
Código fonte desta apresentação:
<br>
[github.com/leouieda/aula2023](https://github.com/leouieda/aula2023)

<i class="fab fa-creative-commons"></i><i class="fab fa-creative-commons-by"></i>
<br>
Unless otherwise noted,
the contents of this presentation are
licensed under the
<br>
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

</div>
</div>
<div class="footnote-left dark">

A imagem de fundo mostra a região Oeste de São Paulo.
Dados são provenientes do satélite Landsat 9.
A imagem foi produzida com o software
[xlandsat](https://www.compgeolab.org/xlandsat/).

</div>
