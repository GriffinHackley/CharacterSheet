import "./css/App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

import Header from "./components/sheet/main/Header";
import Attributes from "./components/sheet/main/Attributes";
import Saves from "./components/sheet//main/Saves";
import Skills from "./components/sheet//main/Skills";
import Combat from "./components/sheet//main/combatPane/Combat";
import Consumables from "./components/sheet//main/Consumables";
import Toggles from "./components/sheet//main/Toggles";
import Inspiration from "./components/sheet/main/Inspiration";
import Proficiency from "./components/sheet/main/Proficiency";
import FlexPanel from "./components/sheet/flexPanel/FlexPanel";
import { useParams } from "react-router-dom";

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
    "http://127.0.0.1:8000/api/characters/" + id + "/level"
  );
  let character = JSON.parse(response.data);
  setCharacter(character);

  setLoading(false);
  setColor(character.config.accentColors);
};

function Sheet() {
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
    return (
      <section className="pageContainer">
        <section>
          <Header headerInfo={character.header} />
        </section>
        <main>
          <Attributes attributesInfo={character.attributes} />
          <section className="attr-applications">
            <Inspiration />
            <Proficiency />
            <Saves savesInfo={character.saves} />
            <Skills skillsInfo={character.skills} />
          </section>

          <Combat combatInfo={character.combat} />

          <section className="rightPane">
            <Consumables consumableInfo={character.consumables} />
            <Toggles />
          </section>
        </main>
        <FlexPanel
          config={character.config}
          featureInfo={character.features}
          equipmentInfo={character.equipment}
          profInfo={character.proficiencies}
          spellInfo={character.spells}
          graphInfo={character.graph}
          flavorInfo={character.flavor}
        />
      </section>
    );
  }
}

export default Sheet;
