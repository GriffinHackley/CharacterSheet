function setColor(primary, secondary){
    let root = document.documentElement;
    console.log(root);

    root.style.setProperty('--primary-accent', primary);
    root.style.setProperty('--secondary-accent', secondary); 
    console.log(root);   
}