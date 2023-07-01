import { useState } from "react";
import FeaturesTab from "./FeaturesTab";
import EquipmentTab from "./EquipmentTab";
import ProficienciesTab from "./ProficienciesTab";
import SpellTab from "./SpellTab";
import PowerAttackTab from "./PowerAttackTab";
import FlavorTab from "./FlavorTab";

export default function FlexPanel({config, featureInfo, profInfo}){
    const [activeTab, setMainActiveTab] = useState('Features')

    let tabs = {
        "Features": <FeaturesTab featuresInfo={featureInfo}></FeaturesTab>,
        "Equipment": <EquipmentTab></EquipmentTab>,
        "Proficiencies": <ProficienciesTab profInfo={profInfo} config={config}></ProficienciesTab>,
        "Spells": <SpellTab></SpellTab>,
        "Power Attack": <PowerAttackTab></PowerAttackTab>,
        "Flavor": <FlavorTab></FlavorTab>,
    };
    
    let tabContents = tabs[activeTab]

    let headerButtons = [];

    for(let tabName in tabs){
        headerButtons.push(
          <button
            type="button"
            onClick={() => setMainActiveTab(tabName)}
          >
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
    )
}