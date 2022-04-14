# test h1
test_input = '<h1 class="title">Some h1 title</h1>'
test_output = '\\section{Some h1 title}\n\n'
result = clovis_to_tex(test_input)

assert result == test_output
