# test for h1
test_input = '<div class="container toggle-h1" data-hide="h1-1"><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div>'
test_output = '<h1 class="title">Some h1</h1>\n'
result = clovis_to_clovis(test_input)

assert result == test_output


# test for h2
test_input = '</div><div class="container toggle-h2 hide-h1-1" data-hide="h2-1" style=""><p placeholder="Sous-titre" class="subtitle" data-count="A) " contenteditable="false">Some h2</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div>'
test_output = '<h2 class="title">Some h2</h2>\n'
result = clovis_to_clovis(test_input)

assert result == test_output



test_input = '''<div id="main-content" class="preview" style="padding-left: 25px;">
<div class="container toggle-h1" data-hide="h1-1"><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h2 hide-h1-1" data-hide="h2-1" style=""><p placeholder="Sous-titre" class="subtitle" data-count="A) " contenteditable="false">Some h2</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h3 hide-h1-1 hide-h2-1" data-hide="h3-1" style=""><p placeholder="Sous-partie" class="subpart" data-count="a) " contenteditable="false">Some h3</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container toggle-h4 hide-h1-1 hide-h2-1 hide-h3-1" data-hide="h4-1" style=""><p placeholder="Titre inférieur" class="subhead" data-count="1) " contenteditable="false">Some h4</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some text<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="hl-yellow">highlighted text</span>, some <b>bold text</b>, some <i>italic text</i>, some <i><b>bold and italic</b></i>, some <span class="hl-yellow"><b>bold and highlighted</b></span>, some <span class="hl-yellow"><i><b>bold, italic highlighted text</b></i></span><i><b></b></i>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><p placeholder="Entrez du texte" class="text" contenteditable="false">Some <span class="f-code">inline code</span>.<br></p></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block danger"><section class="cb-content"><article class="mini-title mt-danger">Attention</article><p placeholder="Avertissement important" contenteditable="false">Some warning<br></p></section></section></div>        <div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1" style=""><section class="colorful-block definition"><section class="cb-content"><article class="mini-title mt-definition">Définition</article><p placeholder="Mot défini" class="definition-title" contenteditable="false">Some word<br></p><p placeholder="Définition" contenteditable="false">Some definition<br></p></section></section></div><div class="container hide-h1-1 hide-h2-1 hide-h3-1 hide-h4-1"><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><div class="block-edit-button-container"></div><section class="colorful-block quote"><section class="cb-content"><section class="quote-container"><article class="quote-content" placeholder="Citation" contenteditable="false">This is a short citation<br></article></section><section class="optional-button-container ob-quote"><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Auteur" contenteditable="false">John Doe<br></article></section><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Source" contenteditable="false">The Book Written by Him<br></article></section><section class="optional-button ob-selected ob-selected-preview"><i class="material-icons optional-icon" style="display: none;">clear</i><article class="optional-text" placeholder="Date" contenteditable="false">1857</article></section></section></section></section></div>                </div>'''

test_output = '''<h1 class="title">Some h1</h1>
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

assert result == test_output