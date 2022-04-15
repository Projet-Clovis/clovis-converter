# test for h1
test_input = '<h1 class="title">Some h1 title</h1>'
test_output = '\\section{Some h1 title}\n\n'
result = clovis_to_tex(test_input)

assert result == test_output


# test for definition
test_input = '''<div class="cb-container definition">
    <div class="cb-title-container">
        <span class="cb-title-icon"></span>
        <span class="cb-title"></span>
    </div>
    <p class="definition-title">Some word</p>
    <p class="text">Some definition</p>
</div>'''
test_output = '\\clovisDefinition{Some word}{\n    Some definition\n}\n\n'
result = clovis_to_tex(test_input)

assert result == test_output


# test for colorful-block danger
test_input = '''<div class="cb-container danger">
    <div class="cb-title-container">
        <span class="cb-title-icon"></span>
        <span class="cb-title"></span>
    </div>
    <p class="text">Some warning</p>
</div>'''
test_output = '\\clovisDefinition{Some word}{\n    Some definition\n}\n\n'
result = clovis_to_tex(test_input)

assert result == test_output
