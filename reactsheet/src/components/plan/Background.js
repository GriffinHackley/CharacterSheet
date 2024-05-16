import { useEffect, useState } from "react";
import "../../css/plan/Background.css";
import { MenuItem, Select } from "@mui/material";
import ExclusiveSelector from "../shared/ExclusiveSelector";

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

  for (let key of Object.keys(features)) {
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

  const [skill1, setSkill1] = useState(choices.skills[0]);
  const [skill2, setSkill2] = useState(choices.skills[1]);

  delete choices.skills;

  let [type, value] = getMiscSelections(choices);
  const [miscSelector1, setmiscSelector1] = useState(type);
  const [misc1, setMisc1] = useState(value);

  let [misc1Options, setMisc1Options] = useState(
    applySelector(
      miscSelector1,
      allTools,
      allArtisanTools,
      allLanguages,
      allInstruments,
      allGames
    )
  );

  [type, value] = getMiscSelections(choices);
  const [miscSelector2, setmiscSelector2] = useState(type);
  const [misc2, setMisc2] = useState(value);
  let [misc2Options, setMisc2Options] = useState(
    applySelector(
      miscSelector2,
      allTools,
      allArtisanTools,
      allLanguages,
      allInstruments,
      allGames
    )
  );

  useEffect(
    () => {
      let allOptions = applySelector(
        miscSelector1,
        allTools,
        allArtisanTools,
        allLanguages,
        allInstruments,
        allGames
      );

      if (!allOptions.includes(misc1)) {
        setMisc1("none");
      }
      setMisc1Options(allOptions);
    },
    [miscSelector1]
  );

  useEffect(
    () => {
      let allOptions = applySelector(
        miscSelector2,
        allTools,
        allArtisanTools,
        allLanguages,
        allInstruments,
        allGames
      );

      if (!allOptions.includes(misc2)) {
        setMisc2("none");
      }
      setMisc2Options(allOptions);
    },
    [miscSelector2]
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
        <ExclusiveSelector
          name="skill"
          type="skills"
          currentChoice={skill1}
          setCurrentChoice={setSkill1}
          proficiencyChoices={proficiencyChoices}
          setProficiencyChoices={setProficiencyChoices}
          allChoices={allSkills}
          index={0}
        />
        <ExclusiveSelector
          name="skill"
          type="skills"
          currentChoice={skill2}
          setCurrentChoice={setSkill2}
          proficiencyChoices={proficiencyChoices}
          setProficiencyChoices={setProficiencyChoices}
          allChoices={allSkills}
          index={1}
        />
      </div>
      <div className="backgroundMiscProf">
        <label>Misc. Proficiencies</label>
        <div>
          {miscProfSelector("misc1", miscSelector1, setmiscSelector1)}
          <ExclusiveSelector
            name="misc"
            type={miscSelector1}
            currentChoice={misc1}
            setCurrentChoice={setMisc1}
            proficiencyChoices={proficiencyChoices}
            setProficiencyChoices={setProficiencyChoices}
            allChoices={misc1Options}
            index={0}
          />
        </div>
        <div>
          {miscProfSelector("misc2", miscSelector2, setmiscSelector2)}
          <ExclusiveSelector
            name="misc"
            type={miscSelector2}
            currentChoice={misc2}
            setCurrentChoice={setMisc2}
            proficiencyChoices={proficiencyChoices}
            setProficiencyChoices={setProficiencyChoices}
            allChoices={misc2Options}
            index={1}
          />
        </div>
      </div>
    </div>
  );
}
