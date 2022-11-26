function setColor(primary, secondary){
    let root = document.documentElement;

    root.style.setProperty('--primary-accent', primary);
    root.style.setProperty('--secondary-accent', secondary); 
}