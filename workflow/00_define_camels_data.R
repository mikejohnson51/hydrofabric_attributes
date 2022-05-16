library(data.table)
library(archive)
library(dplyr)

base = 'https://ral.ucar.edu/sites/default/files/public/product-tool/camels-catchment-attributes-and-meteorology-for-large-sample-studies-dataset-downloads/camels_attributes_v2.0.zip'
archive_extract(base, 'data')

files = list.files('data/camels_attributes_v2.0', pattern = ".txt", full.names = TRUE)
files = files[!grepl("readme", files)]

camels   = Reduce(function(x, y) merge(x, y, by = "gauge_id", all = TRUE), lapply(files, fread)) |>
  mutate(gauge_id = sprintf("%08d", gauge_id))

frame_subset = camels  = read.csv('https://raw.githubusercontent.com/jmframe/lstm/master/data/camels_basin_list_516.txt', header = FALSE) %>%
    mutate(gauge_id = sprintf("%08d", V1)) %>%
    mutate(V1 = NULL)

camels = dplyr::filter(camels, gauge_id %in% frame_subset$gauge_id)

camels = sf::read_sf('data/gagesIII.gpkg') |>
  select(gauge_id = Gage_no, COMID) |>
  sf::st_drop_geometry() |>
  right_join(camels, by = "gauge_id")


fwrite(camels, 'data/camels_compiled.csv', row.names = FALSE)

unlink("data/__MACOSX", recursive = TRUE)
unlink("data/camels_attributes_v2.0", recursive = TRUE)
