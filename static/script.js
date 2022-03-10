$(document).ready(function () {
  $("#register").prop("disabled", true);

  $(
    "#pregnancies, #glucose, #bloodPressure, #skinThickness, #insulin, #bmi, #pedigree, #age"
  ).keyup(function () {
    if (
      $("#pregnancies").val() != "" &&
      $("#glucose").val() != "" &&
      $("#bloodPressure").val() != "" &&
      $("#skinThickness").val() != "" &&
      $("#insulin").val() != "" &&
      $("#bmi").val() != "" &&
      $("#pedigree").val() != "" &&
      $("#age").val() != ""
    ) {
      $("#register").prop("disabled", false);
    } else {
      $("#register").prop("disabled", true);
    }
  });
});
