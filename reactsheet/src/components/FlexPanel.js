import { useState } from "react";
import FeaturesTab from "./Tabs/FeaturesTab";
import EquipmentTab from "./Tabs/EquipmentTab";
import ProficienciesTab from "./Tabs/ProficienciesTab";
import SpellTab from "./Tabs/SpellTab";
import PowerAttackTab from "./Tabs/PowerAttackTab";
import FlavorTab from "./Tabs/FlavorTab";

export default function FlexPanel({panelInfo}){
    const [activeTab, setMainActiveTab] = useState('Features')

    let tabs = {
        "Features": <FeaturesTab featuresInfo={panelInfo}></FeaturesTab>,
        "Equipment": <EquipmentTab></EquipmentTab>,
        "Proficiencies": <ProficienciesTab></ProficienciesTab>,
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