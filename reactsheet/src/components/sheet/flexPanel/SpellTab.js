import "../../../css/sheet/flexPanel/SpellTab.css";
import { useState } from "react";

function getSpellHeader(spellInfo, config) {
  let spellHeader = [];

  spellHeader.push(
    <div className="spellAbility spellHeaderItem">
      <div className="value">
        {spellInfo.ability}
      </div>
      <div className="key">Spell Ability</div>
    </div>
  );

  if (config.edition == "Pathfinder") {
    spellHeader.push(
      <div className="casterLevel spellHeaderItem">
        <div className="value">
          {config.level}
        </div>
        <div className="key">Caster Level</div>
      </div>

      //calculate dc for every spell level
    );
  } else if (config.edition == "5e") {
    spellHeader.push(
      <div
        className="tooltip centered spellModifier spellHeaderItem"
        data-tooltip="{ source }"
      >
        <div className="value">
          {spellInfo.spellAttack.value}
        </div>
        <div className="key">Spell Modifier</div>
      </div>
    );

    spellHeader.push(
      <div
        className="tooltip centered saveDC spellHeaderItem"
        data-tooltip="{{ source }}"
      >
        <div className="value">
          {spellInfo.saveDC.value}
        </div>
        <div className="key">Save DC</div>
      </div>
    );
  }

  return spellHeader;
}

function getSpellList(spellInfo, config) {
  let spellList = [];

  for (let level in spellInfo.spells) {
    let spellLevel = level;
    level = spellInfo.spells[level];
    let spells = [];

    for (let spell in level.list) {
      spells.push(
        <div className="spellName">
          {spell}
        </div>
      );
    }

    if (spellLevel == "Cantrip") {
      spellList.unshift(
        <div className="spellLevel">
          <div className="spellLevelHeader">
            <div>
              Level: {spellLevel}
            </div>
          </div>
          {spells}
        </div>
      );
    } else {
      spellList.push(
        <div className="spellLevel">
          <div className="spellLevelHeader">
            <div>
              Level: {spellLevel}
            </div>
            <div className="spellSlots">
              Slots: {level["slots"]}
            </div>
          </div>
          {spells}
        </div>
      );
    }
  }

  return spellList;
}

function setUpSourceTabs(spellInfo) {
  let mainSource = "";
  let length = 0;
  let sourceTabs = [];
  for (let src in spellInfo) {
    sourceTabs.push(spellInfo[src]);
    if (spellInfo[src] > length) {
      length = spellInfo[src].length;
    }
  }

  mainSource = 1;
  return [mainSource, sourceTabs];
}

export default function SpellTab({ spellInfo, config }) {
  let [mainSource, sourceTabs] = setUpSourceTabs(spellInfo);
  const [activeSourceTab, setActiveSourceTab] = useState(mainSource);

  let sourceButtons = [];

  //Get all tab buttons set up
  for (let source in sourceTabs) {
    let tabName = sourceTabs[source].name;
    sourceButtons.push(
      <button
        type="button"
        key={tabName}
        onClick={() => setActiveSourceTab(source)}
      >
        {tabName}
      </button>
    );
  }

  let spellHeader = getSpellHeader(sourceTabs[activeSourceTab], config);
  let spellList = getSpellList(sourceTabs[activeSourceTab], config);

  return (
    <section className="spellsContainer">
      <div className="tabHeader">
        {sourceButtons}
      </div>
      <div className="spellHeader">
        {spellHeader}
      </div>
      <div className="spellList">
        {spellList}
      </div>
    </section>
  );
}
