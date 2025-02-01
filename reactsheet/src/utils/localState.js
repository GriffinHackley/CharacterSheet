let logging = false;

export function storeCheckboxValue(key, name) {
  // Change to true to enable logging
  let storageKey = name + "-" + key;
  let element = document.getElementById(key);
  let value = null;
  if (element.type === "checkbox") {
    value = element.checked;
  } else {
    value = element.value;
  }
  if (logging) {
    console.log("Storing " + storageKey + " as " + value);
  }
  localStorage.setItem(storageKey, value);
}

export function storeLayout(id, layout) {
  let storageKey = id + "-Layout";

  if (layout == null) {
    console.log("Got null layout. Not saving");

    return;
  }

  let ret = JSON.stringify(
    layout.map(value => {
      return JSON.stringify(value);
    })
  );

  if (logging) {
    console.log("Storing " + storageKey + " as " + ret);
  }

  localStorage.setItem(storageKey, ret);
}

export function getLayout(id) {
  let storageKey = id + "-Layout";
  let item = localStorage.getItem(storageKey);

  if (item === null) {
    return null;
  }

  let ret = JSON.parse(item).map(element => {
    return JSON.parse(element);
  });

  if (logging) {
    console.log("Getting " + storageKey + " as :" + ret);
  }

  return ret;
}

export function getCheckboxValue(key, name) {
  // Change to true to enable logging
  let logging = false;

  let storageKey = name + "-" + key;
  let element = document.getElementById(key);
  let value = localStorage.getItem(storageKey);

  if (logging) {
    console.log("Getting " + storageKey + " as " + value);
  }

  if (element.type === "checkbox") {
    if (value === "false") {
      value = false;
    } else if (value === "true") {
      value = true;
    }
    element.checked = value;
  } else {
    element.value = value;
  }
}
