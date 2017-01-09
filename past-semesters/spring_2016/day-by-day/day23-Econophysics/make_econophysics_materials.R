library(rmarkdown)

make_class_slides <- function () {
  rmarkdown::render(
    "Econophysics-Slides-And-Notes.Rmd",
    output_format = "ioslides_presentation",
    params = list(is_instructor_notes = FALSE),
    output_file = "INSTRUCTOR_slides.html"
  )
}

make_instructor_notes <- function () {
  rmarkdown::render(
    "Econophysics-Slides-And-Notes.Rmd",
    output_format = "html_document",
    params = list(is_instructor_notes = TRUE),
    output_file = "INSTRUCTOR_notes.html"
  )
}

make_class_slides()
make_instructor_notes()

