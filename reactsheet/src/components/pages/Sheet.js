import "../../css/App.css";
import "../../../node_modules/react-grid-layout/css/styles.css";

import axios from "axios";
import { Link, useParams } from "react-router-dom";
import React, { useState, useEffect } from "react";
import RGL, { WidthProvider } from "react-grid-layout";
import { getLayout, storeLayout } from "../../scripts/localState.js";

import Header from "../sheet/Header";
import Toggles from "../sheet/Toggles";
import Passives from "../sheet/Passives";
import Attributes from "../sheet/Attributes";
import Proficiency from "../sheet/Proficiency";
import Consumable from "../sheet/Consumable";
import Combat from "../sheet/combatPane/Combat";
import AttacksAndSpellcasting from "../sheet/combatPane/AttacksAndSpellcasting";

const ReactGridLayout = WidthProvider(RGL);

function setColor(colors) {
  let primary = colors[0];
  let secondary = colors[1];
  let root = document.documentElement;

  root.style.setProperty("--primary-accent", primary);
  root.style.setProperty("--secondary-accent", secondary);
}

const loadCharacter = async (setLoading, setCharacter, id) => {
  setLoading(true);

  const response = await axios.get(
    "http://127.0.0.1:8000/api/characters/" + id
  );
  let character = JSON.parse(response.data);
  setCharacter(character);

  setLoading(false);
  setColor(character.config.accentColors);
};

function initLayout(locked, name) {
  let layout = getLayout(name);
  if (layout) {
    return layout;
  }

  return [
    { i: "combat", x: 2, y: 0, w: 4, h: 4, minW: 3, static: locked },
    {
      i: "attacksandspellcasting",
      x: 2,
      y: 0,
      w: 4,
      h: 2,
      minW: 3,
      minH: 2,
      static: locked
    },
    { i: "proficiency", x: 0, y: 0, w: 2, h: 1, static: locked },
    { i: "toggles", x: 8, y: 0, w: 2, h: 3, static: locked }
  ];
}

function Sheet() {
  const locked = false;
  const [loading, setLoading] = useState(true);
  const [character, setCharacter] = useState([]);
  const { id } = useParams();

  //Get character data
  useEffect(() => {
    loadCharacter(setLoading, setCharacter, id);
  }, []);

  if (loading) {
    return <h4>Loading...</h4>;
  } else {
    const layout = initLayout(locked, character.header["Character Name"]);
    let consumables = [];
    let count = 0;
    for (let consumable in character.consumables) {
      consumables.push(
        <div
          key={"consumable-" + consumable}
          data-grid={{
            x: count % 2,
            y: 1 + Math.floor(count / 2),
            w: 1,
            h: 1,
            static: locked
          }}
        >
          <Consumable
            name={consumable}
            consumableInfo={character.consumables[consumable]}
          />
        </div>
      );
      count++;
    }

    return (
      <section className="pageContainer">
        <Header headerInfo={character.header} />
        <Attributes
          key="attributes"
          attributesInfo={character.attributes}
          skillsInfo={character.skills}
          savesInfo={character.saves}
        />
        <ReactGridLayout
          className="layout"
          layout={layout}
          cols={12}
          rowHeight={100}
          onLayoutChange={layout =>
            storeLayout(character.header["Character Name"], layout)}
        >
          <div key="proficiency">
            <Proficiency />
            <Passives skillsInfo={character.skills} />
          </div>
          {consumables}
          <div key="combat">
            <Combat combatInfo={character.combat} />
          </div>
          <div key="attacksandspellcasting">
            <AttacksAndSpellcasting
              attacks={character.combat.Attacks}
              config={character.combat.config}
            />
          </div>
          <div key="toggles">
            <Toggles
              togglesInfo={character.toggles}
              setCharacter={setCharacter}
              id={id}
            />
          </div>
        </ReactGridLayout>
        <section />
        <Link
          to={`/character/${id}/features/`}
          state={{ featuresInfo: character.features }}
        >
          Features
        </Link>
        <Link
          to={`/character/${id}/equipment/`}
          state={{ equipmentInfo: character.equipment }}
        >
          Equipment
        </Link>
        <Link
          to={`/character/${id}/spells/`}
          state={{ spellInfo: character.spells, config: character.config }}
        >
          Spells
        </Link>
        <Link
          to={`/character/${id}/flavor/`}
          state={{ flavorInfo: character.flavor }}
        >
          Flavor
        </Link>
        {/* <FlexPanel
          config={character.config}
          featureInfo={character.features}
          equipmentInfo={character.equipment}
          profInfo={character.proficiencies}
          spellInfo={character.spells}
          graphInfo={character.graph}
          flavorInfo={character.flavor}
        /> */}
      </section>
    );
  }
}

export default Sheet;
