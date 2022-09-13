library(data.table)
library(terra)
library(zonal)
library(dataRetrieval)
library(units)
library(foreach)
library(dplyr)

validation_check = function(x, validation, cats, normalize = TRUE){
  x = data.frame(x)

  if(normalize){
    x2 = lapply(1:ncol(x), function(i, w) { weighted.mean(x[,i], w) }, w = cats$area_sqkm)
    x2 = data.frame(x2)
    names(x2) = colnames(x)
    tmp = dplyr::bind_rows(x2, validation[ , colnames(validation) %in% colnames(x)] )

    tmp = bind_rows(tmp, 100 * ((tmp[1,] - tmp[2,]) / tmp[2,]))
    rownames(tmp) = c("ngen", "camels", "percent_error")
  } else {
    tmp = dplyr::bind_rows(x, validation[ , colnames(validation) %in% colnames(x)] )

    rownames(tmp) = c("ngen", "camels")
  }

  tmp
}

ff = function(x){
  cs = cumsum(x)
  cs = cs - cummax((x == 0) * cs)
  c(ifelse(diff(cs) < 0, cs, NA), cs[length(cs)])
}

# Summary Units ----

camels    = readr::read_csv("data/camels_compiled.csv", show_col_types = FALSE)
validation = dplyr::filter(camels, gauge_id == '01142500')

catchment_name = "catchments"
ID = "ID"
years = 2

gpkg      = "/Volumes/Transcend/ngen/CAMELS20/camels_01142500_6083547/spatial/hydrofabric.gpkg"


cats = sf::read_sf(gpkg, catchment_name)


validation = dplyr::filter(camels, gauge_id == '01142500')

# Table 1: Name, Location, and topographic characteristics ----

tab1 = list()
gauge_info = readNWISsite('01142500')
tab1$gauge_id = gauge_info$site_no
tab1$gauge_name = gauge_info$station_nm
tab1$gauge_lat = gauge_info$dec_lat_va
tab1$gauge_lon = gauge_info$dec_long_va
tab1$huc_02 = as.numeric(hyAggregate::find_pu(sf::st_centroid(cats[1,]))$VPUID)
tab1$area_geospa_fabric = sum(as.numeric(set_units(sf::st_area(cats), "km2")))
tab1 = data.frame(tab1)
validation_check(tab1, validation, cats, FALSE)

# DEM
url  = "/vsicurl/https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/TIFF/USGS_Seamless_DEM_13.vrt"
DEM = opendap.catalog::dap(url, AOI = cats)

# m above sealevel; m/km-1
x  = c(DEM, 1000*tan(terrain(DEM, v = "slope", unit = "radians")))

terrain = execute_zonal(x, geom = cats, ID = "ID", drop = "ID", join = FALSE)

names(terrain) = c("elev_mean", "slope_mean")

validation_check(terrain, validation, cats)

tab1 = cbind(tab1, terrain)

# Table 2: Climatic indices ----

.SD <-i <- .data <- NULL


# Load PPT, TAVG, and Snow Thresholds

message("Using ", years, " years of Gridmet Data")

# Daily Accumulated PPT mm
pr = list.files('/Volumes/Transcend/ngen/climate/gridmet/pr',   full.names = TRUE)[1:years]
tm = list.files('/Volumes/Transcend/ngen/climate/gridmet/tavg', full.names = TRUE)[1:years]
et = list.files('/Volumes/Transcend/ngen/climate/gridmet/pet', full.names = TRUE)[2:(years+1)]

gridmet_w = weight_grid(pr[1], cats, ID = ID, progress = FALSE)

suppressWarnings({

  doMC::registerDoMC()

  ppt = foreach(i = 1:length(pr), .combine = "cbind") %dopar% {
    execute_zonal(pr[i], w = gridmet_w, ID = ID, drop = ID)
  }

  tavg = foreach(i = 1:length(tm), .combine = "cbind") %dopar% {
    execute_zonal(tm[i], w = gridmet_w, ID = ID, drop = ID)
  }

  pet = foreach(i = 1:length(et), .combine = "cbind") %dopar% {
    execute_zonal(et[i], w = gridmet_w, ID = ID, drop = ID)
  }
})


ppt  = setnames(ppt,  paste0('day', 1:(ncol(ppt))))
tavg = setnames(tavg, paste0('day', 1:(ncol(tavg))))
pet  = setnames(pet,  paste0('day', 1:(ncol(pet))))

# Snow Fractions
file   = '/Volumes/Transcend/ngen/climate/jennings_snow_threshold.tif'
j      = rast(file)
crs(j) = 'EPSG:4326'

snow_tif = project(x = j, y = rast(tm[1]), method = "near") + 273.15

jen      = execute_zonal(snow_tif, w = gridmet_w, ID = ID)
snow_day = tavg[, .SD  < jen$jennings_snow_threshold]
snow     = ppt * snow_day

highPPT = ppt[, .SD > (5*rowMeans(ppt))]
lowPPT  = ppt[, .SD < 1]

high     <- data.table(t(highPPT))
low      <- data.table(t(lowPPT))
mod_cols <- names(high)

high[ , (mod_cols) := lapply(.SD, ff), .SDcols = mod_cols]
low[  , (mod_cols) := lapply(.SD, ff), .SDcols = mod_cols]

traits = data.frame(p_mean         = rowMeans(ppt),
                    pet_mean       = rowMeans(pet),
                    frac_snow      = rowSums(snow) / rowSums(ppt),
                    high_prec_freq = rowSums(highPPT) / years,
                    low_prec_freq  = rowSums(lowPPT) / years,
                    high_prec_dur  = colMeans(high, na.rm = TRUE),
                    low_prec_dur   = colMeans(low,  na.rm = TRUE)) %>%
  mutate(aridity = pet_mean/ p_mean)

validation_check(traits, validation, cats)


# TODO p_seasonality, high_prec_timing, low_prec_timing


# Table 4: Land Cover Characteristics.
tab4 = list()
# base <- "https://storage.googleapis.com/feddata-r/nlcd/"
# year = 2019
# dataset = 'Land_Cover'
# landmass = 'L48'
# path <- glue::glue("/vsicurl/{base}{year}_{dataset}_{landmass}.tif")
#
#
# path = '/Volumes/Transcend/ngen/climate/MODIS/MCD12Q1.006/mosaics_cog/2019-01-01.tif'
# lc = opendap.catalog::dap(path, AOI = cats)
# lc = execute_zonal(lc, geom = cats, fun = "frac", ID = ID, drop= ID, join = FALSE )
#
#
#
# tab4$frac_forest = rowSums(lc[, grepl("frac_4", names(lc))])
#
# tab4$dom_land_cover_frac = apply(lc,1,max)
# tab4$dom_land_cover      = names(lc)[apply(lc,1,which.max)]
# data.frame(tab4)

path = '/Volumes/Transcend/ngen/climate/MODIS/MCD12Q1.006/mosaics_cog/2019-01-01.tif'
lc = execute_zonal(path, geom = cats, fun = "frac", ID = ID, drop= ID, join = FALSE )


tab4$frac_forest = rowSums(lc[, grepl("1|2|3|4|5", names(lc))])

tab4$dom_land_cover_frac = apply(lc,1,max)
tab4$dom_land_cover      = names(lc)[apply(lc,1,which.max)]
data.frame(tab4)


gvf_files = list.files('/Volumes/Transcend/ngen/climate/MODIS/GVF/summary/cogs',
                 full.names = TRUE, pattern = "tif$")
gvf = rast(grep("diff|max", gvf_files, value = TRUE))
names(gvf) = c("diff", "max")

gvf = execute_zonal(gvf, geom = cats, ID = "ID", drop = ID, fun = "mean", join = FALSE)

lai = list.files('/Volumes/Transcend/ngen/climate/MODIS/LAI/summary/cogs',
                 full.names = TRUE, pattern = "tif$")
lai = rast(grep("diff|max", lai, value = TRUE))
names(lai) = c("diff", "max")

lai = execute_zonal(lai, geom = cats, ID = "ID", fun = "mean", drop = "ID", join = FALSE)

o = cbind(gvf, lai)
names(o) = c("gvf_diff", "gvf_max", "lai_diff", "lai_max")




validation_check(o, validation, cats)


#forest_frac, lai_max, lai_diff, gvf_max, gfv_diff, dom_land_cover, dom_land_cover_frac, root_depth_XX



rast('/Users/mjohnson/Downloads/igbp.bin')
#### Soils!

s = rast(c('/Volumes/Transcend/ngen/climate/sand-1m-percent.tif',
'/Volumes/Transcend/ngen/climate/silt-1m-percent.tif',
'/Volumes/Transcend/ngen/climate/clay-1m-percent.tif',
'/Volumes/Transcend/ngen/climate/GLIM/GLIM_xx.tif',
'/Volumes/Transcend/ngen/climate/permeability_permafrost.tif',
'/Volumes/Transcend/ngen/climate/rockdepm.tif'))

tif = rast('/Volumes/Transcend/ngen/climate/average_soil_and_sedimentary-deposit_thickness.tif')

tmp =  project(tif, s, "bilinear")
names(tmp) = 'soil_depth_pelletier'
s = c(s, tmp )


conus_soil_meta = data.frame(layer = 1:11,
                             thickness = c(5,5,10,10,10,20,20,20,50,50,50)) |>
  dplyr::mutate(cumdepth = cumsum(thickness),
                ratio = thickness/150)

"Then for each STATSGO polygon(?) we comptuted the the average of each soil characteristic
over the top 1.5m (9 LAYERS!) of soil using the following weighted mean

Xp = sum(XiTi/Sdepth) where Xi is the value over the layer, Ti is the thinckness,
and Sdepth is hte cummulative depth"

tmp = rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/sand.tif')[[1:9]]

tmp2 = tmp * conus_soil_meta$ratio[1:9]
tmp3 = sum(tmp2)


type = rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/layertext.tif')[[1:9]]
type2 = modal(type)

o_mask = data.frame(to   = c(0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),
                    from = c(NA,1,1,1,1,1,1,1,1,1,1, 1, 1, NA, 1, 1, 1))

organic_mask = terra::classify(type2, o_mask)


w_br_mask = data.frame(to   = c(0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),
                       from = c(NA,1,1,1,1,1,1,1,1,1,1, 1, 1, 1, NA,NA,1))

water_bedrock_mask = terra::classify(type2, w_br_mask)


w_br_o_mask = data.frame(to   = c(0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),
                         from = c(NA, 1,1,1,1,1,1,1,1,1,1, 1, 1, 1, NA,NA,NA))

water_bedrock_other_mask = terra::classify(type2, w_br_o_mask)


####

sand1 = rast('/Volumes/Transcend/ngen/CONUS_SOIL/TIFFS/sand.tif')[[1:9]]
sand2 = sand1 * conus_soil_meta$ratio[1:9]
sand3 = sum(sand2)

row = zonal::execute_zonal(sand3,
                           geom = cats,
                           fun = "frac",
                           ID = "ID",
                           drop = "ID",
                           join = FALSE)

fncols <- function(data, cname) {
  add <-cname[!cname%in%names(data)]

  if(length(add)!=0) data[add] <- 0

  data
}

df = fncols(row, paste0("frac_", sprintf("%02s", 1:16)))
df <- df[,order(names(df))]


sand = zonal::execute_zonal(tmp3,
                     w = soils_w,
                     ID = "ID",
                     drop = "ID")


terra::rast('/Volumes/Transcend/ngen/climate/sand-1m-percent.tif')

soils_w = zonal::weight_grid(s[[1]], cats, ID = ID, progress = FALSE)

soils = zonal::execute_zonal(s,
                            w = soils_w,
                            ID = "ID",
                            drop = "ID") |>
  dplyr::mutate(clay_frac = .data$`clay-1m-percent` * 100,
         sand_frac = .data$`sand-1m-percent` * 100,
         silt_frac = .data$`silt-1m-percent` * 100,
         rockdepm = .data$rockdepm / 100,
         carbonate_rocks_frac = .data$GLIM_xx/ 100,
         GLIM_xx = NULL,
         soil_conductivity = -0.60 +  (0.0126*.data$sand_frac) - (0.0064*.data$clay_frac),
         soil_conductivity = exp(.data$soil_conductivity),
         geol_porostiy = 50.5 - (0.142*.data$sand_frac)  - (0.037*.data$clay_frac),
         max_water_content = (.data$geol_porostiy/100) * .data$rockdepm)


soils = filter(files, grepl('average_soil_and_sedimentary-deposit_thickness.tif', fullname))$fullname %>%
  zonal::execute_zonal(cats, "ID", join = FALSE) %>%
  setnames(c("ID", "soil_depth_pelletier")) %>%
  left_join(soils, by = "ID")


