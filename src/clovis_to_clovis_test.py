# test for h1
test_input = '<div class="container toggle-h1" data-hide="h1-1"><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div>'
expected_output = '<h1 class="title">Some h1</h1>\n'
result = clovis_to_clovis(test_input)

assert result == expected_output


# test for h2
test_input = '</div><div class="container toggle-h2 hide-h1-1" data-hide="h2-1" style=""><p placeholder="Sous-titre" class="subtitle" data-count="A) " contenteditable="false">Some h2</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div>'
expected_output = '<h2 class="title">Some h2</h2>\n'
result = clovis_to_clovis(test_input)

assert result == expected_output



test_input = '''<div id="main-content" class="preview" style="padding-left: 25px;">
<div class="container toggle-h1" data-hide="h1-1"><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h2 hide-h1-1" data-hide="h2-1" style=""><p placeholder="Sous-titre" class="subtitle" data-count="A) " contenteditable="false">Some h2</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h3 hide-h1-1 hide-h2-1" data-hide="h3-1" style=""><p placeholder="Sous-partie" class="subpart" data-count="a) " contenteditable="false">Some h3</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h4 hide-h1-1 hide-h2-1 hide-h3-1" data-hide="h4-1" style=""><p placeholder="Titre inférieur" class="subhead" data-count="1) " contenteditable="false">Some h4</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some text<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="hl-yellow">highlighted text</span>, some <b>bold text</b>, some <i>italic text</i>, some <i><b>bold and italic</b></i>, some <span class="hl-yellow"><b>bold and highlighted</b></span>, some <span class="hl-yellow"><i><b>bold, italic highlighted text</b></i></span><i><b></b></i>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="f-code">inline code</span>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block danger"><section class="cb-content"><article class="mini-title mt-danger">Attention</article><p placeholder="Avertissement important" contenteditable="false">Some warning<br></p></section></section></div>        <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block definition"><section class="cb-content"><article class="mini-title mt-definition">Définition</article><p placeholder="Mot défini" class="definition-title" contenteditable="false">Some word<br></p><p placeholder="Définition" contenteditable="false">Some definition<br></p></section></section></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1"><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><section class="colorful-block quote"><section class="cb-content"><section class="quote-container"><article class="quote-content" placeholder="Citation" contenteditable="false">This is a short citation<br></article></section><section class="optional-button-container ob-quote"><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Auteur" contenteditable="false">John Doe<br></article></section><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Source" contenteditable="false">The Book Written by Him<br></article></section><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Date" contenteditable="false">1857</article></section></section></section></section></div>                </div>'''

expected_output = '''<h1 class="title">Some h1</h1>
<h2 class="title">Some h2</h2>
<h3 class="title">Some h3</h3>
<h4 class="title">Some h4</h4>
<p class="text">Some text</p>
<p class="text">Some <span class="hl-yellow">highlighted text</span>, some <b>bold text</b>, some <i>italic text</i>, some <i><b>bold and italic</b></i>, some <span class="hl-yellow"><b>bold and highlighted</b></span>, some <span class="hl-yellow"><i><b>bold, italic highlighted text</b></i></span>.</p>
<p class="text">Some <span class="f-code">inline code</span>.</p>
<div class="cb-container danger">
        <div class="cb-title-container">
            <span class="cb-title-icon"></span>
            <span class="cb-title"></span>
        </div>
    <p class="text">Some warning</p>
<div class="cb-container definition">
        <div class="cb-title-container">
            <span class="cb-title-icon"></span>
            <span class="cb-title"></span>
        </div>
    <p class="definition-title">Some word</p>
<p class="text">Some definition</p>
<div class="quote-container"><p class="quote-content">This is a short citation</p>
<p class="quote-author">John Doe</p>
<p class="quote-source">The Book Written by Him</p><p class="quote-date">1857</p>
</div>
'''

result = clovis_to_clovis(test_input)

#assert result == expected_output



test_input = '''<div class="container toggle-h1" data-hide="h1-1"><div class="code-container"><div placeholder="Entrez ou copiez du code ici" class="code-code" style="display: none;" contenteditable="false">// nom de classe = nom du fichier<br>class HelloWorld {<br>    &nbsp;&nbsp;&nbsp; public static void main(String[] args) {<br>        &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; System.out.println("Hello world");<br>    &nbsp;&nbsp;&nbsp; }<br>}</div><div class="code-render hljs cs" light="true" language="cs"><div class="code-line"><span class="hljs-comment">// nom de classe = nom du fichier</span></div><div class="code-line"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloWorld</span> {</div><div class="code-line">    &nbsp;&nbsp;&nbsp; <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span>(<span class="hljs-params">String[] args</span>)</span> {</div><div class="code-line">        &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; System.<span class="hljs-keyword">out</span>.println(<span class="hljs-string">"Hello world"</span>);</div><div class="code-line">    &nbsp;&nbsp;&nbsp; }</div><div class="code-line">}</div><div class="code-button-container"><div class="code-button code-size"><div class="code-button-icon"><i class="material-icons">format_size</i></div><div>taille</div></div><div class="code-button code-theme"><div class="code-button-icon"><i class="material-icons"></i></div><div>thème</div></div><div class="code-button code-copy"><div class="code-button-icon"><i class="material-icons">content_copy</i></div><div>copier</div></div></div></div></div></div>'''

expected_output = '''
'''

result = clovis_to_clovis(test_input)

#assert result == expected_output



test_input = '''<div class="container hide-h1-1"><div class="block-edit-button-container"></div><div class="katex-container"><p placeholder="Rédigez du LaTeX ici" class="katex-code" contenteditable="false">5x+3</p><p class="katex-render"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">5x+3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="mord">5</span><span class="mord mathdefault">x</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span></span></span></span></p></div></div>'''

expected_output = '''<div class="katex-container"><p class="katex-code">5x+3</p></div>
'''

result = clovis_to_clovis(test_input)

assert result == expected_output



test_input = '''<div class="container hide-h1-1"><div class="block-edit-button-container"></div><div class="katex-inline-container"><p placeholder="Rédigez du texte ici, et entrez du Latex entre les séparateurs $ ou $$." class="katex-inline-code" contenteditable="false">Some equation : $5x+3$.<br>A fraction : $ \dfrac12$, it is a half.<br></p><p class="katex-inline-render">Some equation : <span><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>5</mn><mi>x</mi><mo>+</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">5x+3</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.72777em; vertical-align: -0.08333em;"></span><span class="mord">5</span><span class="mord mathdefault">x</span><span class="mspace" style="margin-right: 0.222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right: 0.222222em;"></span></span><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">3</span></span></span></span></span>.<br>A fraction : <span><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mn>1</mn><mn>2</mn></mfrac></mrow><annotation encoding="application/x-tex"> \dfrac12</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 2.00744em; vertical-align: -0.686em;"></span><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height: 1.32144em;"><span class="" style="top: -2.314em;"><span class="pstrut" style="height: 3em;"></span><span class="mord">2</span></span><span class="" style="top: -3.23em;"><span class="pstrut" style="height: 3em;"></span><span class="frac-line" style="border-bottom-width: 0.04em;"></span></span><span class="" style="top: -3.677em;"><span class="pstrut" style="height: 3em;"></span><span class="mord">1</span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height: 0.686em;"><span class=""></span></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span></span>, it is a half.<br></p></div></div>'''

expected_output = '''<div class="katex-container"><p class="katex-inline-code">Some equation : $5x+3$.<br>A fraction : $ \\dfrac12$, it is a half.</p></div>
'''

result = clovis_to_clovis(test_input)

assert result == expected_output