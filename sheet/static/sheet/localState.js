function storeItem(key, name) {
  // Change to true to enable logging
  logging = false;
  storageKey = name + "-" + key;
  element = document.getElementById(key);
  value = null;
  if (element.type == "checkbox") {
    value = element.checked;
  } else {
    value = element.value;
  }
  if (logging) {
    console.log("Storing " + storageKey + " as " + value);
  }
  localStorage.setItem(storageKey, value);
}

function getItem(key, name) {
  // Change to true to enable logging
  logging = false;

  storageKey = name + "-" + key;
  element = document.getElementById(key);
  value = localStorage.getItem(storageKey);

  if (logging) {
    console.log("Getting " + storageKey + " as " + value);
  }

  if (element.type == "checkbox") {
    if (value == "false") {
      value = false;
    } else if (value == "true") {
      value = true;
    }
    element.checked = value;
  } else {
    element.value = value;
  }
}
