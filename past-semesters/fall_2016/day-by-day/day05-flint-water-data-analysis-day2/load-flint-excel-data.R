rm(list = ls())

require('jsonlite')
require('magrittr')
require('readxl')

worksheets_to_extract <-
  excel_sheets('Flint Lead Kits ICP Data.xlsx')[4:12]
column_names_from_spreadsheet <- c(
  "Sample",
  "208Pb",
  "",
  "23Na",
  "25Mg",
  "27Al",
  "28Si",
  "31P",
  "34S",
  "35Cl",
  "39K",
  "43Ca",
  "47Ti",
  "51V",
  "52Cr",
  "54Fe",
  "55Mn",
  "59Co",
  "60Ni",
  "65Cu",
  "66Zn",
  "75As",
  "78Se",
  "88Sr",
  "95Mo",
  "107Ag",
  "111Cd",
  "112Sn",
  "137Ba",
  "238U"
)

flint_data_by_bottle <-
  lapply(
    X = worksheets_to_extract,
    FUN = read_excel,
    path = 'Flint Lead Kits ICP Data.xlsx',
    skip = 3
  ) %>% lapply( # Use the column names from the spreadsheet
    X = .,
    FUN = function(x) {
      colnames(x) <- column_names_from_spreadsheet
      return(x)
    }
  )

