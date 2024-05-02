import { useState } from "react";
import { useLocation } from "react-router-dom";
import CollapsibleTab from "../shared/collapsibleTab";
import { ToggleButton, ToggleButtonGroup } from "@mui/material";

// Find the class that has the most features and set it as the main class
function getMainClass(featuresInfo) {
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

function setUpMainTabs(featuresInfo, activeTab, setActiveTab) {
  const control = {
    value: activeTab,
    onChange: (event, newTab) => {
      if (newTab) {
        setActiveTab(newTab);
      }
    },
    exclusive: true
  };

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

  return [headerButtons, contents, control];
}

function setupClassTabs(
  featuresInfo,
  contents,
  activeClassTab,
  setActiveClassTab
) {
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

  return [contents, classControl, classButtons];
}

export default function Features() {
  const location = useLocation();
  const { featuresInfo } = location.state;
  const [activeTab, setActiveTab] = useState("Class");

  let [headerButtons, contents, control] = setUpMainTabs(
    featuresInfo,
    activeTab,
    setActiveTab
  );

  let classControl = {};
  let classButtons = [];
  let allTabs = [];
  let mainClass = getMainClass(featuresInfo);
  const [activeClassTab, setActiveClassTab] = useState(mainClass);
  if (activeTab == "Class") {
    [contents, classControl, classButtons] = setupClassTabs(
      featuresInfo,
      contents,
      activeClassTab,
      setActiveClassTab
    );
  }

  if (activeTab == "Misc.") {
    Object.keys(contents).forEach(source => {
      if (contents[source].length > 0) {
        allTabs.push(
          <h3 style={{ paddingLeft: "5px" }}>
            {source}
          </h3>
        );
        contents[source].forEach(content => {
          allTabs.push(
            <CollapsibleTab name={content.name} text={content.text} />
          );
        });
      }
    });
  } else if (activeTab == "Race") {
    let attributes = "";
    contents.Attributes.forEach(content => {
      attributes =
        attributes + `<div><h4>${content.name}: </h4> ${content.text}</div>`;
    });

    allTabs.push(<CollapsibleTab name="Attributes" text={attributes} />);

    contents.Features.forEach(content => {
      allTabs.push(<CollapsibleTab name={content.name} text={content.text} />);
    });
  } else {
    contents.forEach(content => {
      allTabs.push(<CollapsibleTab name={content.name} text={content.text} />);
    });
  }

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
