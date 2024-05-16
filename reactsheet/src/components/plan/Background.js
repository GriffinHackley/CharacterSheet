import { useEffect, useState } from "react";
import "../../css/plan/Background.css";
import { MenuItem, Select } from "@mui/material";
import Selector from "../shared/Selector";

function optionSelector(id, setOption, currentOption, otherOption, allOptions) {
  //   Dont let them choose the same option as the other selector
  allOptions = allOptions.filter(option => option !== otherOption);
  let selected = currentOption;

  let options = allOptions.map(option => {
    return (
      <option key={option}>
        {option}
      </option>
    );
  });

  options.push(
    <option hidden disabled value key={"defaultOption"}>
      -- select an option --
    </option>
  );

  if (currentOption === "none") {
    selected = "defaultOption";
  }
  return (
    <select
      name={id}
      id={id}
      onChange={e => setOption(e.target.value)}
      value={selected}
    >
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
      <label htmlFor={id + "Language"}>Language</label>

      <input
        type="radio"
        id={id + "Tool"}
        name={id + "miscProf"}
        value="tools"
        defaultChecked={selectorType === "tools" ? true : false}
      />
      <label htmlFor={id + "Tool"}>Tool</label>

      <input
        type="radio"
        id={id + "ArtisanTool"}
        name={id + "miscProf"}
        value="artisanTools"
        defaultChecked={selectorType === "artisanTools" ? true : false}
      />
      <label htmlFor={id + "ArtisanTool"}>Artisan Tool</label>

      <input
        type="radio"
        id={id + "Instrument"}
        name={id + "miscProf"}
        value="instruments"
        defaultChecked={selectorType === "instruments" ? true : false}
      />
      <label htmlFor={id + "Instrument"}>Instrument</label>

      <input
        type="radio"
        id={id + "GameSet"}
        name={id + "miscProf"}
        value="gameSets"
        defaultChecked={selectorType === "gameSets" ? true : false}
      />
      <label htmlFor={id + "GameSet"}>Game Set</label>
    </div>
  );
}

function applySelector(
  selector,
  allTools,
  allArtisanTools,
  allLanguages,
  allInstruments,
  allGames
) {
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
        <option value={key} key={key}>
          {key}
        </option>
      );
    } else {
      choices.push(
        <option value={key} key={key}>
          {key}
        </option>
      );
    }
  }

  if (!usedFeature) {
    choices.push(
      <option hidden disabled value key={"defaultAncestry"}>
        -- select an ancestry --
      </option>
    );
  }

  return choices;
}

function getMiscSelections(choices) {
  if (Object.keys(choices).length == 0) {
    throw "Could not find Misc. Selection";
  }
  let keys = Object.keys(choices);
  let key = keys[0];
  let value = choices[key].pop();
  if (choices[key].length === 0) {
    delete choices[key];
  }
  return [key, value];
}

function onTestSkillSelect(
  e,
  proficiencyChoices,
  setProficiencyChoices,
  setCurrentChoice,
  id
) {
  proficiencyChoices.skills[id] = e.target.value;
  setProficiencyChoices(proficiencyChoices);
  setCurrentChoice(e.target.value);
}

function getSkillSelector(
  currentChoice,
  setCurrentChoice,
  proficiencyChoices,
  setProficiencyChoices,
  allSkills,
  index
) {
  let id = "backgroundSkill-" + index;

  //   Filter out all entries that are already being used
  let filterSkills = [];
  for (const [key, skill] of Object.entries(proficiencyChoices.skills)) {
    if (key !== id) {
      filterSkills.push(skill);
    }
  }

  if (proficiencyChoices.skills[id] !== currentChoice) {
    proficiencyChoices.skills[id] = currentChoice;
    setProficiencyChoices(structuredClone(proficiencyChoices));
  }

  return (
    <Select
      id={id}
      key={id}
      value={currentChoice}
      onChange={e =>
        onTestSkillSelect(
          e,
          proficiencyChoices,
          setProficiencyChoices,
          setCurrentChoice,
          id
        )}
    >
      {allSkills.map(skill => {
        let disabled = filterSkills.includes(skill);

        return (
          <MenuItem disabled={disabled} key={id + skill} value={skill}>
            {skill}
          </MenuItem>
        );
      })}
    </Select>
  );
}

export default function Background({
  backgrounds,
  proficiencyChoices,
  setProficiencyChoices,
  allSkills,
  allTools,
  allArtisanTools,
  allGames,
  allInstruments,
  allLanguages
}) {
  let allBackgrounds = backgrounds.all;
  let choices = structuredClone(backgrounds.choices);
  delete choices.name;

  const [activeFeature, setActiveFeature] = useState(choices.feature);
  delete choices.feature;

  const [skill1, setskill1] = useState(choices.skills[0]);
  const [skill2, setskill2] = useState(choices.skills[1]);

  let skillSelector1 = getSkillSelector(
    skill1,
    setskill1,
    proficiencyChoices,
    setProficiencyChoices,
    allSkills,
    0
  );

  let skillSelector2 = getSkillSelector(
    skill2,
    setskill2,
    proficiencyChoices,
    setProficiencyChoices,
    allSkills,
    1
  );

  //   const [skill1, setskill1] = useState(choices.skills[0]);
  //   const [skill2, setskill2] = useState(choices.skills[1]);
  delete choices.skills;

  let [type, value] = getMiscSelections(choices);
  const [miscSelector1, setmiscSelector1] = useState(type);
  const [misc1, setmisc1] = useState(value);
  let misc1Options = applySelector(
    miscSelector1,
    allTools,
    allArtisanTools,
    allLanguages,
    allInstruments,
    allGames
  );

  [type, value] = getMiscSelections(choices);
  const [miscSelector2, setmiscSelector2] = useState(type);
  const [misc2, setmisc2] = useState(value);
  let misc2Options = applySelector(
    miscSelector2,
    allTools,
    allArtisanTools,
    allLanguages,
    allInstruments,
    allGames
  );

  return (
    <div>
      <h3>Background</h3>
      <label htmlFor="backgroundFeature">Feature: </label>
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
        {skillSelector1}
        {skillSelector2}
        {/* {optionSelector("skill1", setskill1, skill1, skill2, allSkills)}
        {optionSelector("skill2", setskill2, skill2, skill1, allSkills)} */}
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
