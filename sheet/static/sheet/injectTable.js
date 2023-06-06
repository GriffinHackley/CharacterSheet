function inject(featureName, table){
    table = table.replaceAll("&#x27;", "")
    table = table.replaceAll("&lt;", "<")
    table = table.replaceAll("&gt;", ">")
    table = table.replaceAll("&quot;", "'")
    test = document.getElementById(featureName)
    test.innerHTML = table
}