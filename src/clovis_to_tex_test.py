# test for h1
test_input = '<h1 class="title">Some h1 title</h1>'
expected_output = '\\section{Some h1 title}\n\n'
result = clovis_to_tex(test_input)

assert result == expected_output


# test for definition
test_input = '''<div class="cb-container definition">
    <div class="cb-title-container">
        <span class="cb-title-icon"></span>
        <span class="cb-title"></span>
    </div>
    <p class="definition-title">Some word</p>
    <p class="text">Some definition</p>
</div>'''
expected_output = '\\clovisDefinition{Some word}{\n    Some definition\n}\n\n'
result = clovis_to_tex(test_input)

assert result == expected_output


# test for colorful-block danger
test_input = '''<div class="cb-container danger">
    <div class="cb-title-container">
        <span class="cb-title-icon"></span>
        <span class="cb-title"></span>
    </div>
    <p class="text">Some warning</p>
</div>'''
expected_output = '\\clovisDanger{Some warning\\\\\n\n}\n\n'
result = clovis_to_tex(test_input)

assert result == expected_output


# test for katex-code
test_input = '''<div class="katex-container"><p class="katex-code">5x+3</p></div>'''
expected_output = '5x+3\\\\\n\n'
result = clovis_to_tex(test_input)

assert result == expected_output


# test for katex-inline-code
test_input = '<div class="katex-container"><p class="katex-inline-code">Some equation : $5x+3$.<br>A fraction : $ \\dfrac12$, it is a half.</p></div>'
expected_output = 'Some equation : $5x+3$.\\\\A fraction : $ \\dfrac12$, it is a half.\\\\\n\n'
result = clovis_to_tex(test_input)

assert result == expected_output
