var allInputs = document.getElementsByTagName("input");
var allInputs = Array.prototype.slice.call(allInputs, 0);

allInputs.forEach((element) => {
  element.setAttribute("data-lpignore", true);
});
