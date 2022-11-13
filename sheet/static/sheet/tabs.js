function setupTabs(tab){
    //add event listener to switch tabs
    document.querySelectorAll(".tabButton").forEach(button => {
        const sidebar = button.parentElement;
        const tabsContainer = sidebar.parentElement;

        prefixes = ["main-", "feature-"]

        prefixes.forEach(prefix => {
            activeButton = localStorage.getItem(prefix + "activeButton")

            //Set initial active tabs
            if(activeButton == button.id){
                console.log("Activating button from localstorage to " + activeButton);
                activateTab(prefix)
            }
        })
        

        button.addEventListener("click", () => {
            prefix = button.dataset.forTab.split("-")[0]
            prefix = prefix + "-"
            sidebar.querySelectorAll(".tabButton").forEach(button => {
                button.classList.remove("tabButton--active");
            })

            tabsContainer.querySelectorAll(".tabContent").forEach(tab => {
                tab.classList.remove("tabContent--active");
            })

            storeKey = prefix + "activeButton"
            console.log("Storing " + storeKey + " as " + button.id);
            localStorage.setItem(storeKey, button.id)

            console.log("Activating buttons")
            activateTabs()
        })
    })
}

function activateTabs(){
    activateTab("main-")
    activateTab("feature-")
}

function activateTab(prefix){
    activeButton = localStorage.getItem(prefix + "activeButton")
    button = document.getElementById(activeButton)
    const sidebar = button.parentElement;
    const tabsContainer = sidebar.parentElement;
    const tabName = button.dataset.forTab;

    let queryString = '.tabContent[data-tab="' + tabName + '"]'
    const tabToActivate = tabsContainer.querySelector(queryString)

    console.log("Activating button: " + button.id)
    button.classList.add("tabButton--active");
    tabToActivate.classList.add("tabContent--active");
}

document.addEventListener("DOMContentLoaded", () => {
    setupTabs();
})