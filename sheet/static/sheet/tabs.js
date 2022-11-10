function setupTabs(tab){
    //add event listener to switch tabs
    document.querySelectorAll(".tabButton").forEach(button => {
        const sidebar = button.parentElement;
        const tabsContainer = sidebar.parentElement;
        const tabNumber = button.dataset.forTab;

        let queryString = '.tabContent[data-tab="' + tabNumber + '"]'
        const tabToActivate = tabsContainer.querySelector(queryString)

        button.addEventListener("click", () => {
            sidebar.querySelectorAll(".tabButton").forEach(button => {
              button.classList.remove("tabButton--active");
            })

            tabsContainer.querySelectorAll(".tabContent").forEach(tab => {
              tab.classList.remove("tabContent--active");
            })

            button.classList.add("tabButton--active");
            tabToActivate.classList.add("tabContent--active");

            console.log("Storing active tab as " + tabNumber);
            localStorage.setItem("activeTab", tabNumber)
        })

        //Set active tab
        if(tab == tabNumber){
            console.log("Activating tab from localstorage to " + tab);
            button.classList.add("tabButton--active");
            tabToActivate.classList.add("tabContent--active");
        }
    })
}

document.addEventListener("DOMContentLoaded", () => {
    activeTab = localStorage.getItem("activeTab")
    setupTabs(activeTab);
})