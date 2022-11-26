function inject(featureName, table){
    table = table.replaceAll("&#x27;", "")
    table = table.replaceAll("&lt;", "<")
    table = table.replaceAll("&gt;", ">")
    table = table.replaceAll("&quot;", "'")
    console.log(table)
    test = document.getElementById(featureName)
    test.innerHTML = table
}