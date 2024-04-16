import { useState } from "react";
import CollapsibleTab from "../../shared/collapsibleTab";

function setUpClassTabs(featuresInfo) {
  let mainClass = "";
  let length = 0;
  let classTabs = [];
  for (let cls in featuresInfo.Class) {
    classTabs.push(cls);
    if (featuresInfo.Class[cls].length > length) {
      mainClass = cls;
      length = featuresInfo.Class[cls].length;
    }
  }

  return [mainClass, classTabs];
}

function setUpMainTabs(featuresInfo, setMainActiveTab, activeTab) {
  let tabs = {};

  for (let source in featuresInfo) {
    let feature = featuresInfo[source];
    tabs[source] = feature;
  }

  let headerButtons = [];

  //Get all tab buttons set up
  for (let tabName in tabs) {
    headerButtons.push(
      <button
        type="button"
        key={tabName}
        onClick={() => setMainActiveTab(tabName)}
      >
        {tabName}
      </button>
    );
  }

  let contents = tabs[activeTab];

  return [headerButtons, contents];
}

export default function FeaturesTab({ featuresInfo }) {
  const [activeTab, setMainActiveTab] = useState("Class");
  let [headerButtons, contents] = setUpMainTabs(
    featuresInfo,
    setMainActiveTab,
    activeTab
  );

  let [mainClass, classTabs] = setUpClassTabs(featuresInfo);
  const [activeSubTab, setActiveSubTab] = useState(mainClass);

  let classButtons = [];
  if (activeTab == "Class") {
    //Get all tab buttons set up
    for (let tabName in contents) {
      classButtons.push(
        <button
          type="button"
          key={tabName}
          onClick={() => setActiveSubTab(tabName)}
        >
          {tabName}
        </button>
      );
    }
    contents = contents[activeSubTab];
  }
  let allTabs = [];
  contents.forEach(content => {
    allTabs.push(<CollapsibleTab name={content.name} text={content.text} />);
  });

  return (
    <section className="flexPanel">
      <div className="flexHeader tabHeader">
        {headerButtons}
      </div>
      <div className="tabHeader">
        {classButtons}
      </div>
      {allTabs}
    </section>
  );
}
