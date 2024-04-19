import { useState } from "react";
import FeaturesTab from "./FeaturesTab";
import EquipmentTab from "./EquipmentTab";
import ProficienciesTab from "./ProficienciesTab";
import SpellTab from "./SpellTab";
import GraphTab from "./GraphTab";
import FlavorTab from "./FlavorTab";
import { ToggleButton, ToggleButtonGroup } from "@mui/material";

export default function FlexPanel({
  config,
  featureInfo,
  equipmentInfo,
  profInfo,
  spellInfo,
  graphInfo,
  flavorInfo
}) {
  const [activeTab, setActiveTab] = useState("Features");

  let tabs = {
    Features: <FeaturesTab featuresInfo={featureInfo} />,
    Equipment: <EquipmentTab equipmentInfo={equipmentInfo} config={config} />,
    Proficiencies: <ProficienciesTab profInfo={profInfo} config={config} />,
    Spells: <SpellTab spellInfo={spellInfo} config={config} />,
    "Damage Graph": <GraphTab graphInfo={graphInfo} />,
    Flavor: <FlavorTab flavorInfo={flavorInfo} />
  };

  let tabContents = tabs[activeTab];

  const control = {
    value: activeTab,
    onChange: (event, newTab) => {
      if (newTab) {
        setActiveTab(newTab);
      }
    },
    exclusive: true
  };

  let toggleButtons = [];

  for (let tab in tabs) {
    toggleButtons.push(
      <ToggleButton value={tab} key={tab}>
        {tab}
      </ToggleButton>
    );
  }

  return (
    <section className="flexPanel">
      <ToggleButtonGroup {...control} size="large" fullWidth={true}>
        {toggleButtons}
      </ToggleButtonGroup>
      {tabContents}
    </section>
  );
}
