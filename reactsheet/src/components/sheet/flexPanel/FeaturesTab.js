import { useState } from "react";

export default function FeaturesTab({ featuresInfo }) {
  const [activeTab, setMainActiveTab] = useState("Class");

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

  let tabContents = [];

  let init = Array(contents.length).fill(false);
  const [expandedFeatures, setExpandedFeatures] = useState(init);

  const toggleExpanded = index => {
    let ret = [...expandedFeatures];
    ret[index] = !expandedFeatures[index];
    setExpandedFeatures(ret);
  };

  const getContent = (feature, index) => {
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
          {getContent(feature, index)}
        </div>
      </div>
    );
  }

  return (
    <section className="flexPanel">
      <div className="flexHeader tabHeader">
        {headerButtons}
      </div>
      {tabContents}
    </section>
  );
}
