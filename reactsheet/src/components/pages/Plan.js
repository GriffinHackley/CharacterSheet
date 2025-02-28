import axios from "axios";
import { useParams } from "react-router-dom";
import { React, useState, useEffect } from "react";
import Ancestry from "../plan/Ancestry";
import Background from "../plan/Background";
import Stats from "../plan/Stats";
import "../../css/pages/Plan.css";
import Classes from "../plan/Classes";
import setColors from "../../utils/setColors";

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
  "Abyssal",
  "Aquan",
  "Auran",
  "Celestial",
  "DeepSpeech",
  "Draconic",
  "Dwarvish",
  "Elvish",
  "Giant",
  "Gnomish",
  "Goblin",
  "Halfling",
  "Ignan",
  "Infernal",
  "Orc",
  "Sylvan",
  "Terran",
  "Undercommon"
];

const loadPlan = async (setLoading, setPlan, setAncestry, id) => {
  setLoading(true);

  const response = await axios.get(
    `http://127.0.0.1:8000/api/characters/${id}/plan`
  );
  let plan = JSON.parse(response.data);
  setPlan(plan);

  setAncestry(plan[0].races.choice);

  setColors(plan[0].config.accentColors);

  setLoading(false);
};

export default function Plan() {
  const [proficiencyChoices, setProficiencyChoices] = useState({
    skills: {},
    artisanTools: {},
    tools: {},
    gameSets: {},
    instruments: {},
    languages: {}
  });

  const [loading, setLoading] = useState(true);
  const [plan, setPlan] = useState([]);
  const { id } = useParams();
  const [chosenAncestry, setAncestry] = useState(null);

  useEffect(() => {
    loadPlan(setLoading, setPlan, setAncestry, id);
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="planPage">
      <div className="level">
        <h1>Level 0</h1>
        <Stats stats={plan[0].stats} />
        <Ancestry
          allAncestries={plan[0].races.all}
          chosenAncestry={chosenAncestry}
          setAncestry={setAncestry}
          proficiencyChoices={proficiencyChoices}
          setProficiencyChoices={setProficiencyChoices}
          allLanguages={allLanguages}
        />
        <Background
          backgrounds={plan[0].backgrounds}
          proficiencyChoices={proficiencyChoices}
          setProficiencyChoices={setProficiencyChoices}
          allSkills={allSkills}
          allArtisanTools={allArtisanTools}
          allTools={allTools}
          allGames={allGames}
          allInstruments={allInstruments}
          allLanguages={allLanguages}
        />
        <Classes classes={plan[1]} />
      </div>
    </div>
  );
}
