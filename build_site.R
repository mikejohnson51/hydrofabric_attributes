pacman::p_load(rmarkdown, fs)

render('workflow/camels_data_creation/data_dictionary.Rmd')

file_move('workflow/camels_data_creation/data_dictionary.html',
          'docs/data_dictionary.html')

render('docs/index.Rmd')

