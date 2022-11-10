function storeItem(key, name) {
    storageKey = name + "-" + key
    localStorage.setItem(storageKey, document.getElementById(key).value);
    console.log("Storing " + storageKey + " as " + document.getElementById(key).value)
}
  
function getItem(key, name) {
    storageKey = name + "-" + key
    document.getElementById(key).value = localStorage.getItem(storageKey);
    console.log("Getting " + storageKey + " as " + document.getElementById(key).value)
}