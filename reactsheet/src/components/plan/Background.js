import { useState } from "react";
import "../../css/plan/Background.css";

function displayContent(feature) {
  if (feature == "") {
    return;
  }
  let text = [];
  feature.forEach(line => {
    if (line.type == "normal") {
      text.push(
        <p>
          {line.text}
        </p>
      );
    } else if (line.type == "heading") {
      text.push(
        <h4>
          {line.text}
        </h4>
      );
    } else if (line.type == "table") {
      text.push(<h1>Tables have not been implemented</h1>);
    }
  });
  return (
    <div>
      {text}
    </div>
  );
}

function optionSelector(id, setOption, currentOption, otherOption, allOptions) {
  let options = [];
  options.push(
    <option hidden disabled selected value>
      -- select an option --
    </option>
  );

  //   Dont let them choose the same option as the other selector
  allOptions = allOptions.filter(option => option != otherOption);

  for (let option in allOptions) {
    let isSelected = false;
    if (currentOption == allOptions[option]) {
      isSelected = true;
    }
    options.push(
      <option selected={isSelected}>
        {allOptions[option]}
      </option>
    );
  }
  return (
    <select name={id} id={id} onChange={e => setOption(e.target.value)}>
      {options}
    </select>
  );
}

function toolOrLanguageSelector(id, setSelector) {
  return (
    <div onChange={e => setSelector(e.target.value)}>
      <input
        type="radio"
        id={id + "Language"}
        name={id + "LanguageOrTool"}
        value="language"
        defaultChecked
      />
      <label for={id + "Language"}>Language</label>
      <input
        type="radio"
        id={id + "Tool"}
        name={id + "LanguageOrTool"}
        value="tool"
      />
      <label for={id + "Tool"}>Tool</label>
    </div>
  );
}

export default function Background({ backgrounds }) {
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

  let allTools = [
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
    "Woodcarver's tools",
    "Dice set",
    "Dragonchess set",
    "Playing card set",
    "Three-Dragon Ante set",
    "Bagpipes",
    "Drum",
    "Dulcimer",
    "Flute",
    "Lute",
    "Lyre",
    "Horn",
    "Pan flute",
    "Shawm",
    "Viol",
    "Disguise kit",
    "Forgery kit",
    "Herbalism kit",
    "Navigator's tools",
    "Poisoner's kit",
    "Thieves' tools"
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

  let features = [];

  features.push(
    <option hidden disabled selected value>
      -- select an option --
    </option>
  );

  for (let background in backgrounds) {
    features.push(
      <option value={background}>
        {background}
      </option>
    );
  }

  const [activeFeature, setActiveFeature] = useState("none");
  let featureText = "";

  if (activeFeature != "none") {
    featureText = displayContent(backgrounds[activeFeature]);
  }

  const [skill1, setskill1] = useState("none");
  const [skill2, setskill2] = useState("none");
  const [miscSelector1, setmiscSelector1] = useState("language");
  const [miscSelector2, setmiscSelector2] = useState("language");
  const [misc1, setmisc1] = useState("none");
  const [misc2, setmisc2] = useState("none");

  let misc1Options = [];
  if (miscSelector1 == "tool") {
    misc1Options = allTools;
  } else if (miscSelector1 == "language") {
    misc1Options = allLanguages;
  }

  let misc2Options = [];
  if (miscSelector2 == "tool") {
    misc2Options = allTools;
  } else if (miscSelector2 == "language") {
    misc2Options = allLanguages;
  }

  return (
    <div>
      <h3>Background</h3>
      <label for="backgroundFeature">Feature: </label>
      <select
        name="backgroundFeature"
        id="backgroundFeature"
        onChange={e => setActiveFeature(e.target.value)}
      >
        {features}
      </select>
      <div>
        {featureText}
      </div>
      <div className="backgroundSkills">
        <label>Skills:</label>
        {optionSelector("skill1", setskill1, skill1, skill2, allSkills)}
        {optionSelector("skill2", setskill2, skill2, skill1, allSkills)}
      </div>
      <div className="backgroundMiscProf">
        <label>Misc. Proficiencies</label>
        <div>
          {/* TODO: It is possible to get duplicate entries by switching between language and tools */}
          {toolOrLanguageSelector("misc1", setmiscSelector1)}
          {optionSelector("misc1", setmisc1, misc1, misc2, misc1Options)}
          {misc1}
        </div>
        <div>
          {toolOrLanguageSelector("misc2", setmiscSelector2)}
          {optionSelector("misc2", setmisc2, misc2, misc1, misc2Options)}
          {misc2}
        </div>
      </div>
    </div>
  );
}
