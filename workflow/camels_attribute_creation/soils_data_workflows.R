###
# Build Soil Layers for CAMELS
# Mike Johnson
###

#-- Meta Data
## Note: The Camels workflow only operates on the

conus_soil_meta = data.frame(layer = 1:11,
                             thickness = c(5,5,10,10,10,20,20,20,50,50,50)) |>
  dplyr::mutate(cumdepth = cumsum(thickness)) |>
  dplyr::filter(cumdepth <= 150)   |>
  dplyr::mutate(ratio = thickness / max(cumdepth))

#-- Masks
## Note: The Camels workflow relies on three domaninate catgory masks

dominant_category = rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/layertext.tif')[[1:max(conus_soil_meta$layer)]]
dominant_category = modal(dominant_category)

o_mask = data.frame(to   = c(0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),
                    from = c(NA,1,1,1,1,1,1,1,1,1,1, 1, 1, NA, 1, 1, 1))

organic_mask = terra::classify(dominant_category, o_mask)


w_br_mask = data.frame(to   = c(0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),
                       from = c(NA,1,1,1,1,1,1,1,1,1,1, 1, 1, 1, NA,NA,1))

water_bedrock_mask = terra::classify(dominant_category, w_br_mask)

w_br_o_mask = data.frame(to   = c(0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),
                         from = c(NA, 1,1,1,1,1,1,1,1,1,1, 1, 1, 1, NA,NA,NA))

water_bedrock_other_mask = terra::classify(dominant_category, w_br_o_mask)

w_br_o_o_mask = data.frame(to   = c(0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),
                         from = c(NA, 1,1,1,1,1,1,1,1,1,1, 1, 1, NA, NA,NA,NA))

water_bedrock_other_organic_mask = terra::classify(dominant_category, w_br_o_o_mask)
plot(water_bedrock_other_organic_mask)

# Data

## Fracs!
### Camels computes the fraction of water (cat 14), organic matter (cat 13), and other (cat 16)

type_fracs = zonal::execute_zonal(dominant_category, geom = cats, fun = "frac", ID = "ID", drop = "ID", join = FALSE)

fncols <- function(data, cname) {
  add <-cname[!cname%in%names(data)]

  if(length(add)!=0) data[add] <- 0

  data
}

type_fracs = fncols(type_fracs, paste0("frac_", 1:16))


type_fracs = type_fracs[, grepl(c("13|14|16"), names(type_fracs))]
names(type_fracs) = c("organic_frac", "water_frac", "other_frac")


## Sand, Silt Clay

"Then for each STATSGO polygon(?) we comptuted the the average of each soil characteristic
over the top 1.5m (9 LAYERS!) of soil using the following weighted mean

Xp = sum(Xi *(Ti/Sdepth)) where Xi is the value over the layer, Ti is the thinckness,
and Sdepth is hte cummulative depth"

reduce_conus_soil = function(path, mask, conus_soil_meta){
  tmp = rast(path)[[1:max(conus_soil_meta$layer)]]
  tmp1 = tmp * mask
  tmp2 = tmp1 * conus_soil_meta$ratio
  tmp3 = sum(tmp2)
  tmp3
}

sand = reduce_conus_soil('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/sand.tif',
                         water_bedrock_other_organic_mask,
                         conus_soil_meta)

silt = reduce_conus_soil('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/silt.tif',
                         water_bedrock_other_organic_mask,
                         conus_soil_meta)

clay = reduce_conus_soil('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/clay.tif',
                         water_bedrock_other_organic_mask,
                         conus_soil_meta)

depth_cm  = rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/rockdepm.tif')
depth_m   = depth_cm * water_bedrock_mask
depth_m[] = pmin(150, values(depth_cm)) / 100

pelletier = rast('/Volumes/Transcend/ngen/climate/average_soil_and_sedimentary-deposit_thickness.tif')
pelletier = project(pelletier, clay[[1]], "bilinear")
soil_depth_pelletier   = pelletier
soil_depth_pelletier[] = pmin(50, values(pelletier))


# soil porosity

sand_layers = .142 * (rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/sand.tif')[[1:max(conus_soil_meta$layer)]])
clay_layers = .037 * (rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/clay.tif')[[1:max(conus_soil_meta$layer)]])
porosity = 50.5 - sand_layers - clay_layers

porosity[is.na(organic_mask)] = .9
porosity = porosity * water_bedrock_other_mask
porosity = porosity * conus_soil_meta$ratio
porosity = sum(porosity) / 100

# soil_conductivity

sand_layers = .0126 * (rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/sand.tif')[[1:max(conus_soil_meta$layer)]])
clay_layers = .0064 * (rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/clay.tif')[[1:max(conus_soil_meta$layer)]])
conductivity = -0.60 + sand_layers - clay_layers
conductivity = exp(conductivity)


conductivity[is.na(organic_mask)] = 36
conductivity = conductivity * water_bedrock_other_mask
conductivity = conductivity * conus_soil_meta$ratio
conductivity = sum(conductivity)

out = zonal::execute_zonal(c(sand, silt, clay, depth_m, soil_depth_pelletier, conductivity, porosity),
                     w = soils_w,
                     ID = "ID",
                     drop = "ID",
                     join = FALSE)

names(out) = c("sand_frac", "silt_frac", "clay_frac",
               "soil_depth_statsgo", "soil_depth_pelletier",
               "soil_conductivity", "soil_porosity")

out$max_water_content = out$soil_depth_statsgo *out$soil_porosity



### GLiM

wkt = st_bbox(cats)
sf::st_layers('/Volumes/Transcend/ngen/climate/GLIM/LiMW_GIS 2015.gdb')


rast('/Volumes/Transcend/ngen/climate/GLIM/GLIM_xx.tif')
test = sf::read_sf('/Volumes/Transcend/ngen/climate/GLIM/LiMW_GIS 2015.gdb')

test$fac = as.factor(test$xx)

r = raster::raster('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/sand.tif')[[1]]
test = sf::st_transform(test, sf::st_crs(r))
fglim = fasterize::fasterize(test, r, field = "fac")

plot(fglim)

class = data.frame(
  int = paste0("frac_", 1:16),
  class = levels(test$fac),
  description = c('Evaporites',
                  'Ice and Glaciers',
                  'Metamorphics',
                  'No Data',
                  'Acid plutonic rocks',
                  'Basic plutonic rocks',
                  'Intermediate plutonic rocks',
                  'Pyroclastics',
                  'Carbonate sedimentary rocks',
                  'Mixed sedimentary rocks',
                  'Siliciclastic sedimentary rocks',
                  'Unconsolidated sediments',
                  'Acid volcanic rocks',
                  'Basic volcanic rocks',
                  'Intermediate volcanic rocks',
                  'Water Bodies'))


out = zonal::execute_zonal('/Volumes/Transcend/ngen/climate/GLIM/GLIM_xx.tif',
                     cats, ID = "ID", join = FALSE, fun = "frac")

library(tidyr)

tmp = out %>%
  gather(class, class_frac, -ID) %>%
  group_by(ID) %>%
  # now we select the TOP 2
  slice_max(class_frac, n = 2, with_ties = FALSE) %>%
  # now we add the colors
  ungroup() %>%
  mutate(name = rep(c("geol_1st", "geol_2nd"), times = nrow(cats))) |>
  pivot_wider(ID, names_from = name,
              names_glue = "{name}_{.value}",
              values_from = c(class, class_frac))


tmp$geol_1st_class = class$description[match(tmp$geol_1st_class, class$int)]
tmp$geol_2nd_class = class$description[match(tmp$geol_2nd_class, class$int)]
tmp = tmp[match(cats$ID, tmp$ID),]
tmp$ID = NULL

## GLYMPHS

fin = cbind(out, type_fracs, tmp)

g = sf::read_sf('/Volumes/Transcend/ngen/GLHYMPS/GLHYMPS.gdb')

names(g)
