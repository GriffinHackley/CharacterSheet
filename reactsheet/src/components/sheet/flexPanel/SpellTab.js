import "../../../css/sheet/flexPanel/SpellTab.css";
import formatSource from "../../../scripts/formatSource";
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
        className="tooltip centered concentration spellHeaderItem"
        data-tooltip={formatSource(spellInfo.concentration.source)}
      >
        <div className="value">
          {spellInfo.concentration.value}
        </div>
        <div className="key">Concentration</div>
      </div>
    );
    spellHeader.push(
      <div
        className="tooltip centered spellModifier spellHeaderItem"
        data-tooltip={formatSource(spellInfo.spellAttack.source)}
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
        data-tooltip={formatSource(spellInfo.saveDC.source)}
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

function getSpellList(list, slots, activeSource, config) {
  let spellList = [];

  for (let level in list) {
    let spellLevel = level;

    if (level != "Cantrip") {
      spellLevel = parseInt(level);
    }

    let listForLevel = list[level];
    let spells = [];
    for (let spell in listForLevel) {
      let fullSpell = JSON.parse(listForLevel[spell]);
      if (fullSpell.source != activeSource) {
        continue;
      }
      spells.push(
        <tr className="spell">
          <td className="spellName">
            {fullSpell.name}
          </td>
          <td className="spellCastingTime">
            {fullSpell.shortCast}
          </td>
          <td className="spellRange">
            {fullSpell.range}
          </td>
          <td className="spellComponents">
            {fullSpell.shortComponent}
          </td>
        </tr>
      );
    }

    if (spells.length == 0) {
      continue;
    }

    if (spellLevel == "Cantrip") {
      spellList.unshift(
        <div className="spellLevel">
          <div className="spellLevelHeader">
            <div>
              Level: {spellLevel}
            </div>
          </div>
          <table>
            <tr>
              <th>Name</th>
              <th>Casting Time</th>
              <th>Range</th>
              <th>Components</th>
            </tr>

            {spells}
          </table>
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
              Slots: {slots[level]}
            </div>
          </div>
          <table>
            <tr>
              <th>Name</th>
              <th>Casting Time</th>
              <th>Range</th>
              <th>Components</th>
            </tr>

            {spells}
          </table>
        </div>
      );
    }
  }

  return spellList;
}

function setUpSourceTabs(spellInfo) {
  let mainSource = 0;
  let highestMod = 0;
  let sourceTabs = {};

  for (let src in spellInfo.headers) {
    sourceTabs[src] = spellInfo.headers[src];

    let currentMod = spellInfo.headers[src].abilityMod;
    if (currentMod > highestMod) {
      highestMod = currentMod;
      mainSource = src;
    }
  }

  return [mainSource, sourceTabs];
}

export default function SpellTab({ spellInfo, config }) {
  let [mainSource, sourceTabs] = setUpSourceTabs(spellInfo);
  const [activeSourceTab, setActiveSourceTab] = useState(mainSource);

  let sourceButtons = [];

  //Get all tab buttons set up
  for (let source in sourceTabs) {
    sourceButtons.push(
      <button
        type="button"
        key={source}
        onClick={() => setActiveSourceTab(source)}
      >
        {source}
      </button>
    );
  }

  let spellHeader = getSpellHeader(sourceTabs[activeSourceTab], config);
  let spellList = getSpellList(
    spellInfo.list,
    spellInfo.slots,
    activeSourceTab,
    config
  );

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
