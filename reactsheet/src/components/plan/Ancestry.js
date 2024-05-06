import { useState } from "react";
import Selector from "../shared/Selector";

function getFeatureText(ancestries, chosenAncestry) {
  let text = [];
  if (chosenAncestry === "none") {
    return text;
  }

  let features = ancestries[chosenAncestry].Features;

  features.forEach(feature => {
    text.push(
      <div key={feature.name}>
        <h5 className="featureHeading">
          {feature.name}:
        </h5>
        <div dangerouslySetInnerHTML={{ __html: feature.text }} />
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
