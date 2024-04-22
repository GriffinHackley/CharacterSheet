import { useState } from "react";
import CollapsibleTab from "../../shared/collapsibleTab";
import { ToggleButton, ToggleButtonGroup } from "@mui/material";

// Find the class that has the most features and set it as the main class
function setUpClassTabs(featuresInfo) {
  let mainClass = "";
  let length = 0;
  for (let cls in featuresInfo.Class) {
    if (featuresInfo.Class[cls].length > length) {
      mainClass = cls;
      length = featuresInfo.Class[cls].length;
    }
  }

  return mainClass;
}

function setUpMainTabs(featuresInfo, setActiveTab, activeTab) {
  let tabs = {};

  for (let source in featuresInfo) {
    let feature = featuresInfo[source];
    tabs[source] = feature;
  }

  let headerButtons = [];

  //Get all tab buttons set up
  for (let tabName in tabs) {
    headerButtons.push(
      <ToggleButton value={tabName} key={tabName}>
        {tabName}
      </ToggleButton>
    );
  }

  let contents = tabs[activeTab];

  return [headerButtons, contents];
}

export default function FeaturesTab({ featuresInfo }) {
  const [activeTab, setActiveTab] = useState("Class");

  const control = {
    value: activeTab,
    onChange: (event, newTab) => {
      if (newTab) {
        setActiveTab(newTab);
      }
    },
    exclusive: true
  };

  let [headerButtons, contents] = setUpMainTabs(
    featuresInfo,
    setActiveTab,
    activeTab
  );

  let mainClass = setUpClassTabs(featuresInfo);
  const [activeClassTab, setActiveClassTab] = useState(mainClass);

  const classControl = {
    value: activeClassTab,
    onChange: (event, newTab) => {
      if (newTab) {
        setActiveClassTab(newTab);
      }
    },
    exclusive: true
  };

  let classButtons = [];
  if (activeTab == "Class") {
    //Get all tab buttons set up
    for (let tabName in contents) {
      if (Object.keys(featuresInfo.Class).length < 1) {
        classButtons.push(
          <ToggleButton
            key={tabName}
            value={tabName}
            onClick={() => setActiveClassTab(tabName)}
          >
            {tabName}
          </ToggleButton>
        );
      }
    }
    contents = contents[activeClassTab];
  }

  let allTabs = [];
  contents.forEach(content => {
    allTabs.push(<CollapsibleTab name={content.name} text={content.text} />);
  });

  return (
    <section>
      <ToggleButtonGroup
        className="flexHeader tabHeader"
        {...control}
        size="medium"
        fullWidth={true}
      >
        {headerButtons}
      </ToggleButtonGroup>
      <ToggleButtonGroup
        className="tabHeader"
        {...classControl}
        size="small"
        fullWidth={true}
      >
        {classButtons}
      </ToggleButtonGroup>
      {allTabs}
    </section>
  );
}
