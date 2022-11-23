function setColor(accentColor){
    let root = document.documentElement;
    console.log(root);

    root.style.setProperty('--primary-accent', accentColor); 
    console.log(root);   
}