import { useState } from "react";
import FeaturesTab from "./FeaturesTab";
import EquipmentTab from "./EquipmentTab";
import ProficienciesTab from "./ProficienciesTab";
import SpellTab from "./SpellTab";
import PowerAttackTab from "./PowerAttackTab";
import FlavorTab from "./FlavorTab";

export default function FlexPanel({
  config,
  featureInfo,
  profInfo,
  flavorInfo
}) {
  const [activeTab, setMainActiveTab] = useState("Features");

  let tabs = {
    Features: <FeaturesTab featuresInfo={featureInfo} />,
    Equipment: <EquipmentTab />,
    Proficiencies: <ProficienciesTab profInfo={profInfo} config={config} />,
    Spells: <SpellTab />,
    "Power Attack": <PowerAttackTab />,
    Flavor: <FlavorTab flavorInfo={flavorInfo} />
  };

  let tabContents = tabs[activeTab];

  let headerButtons = [];

  for (let tabName in tabs) {
    headerButtons.push(
      <button type="button" onClick={() => setMainActiveTab(tabName)}>
        {tabName}
      </button>
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
