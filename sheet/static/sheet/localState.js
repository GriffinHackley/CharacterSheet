function storeItem(key){
    console.log(key)
    localStorage.setItem(key, document.getElementById(key).value);
    console.log("Storing " + key + " as " + document.getElementById(key).value)
}
  
function getItem(key){
    document.getElementById(key).value = localStorage.getItem(key);
    console.log("Getting " + key + " as " + document.getElementById(key).value)
}