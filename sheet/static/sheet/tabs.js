function setupTabs(name) {
  //add event listener to switch tabs
  document.querySelectorAll(".tabButton").forEach((button) => {
    const sidebar = button.parentElement;
    const tabsContainer = sidebar.parentElement;

    prefixes = ["main-", "feature-"];

    prefixes.forEach((prefix) => {
      activeButton = localStorage.getItem(name + prefix + "activeButton");

      //Set initial active tabs
      if (activeButton == button.id) {
        console.log("Activating button from localstorage to " + activeButton);
        activateTab(name, prefix);
      }
    });

    button.addEventListener("click", () => {
      console.log("Clicked");
      prefix = button.dataset.forTab.split("-")[0];
      prefix = prefix + "-";
      sidebar.querySelectorAll(".tabButton").forEach((button) => {
        button.classList.remove("tabButton--active");
      });

      tabsContainer.querySelectorAll(".tabContent").forEach((tab) => {
        tab.classList.remove("tabContent--active");
      });

      storeKey = name + prefix + "activeButton";
      console.log("Storing " + storeKey + " as " + button.id);
      localStorage.setItem(storeKey, button.id);

      console.log("Activating buttons");
      activateTabs(name);
    });
  });
}

function activateTabs(name) {
  activateTab(name, "main-");
  activateTab(name, "feature-");
}

function activateTab(name, prefix) {
  activeButton = localStorage.getItem(name + prefix + "activeButton");
  button = document.getElementById(activeButton);
  const sidebar = button.parentElement;
  const tabsContainer = sidebar.parentElement;
  const tabName = button.dataset.forTab;

  let queryString = '.tabContent[data-tab="' + tabName + '"]';
  const tabToActivate = tabsContainer.querySelector(queryString);

  console.log("Activating button: " + button.id);
  button.classList.add("tabButton--active");
  tabToActivate.classList.add("tabContent--active");
}

function init(name) {
  name = name + "-";
  document.addEventListener("DOMContentLoaded", () => {
    setupTabs(name);
  });
}
