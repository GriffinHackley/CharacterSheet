import { useState } from "react";
import "../../css/plan/Background.css";

let allSkills = [
  "Acrobatics",
  "Animal Handling",
  "Arcana",
  "Athletics",
  "Deception",
  "History",
  "Insight",
  "Intimidation",
  "Investigation",
  "Medicine",
  "Nature",
  "Perception",
  "Performance",
  "Persuasion",
  "Religion",
  "Sleight of Hand",
  "Stealth",
  "Survival"
];

let allArtisanTools = [
  "Alchemist's supplies",
  "Brewer's supplies",
  "Calligrapher's supplies",
  "Carpenter's tools",
  "Cartographer's tools",
  "Cobbler's tools",
  "Cook's utensils",
  "Glassblower's tools",
  "Jeweler's tools",
  "Leatherworker's tool",
  "Mason's tools",
  "Painter's supplies",
  "Potter's tools",
  "Smith's tools",
  "Tinker's tools",
  "Weaver's tools",
  "Woodcarver's tools"
];

let allTools = [
  "Disguise kit",
  "Forgery kit",
  "Herbalism kit",
  "Navigator's tools",
  "Poisoner's kit",
  "Thieves' tools"
];

let allGames = [
  "Dice set",
  "Dragonchess set",
  "Playing card set",
  "Three-Dragon Ante set"
];

let allInstruments = [
  "Bagpipes",
  "Drum",
  "Dulcimer",
  "Flute",
  "Lute",
  "Lyre",
  "Horn",
  "Pan flute",
  "Shawm",
  "Viol"
];

let allLanguages = [
  "Dwarvish",
  "Elvish",
  "Giant",
  "Gnomish",
  "Goblin",
  "Halfling",
  "Orc",
  "Abyssal",
  "Celestial",
  "DeepSpeech",
  "Draconic",
  "Infernal",
  "Aquan",
  "Auran",
  "Ignan",
  "Terran",
  "Sylvan",
  "Undercommon"
];

function optionSelector(id, setOption, currentOption, otherOption, allOptions) {
  let options = [];

  //   Dont let them choose the same option as the other selector
  allOptions = allOptions.filter(option => option !== otherOption);
  let oneSelected = false;

  for (let option in allOptions) {
    let isSelected = false;
    if (currentOption.toLowerCase() === allOptions[option].toLowerCase()) {
      isSelected = true;
      oneSelected = true;
    }
    options.push(
      <option selected={isSelected}>
        {allOptions[option]}
      </option>
    );
  }
  if (currentOption === "none") {
    options.push(
      <option hidden disabled selected value>
        -- select an option --
      </option>
    );
  } else if (!oneSelected) {
    throw `${currentOption} is not in list ${allOptions}`;
  }
  return (
    <select name={id} id={id} onChange={e => setOption(e.target.value)}>
      {options}
    </select>
  );
}

function miscProfSelector(id, selectorType, setSelector) {
  return (
    <div onChange={e => setSelector(e.target.value)}>
      <input
        type="radio"
        id={id + "Language"}
        name={id + "miscProf"}
        value="languages"
        defaultChecked={selectorType === "languages" ? true : false}
      />
      <label for={id + "Language"}>Language</label>

      <input
        type="radio"
        id={id + "Tool"}
        name={id + "miscProf"}
        value="tools"
        defaultChecked={selectorType === "tools" ? true : false}
      />
      <label for={id + "Tool"}>Tool</label>

      <input
        type="radio"
        id={id + "ArtisanTool"}
        name={id + "miscProf"}
        value="artisanTools"
        defaultChecked={selectorType === "artisanTools" ? true : false}
      />
      <label for={id + "ArtisanTool"}>Artisan Tool</label>

      <input
        type="radio"
        id={id + "Instrument"}
        name={id + "miscProf"}
        value="instruments"
        defaultChecked={selectorType === "instruments" ? true : false}
      />
      <label for={id + "Instrument"}>Instrument</label>

      <input
        type="radio"
        id={id + "GameSet"}
        name={id + "miscProf"}
        value="gameSets"
        defaultChecked={selectorType === "gameSets" ? true : false}
      />
      <label for={id + "GameSet"}>Game Set</label>
    </div>
  );
}

function applySelector(selector) {
  if (selector === "tools") {
    return allTools;
  } else if (selector === "languages") {
    return allLanguages;
  } else if (selector === "artisanTools") {
    return allArtisanTools;
  } else if (selector === "instruments") {
    return allInstruments;
  } else if (selector === "gameSets") {
    return allGames;
  }
}

function getAllFeatures(features, chosenFeature) {
  let choices = [];

  let usedFeature = false;

  for (let [key, value] of Object.entries(features)) {
    if (key === chosenFeature) {
      usedFeature = true;
      choices.push(
        <option value={key} selected>
          {key}
        </option>
      );
    } else {
      choices.push(
        <option value={key}>
          {key}
        </option>
      );
    }
  }

  if (!usedFeature) {
    choices.push(
      <option hidden disabled selected value>
        -- select an ancestry --
      </option>
    );
  }

  return choices;
}

function getMiscSelections(choices) {
  let keys = Object.keys(choices);
  let key = keys[0];
  let value = choices[key].pop();
  if (choices[key].length === 0) {
    delete choices[key];
  }
  return [key, value];
}

export default function Background({ backgrounds }) {
  let allBackgrounds = backgrounds.all;
  let choices = structuredClone(backgrounds.choices);
  delete choices.name;

  const [activeFeature, setActiveFeature] = useState(choices.feature);
  delete choices.feature;

  const [skill1, setskill1] = useState(choices.skills[0]);
  const [skill2, setskill2] = useState(choices.skills[1]);
  delete choices.skills;

  let [type, value] = getMiscSelections(choices);
  const [miscSelector1, setmiscSelector1] = useState(type);
  const [misc1, setmisc1] = useState(value);
  let misc1Options = applySelector(miscSelector1);

  [type, value] = getMiscSelections(choices);
  const [miscSelector2, setmiscSelector2] = useState(type);
  const [misc2, setmisc2] = useState(value);
  let misc2Options = applySelector(miscSelector2);

  return (
    <div>
      <h3>Background</h3>
      <label for="backgroundFeature">Feature: </label>
      <select
        name="backgroundFeature"
        id="backgroundFeature"
        onChange={e => setActiveFeature(e.target.value)}
      >
        {getAllFeatures(allBackgrounds, activeFeature)}
      </select>
      <div
        dangerouslySetInnerHTML={{ __html: allBackgrounds[activeFeature] }}
      />
      <div className="backgroundSkills">
        <label>Skills:</label>
        {optionSelector("skill1", setskill1, skill1, skill2, allSkills)}
        {optionSelector("skill2", setskill2, skill2, skill1, allSkills)}
      </div>
      <div className="backgroundMiscProf">
        <label>Misc. Proficiencies</label>
        <div>
          {miscProfSelector("misc1", miscSelector1, setmiscSelector1)}
          {optionSelector("misc1", setmisc1, misc1, misc2, misc1Options)}
          {misc1}
        </div>
        <div>
          {miscProfSelector("misc2", miscSelector2, setmiscSelector2)}
          {optionSelector("misc2", setmisc2, misc2, misc1, misc2Options)}
          {misc2}
        </div>
      </div>
    </div>
  );
}
