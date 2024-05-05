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
import SideDrawer from "../sheet/SideDrawer.js";
import Features from "../sheet/FeaturesPanel.js";
import FeaturesPanel from "../sheet/FeaturesPanel.js";

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

function initLayout(editMode, id, consumables) {
  let layout = getLayout(id);
  if (layout != null) {
    return layout;
  }

  console.log("Using default layout");
  let ret = [
    {
      i: "combat",
      x: 2,
      y: 0,
      w: 4,
      h: 4,
      minW: 3,
      minH: 4,
      static: !editMode
    },
    {
      i: "attacksandspellcasting",
      x: 2,
      y: 5,
      w: 4,
      h: 2,
      minW: 3,
      minH: 2,
      static: !editMode
    },
    { i: "proficiency", x: 0, y: 0, w: 2, h: 1, static: !editMode },
    { i: "toggles", x: 8, y: 0, w: 2, h: 3, static: !editMode },
    { i: "features", x: 0, y: 0, w: 2, h: 3, static: !editMode }
  ];

  let count = 0;
  for (let consumable in consumables) {
    ret.push({
      i: "consumable-" + consumable,
      x: 1 + count % 2,
      y: 1 + Math.floor(count / 2),
      w: 2,
      h: 1,
      static: !editMode
    });
    count++;
  }

  return ret;
}

function Sheet() {
  const { id } = useParams();
  const [loading, setLoading] = useState(true);
  const [editMode, setEditMode] = useState(false);
  const [character, setCharacter] = useState([]);
  const [layout, setLayout] = useState(initLayout(editMode, id));

  useEffect(
    () => {
      let newLayout = [];

      //Put the array in reverse order because they layout doesnt change enough?
      layout.forEach(value => {
        value["static"] = !editMode;
        newLayout.unshift(value);
      });

      if (!editMode) {
        storeLayout(id, newLayout);
      }

      setLayout([...newLayout]);
    },
    [editMode]
  );

  //Get character data
  useEffect(() => {
    loadCharacter(setLoading, setCharacter, id);
  }, []);

  if (loading) {
    return <h4>Loading...</h4>;
  } else {
    let consumables = [];

    for (let consumable in character.consumables) {
      consumables.push(
        <div key={"consumable-" + consumable}>
          <Consumable
            name={consumable}
            consumableInfo={character.consumables[consumable]}
          />
        </div>
      );
    }

    return (
      <section className="pageContainer">
        <SideDrawer
          id={id}
          character={character}
          editMode={editMode}
          setEditMode={setEditMode}
        />
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
          onLayoutChange={newLayout => {
            setLayout([...newLayout]);
          }}
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
          <div key="features">
            <FeaturesPanel features={character.features} />
          </div>
        </ReactGridLayout>
        <section />
      </section>
    );
  }
}

export default Sheet;
