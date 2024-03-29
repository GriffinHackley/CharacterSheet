import { useState } from "react";

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

function getContent(feature, expandedFeatures, index) {
  if (expandedFeatures[index]) {
    let text = [];
    feature.text.forEach(line => {
      if (line.type == "normal") {
        text.push(
          <p>
            {line.text}
          </p>
        );
      } else if (line.type == "heading") {
        text.push(
          <h4>
            {line.text}
          </h4>
        );
      } else if (line.type == "table") {
        <h1>Tables have not been implemented</h1>;
      }
    });
    return (
      <div>
        {text}
      </div>
    );
  } else {
    return;
  }
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

  let tabContents = [];
  let init = Array(contents.length).fill(false);
  const [expandedFeatures, setExpandedFeatures] = useState(init);

  const toggleExpanded = index => {
    let ret = [...expandedFeatures];
    ret[index] = !expandedFeatures[index];
    setExpandedFeatures(ret);
  };

  for (let index in contents) {
    let feature = contents[index];

    tabContents.push(
      <div className="feature">
        <button
          type="button"
          className="featureName collapsible"
          key={feature.name}
          onClick={() => toggleExpanded(index)}
        >
          {feature.name}
        </button>
        <div className="featureDescription">
          {getContent(feature, expandedFeatures, index)}
        </div>
      </div>
    );
  }

  return (
    <section className="flexPanel">
      <div className="flexHeader tabHeader">
        {headerButtons}
      </div>
      <div className="tabHeader">
        {classButtons}
      </div>
      {tabContents}
    </section>
  );
}
