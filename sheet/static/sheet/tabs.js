function setupTabs(tab){
    //add event listener to switch tabs
    document.querySelectorAll(".tabButton").forEach(button => {
        const sidebar = button.parentElement;
        const tabsContainer = sidebar.parentElement;
        const tabName = button.dataset.forTab;

        let queryString = '.tabContent[data-tab="' + tabName + '"]'
        const tabToActivate = tabsContainer.querySelector(queryString)

        button.addEventListener("click", () => {
            sidebar.querySelectorAll(".tabButton").forEach(button => {
              button.classList.remove("tabButton--active");
            })

            tabsContainer.querySelectorAll(".tabContent").forEach(tab => {
              tab.classList.remove("tabContent--active");
            })

            console.log("Storing active tab as " + tabName);
            localStorage.setItem("activeTab", tabName)

            console.log("Activating tab: " + tabToActivate)
            button.classList.add("tabButton--active");
            tabToActivate.classList.add("tabContent--active");
        })

        //Set active tab
        if(tab == tabName){
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