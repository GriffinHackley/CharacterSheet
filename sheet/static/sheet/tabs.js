function setupTabs(name, logging) {
  //add event listener to switch tabs
  document.querySelectorAll(".tabButton").forEach(button => {
    const sidebar = button.parentElement;
    const tabsContainer = sidebar.parentElement;

    prefixes = ["main-", "feature-"];

    prefixes.forEach(prefix => {
      activeButton = localStorage.getItem(name + prefix + "activeButton");

      //Set initial active tabs
      if (activeButton == button.id) {
        if (logging) {
          console.log("Activating button from localstorage to " + activeButton);
        }
        activateTab(name, prefix, logging);
      }
    });

    button.addEventListener("click", () => {
      prefix = button.dataset.forTab.split("-")[0];
      prefix = prefix + "-";
      sidebar.querySelectorAll(".tabButton").forEach(button => {
        button.classList.remove("tabButton--active");
      });

      tabsContainer.querySelectorAll(".tabContent").forEach(tab => {
        tab.classList.remove("tabContent--active");
      });

      storeKey = name + prefix + "activeButton";
      localStorage.setItem(storeKey, button.id);
      if (logging) {
        console.log("Storing " + storeKey + " as " + button.id);
      }

      if (logging) {
        console.log("Activating buttons");
      }
      activateTabs(name, logging);
    });
  });
}

function activateTabs(name, logging) {
  activateTab(name, "main-", logging);
  activateTab(name, "feature-", logging);
}

function activateTab(name, prefix, logging) {
  activeButton = localStorage.getItem(name + prefix + "activeButton");
  button = document.getElementById(activeButton);
  const sidebar = button.parentElement;
  const tabsContainer = sidebar.parentElement;
  const tabName = button.dataset.forTab;

  let queryString = '.tabContent[data-tab="' + tabName + '"]';
  const tabToActivate = tabsContainer.querySelector(queryString);

  if (logging) {
    console.log("Activating button: " + button.id);
  }

  button.classList.add("tabButton--active");
  tabToActivate.classList.add("tabContent--active");
}

function init(name) {
  logging = false;
  name = name + "-";
  document.addEventListener("DOMContentLoaded", () => {
    setupTabs(name, logging);
  });
}
