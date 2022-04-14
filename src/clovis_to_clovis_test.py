test_input = '<div class="container toggle-h1" data-hide="h1-1"><p placeholder="Titre" class="title" data-count="I - " contenteditable="false">Some h1</p><div class="toggle-title-container"><i class="material-icons toggle-title"></i></div>'
test_output = '<h1 class="title">Some h1</h1>'

result = clovis_to_clovis(test_input)

assert result == test_output
