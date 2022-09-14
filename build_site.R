rmarkdown::render('workflow/camels_data_creation/data_dictionary.Rmd')

fs::file_move('workflow/camels_data_creation/data_dictionary.html',
              'docs/data_dictionary.html')

rmarkdown::render('docs/index.Rmd')
