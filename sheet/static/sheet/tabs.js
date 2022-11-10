function setupTabs(){
    document.querySelectorAll(".tabButton").forEach(button => {
      button.addEventListener("click", () => {
        const sidebar = button.parentElement;
        const tabsContainer = sidebar.parentElement;
        const tabNumber = button.dataset.forTab;
        
        let queryString = '.tabContent[data-tab="' + tabNumber + '"]'
        const tabToActivate = tabsContainer.querySelector(queryString)

        sidebar.querySelectorAll(".tabButton").forEach(button => {
          button.classList.remove("tabButton--active");
        })

        tabsContainer.querySelectorAll(".tabContent").forEach(tab => {
          tab.classList.remove("tabContent--active");
        })

        button.classList.add("tabButton--active");
        tabToActivate.classList.add("tabContent--active");
      })
    })
  }

document.addEventListener("DOMContentLoaded", () => {
    setupTabs();
})