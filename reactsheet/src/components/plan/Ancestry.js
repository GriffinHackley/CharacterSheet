import { useState } from "react";
import Selector from "../shared/selector";

function displayFeature(feature) {
  if (feature === "") {
    return;
  }
  let text = [];
  feature.forEach(line => {
    if (line.type === "normal") {
      text.push(
        <p className="featureText">
          {line.text}
        </p>
      );
    } else if (line.type === "heading") {
      text.push(
        <h5 className="featureText">
          {line.text}
        </h5>
      );
    } else if (line.type === "table") {
      text.push(<h1>Tables have not been implemented</h1>);
    }
  });
  return (
    <div className="featureContainer">
      {text}
    </div>
  );
}

function getFeatureText(ancestries, chosenAncestry) {
  let text = [];
  if (chosenAncestry === "none") {
    return text;
  }

  let features = ancestries[chosenAncestry].features;

  features.forEach(feature => {
    text.push(
      <div>
        <h5 className="featureHeading">
          {feature.name}:
        </h5>
        {displayFeature(feature.text)}
      </div>
    );
  });

  return text;
}

export default function Ancestry({ ancestries }) {
  let allAncestries = ancestries.all;
  let choice = ancestries.choice;
  const [chosenAncestry, setAncestry] = useState(choice);

  return (
    <div>
      <h3>Ancestry</h3>
      <Selector
        type={"ancestry"}
        choice={chosenAncestry}
        allChoices={Object.keys(allAncestries)}
        setFunction={setAncestry}
      />
      {getFeatureText(allAncestries, chosenAncestry)}
    </div>
  );
}
