import "../../css/App.css";
import "../../../node_modules/react-grid-layout/css/styles.css";

import { useParams } from "react-router-dom";
import React, { useState, useEffect } from "react";
import RGL, { WidthProvider } from "react-grid-layout";
import { getLayout, storeLayout } from "../../utils/localState.js";

import Header from "../sheet/Header";
import Toggles from "../sheet/Toggles";
import Passives from "../sheet/Passives";
import Attributes from "../sheet/Attributes";
import Proficiency from "../sheet/Proficiency";
import Consumable from "../sheet/Consumable";
import Combat from "../sheet/combatPane/Combat";
import AttacksAndSpellcasting from "../sheet/combatPane/AttacksAndSpellcasting";
import SideDrawer from "../sheet/SideDrawer.js";
import FeaturesPanel from "../sheet/FeaturesPanel.js";
import { ThemeProvider, createTheme } from "@mui/material";
import defaultLayout from "../../layouts/defaultLayout.js";
import { makeRequest } from "../../utils/api.js";

const ReactGridLayout = WidthProvider(RGL);

function setColor(colors) {
  let primary = colors[0];
  let secondary = colors[1];
  let root = document.documentElement;

  root.style.setProperty("--primary-accent", primary);
  root.style.setProperty("--secondary-accent", secondary);
}

function loadCharacter(setLoading, setCharacter, setLayout, id) {
  setLoading(true);

  let url = "http://127.0.0.1:8000/api/characters/" + id;

  makeRequest(url).then(character => {
    setCharacter(character);
    setColor(character.config.accentColors);
    setLayout(initLayout(false, id, character));
    setLoading(false);
  });
}

function initLayout(editMode, id, character) {
  if (!character) {
    return null;
  }

  let layout = getLayout(id);

  if (layout != null) {
    console.log("Setting custom layout");
    return layout;
  }

  console.log("Setting layout to default");
  return defaultLayout(editMode, character);
}

function Sheet() {
  const { id } = useParams();
  const [loading, setLoading] = useState(true);
  const [editMode, setEditMode] = useState(false);
  const [character, setCharacter] = useState(null);
  const [layout, setLayout] = useState(initLayout(editMode, character));

  useEffect(
    () => {
      if (layout == null) {
        return;
      }
      let newLayout = [];

      //Put the array in reverse order because the layout doesnt change enough?
      layout.forEach(value => {
        value["static"] = !editMode;
        newLayout.unshift(value);
      });

      if (!editMode) {
        storeLayout(id, newLayout);
      }

      console.log("Setting custom layout");
      setLayout([...newLayout]);
    },
    [editMode, id]
  );

  //Get character data
  useEffect(
    () => {
      loadCharacter(setLoading, setCharacter, setLayout, id);
    },
    [id]
  );

  if (loading) {
    return <h4>Loading...</h4>;
  } else {
    const theme = createTheme({
      components: {
        MuiPaper: {
          styleOverrides: {
            root: {
              border: `3px solid ${character.config.accentColors[1]}`,
              backgroundColor: character.config.accentColors[0],
              borderRadius: "10px",
              height: "100%"
            }
          }
        }
      }
      // palette: {
      //   primary: purple,
      //   secondary: purple
      // }
    });

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
      <ThemeProvider theme={theme}>
        <section>
          <SideDrawer
            id={id}
            character={character}
            editMode={editMode}
            setEditMode={setEditMode}
            setLayout={setLayout}
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
            rowHeight={50}
            onLayoutChange={newLayout => {
              console.log("Setting custom layout");
              setLayout([...newLayout]);
            }}
          >
            <div key="proficiency">
              <Proficiency />
            </div>
            <div key="passives">
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
                setResponse={setCharacter}
                url={"http://127.0.0.1:8000/api/characters/toggles/" + id}
                id={id}
              />
            </div>
            <div key="features">
              <FeaturesPanel features={character.features} />
            </div>
          </ReactGridLayout>
          <section />
        </section>
      </ThemeProvider>
    );
  }
}

export default Sheet;
