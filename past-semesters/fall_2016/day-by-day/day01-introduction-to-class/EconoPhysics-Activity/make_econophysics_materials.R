library(rmarkdown)
Title <- "Econophysics"


make_class_slides <- function (assignment_title) {
  rmarkdown::render(
    "Econophysics-Slides-And-Notes.Rmd",
    output_format = "ioslides_presentation",
    params = list(is_instructor_notes = FALSE),
    output_file = paste0(
      "SLIDES-"
      , assignment_title
      , ".html"
    )
  )
}

make_instructor_notes <- function (assignment_title) {
  rmarkdown::render(
    "Econophysics-Slides-And-Notes.Rmd",
    output_format = "html_document",
    params = list(is_instructor_notes = TRUE),
    output_file = paste0(
      "NOTES-"
      , assignment_title
      , ".html"
    )
  )
}

make_class_slides(Title)
make_instructor_notes(Title)

