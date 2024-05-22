import "../../css/App.css";
import "../../../node_modules/react-grid-layout/css/styles.css";

import axios from "axios";
import { useParams } from "react-router-dom";
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
import FeaturesPanel from "../sheet/FeaturesPanel.js";
import { ThemeProvider, createTheme } from "@mui/material";
import { blue, purple } from "@mui/material/colors";

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

  const response = await axios
    .get("http://127.0.0.1:8000/api/characters/" + id)
    .catch(function(error) {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        throw error.response.data;
      } else if (error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
        // http.ClientRequest in node.js
        throw error.request;
      } else {
        // Something happened in setting up the request that triggered an Error
        throw error.message;
      }
    });
  let character = JSON.parse(response.data);
  setCharacter(character);

  setLoading(false);
  setColor(character.config.accentColors);
  return character;
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
      x: 6,
      y: 0,
      w: 4,
      h: 6,
      minW: 3,
      minH: 6,
      static: !editMode
    },
    {
      i: "attacksandspellcasting",
      x: 6,
      y: 6,
      w: 4,
      h: 4,
      minW: 3,
      minH: 4,
      static: !editMode
    },
    { i: "proficiency", x: 10, y: 0, w: 2, h: 1, minW: 2, static: !editMode },
    { i: "passives", x: 10, y: 1, w: 2, h: 2, minH: 2, static: !editMode },
    {
      i: "toggles",
      x: 10,
      y: 5,
      w: 2,
      h: 5,
      minW: 2,
      minH: 3,
      static: !editMode
    },
    { i: "features", x: 0, y: 0, w: 6, h: 6, static: !editMode }
  ];

  let count = 0;
  for (let consumable in consumables) {
    ret.push({
      i: "consumable-" + consumable,
      x: 10 + count % 2,
      y: 3 + Math.floor(count / 2),
      w: 1,
      h: 2,
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
  const [layout, setLayout] = useState(
    initLayout(editMode, id, character.consumables)
  );

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
    let temp = loadCharacter(setLoading, setCharacter, id);
    setLayout(initLayout(editMode, id, temp.consumables));
  }, []);

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
