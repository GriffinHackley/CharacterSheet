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

function addProficiencies(
  allAncestries,
  choice,
  proficiencyChoices,
  setProficiencyChoices
) {
  if (choice === "none") {
    return;
  }

  let proficiencies = allAncestries[choice].Proficiencies;

  for (let [type, value] of Object.entries(proficiencies)) {
    for (let i = 0; i < value.length; i++) {
      proficiencyChoices[type][`ancestry-${type}-${i}`] = value[i];
    }
  }

  setProficiencyChoices(proficiencyChoices);
}

export default function Ancestry({
  allAncestries,
  chosenAncestry,
  setAncestry,
  proficiencyChoices,
  setProficiencyChoices
}) {
  addProficiencies(
    allAncestries,
    chosenAncestry,
    proficiencyChoices,
    setProficiencyChoices
  );

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
