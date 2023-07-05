import "./css/App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

import Header from "./components/main/Header";
import Attributes from "./components/main/Attributes";
import Saves from "./components/main/Saves";
import Skills from "./components/main/Skills";
import Combat from "./components/main/combatPane/Combat";
import Consumables from "./components/main/Consumables";
import Toggles from "./components/main/Toggles";
import Inspiration from "./components/main/Inspiration";
import Proficiency from "./components/main/Proficiency";
import FlexPanel from "./components/flexPanel/FlexPanel";

function setColor(primary, secondary) {
  let root = document.documentElement;

  root.style.setProperty("--primary-accent", primary);
  root.style.setProperty("--secondary-accent", secondary);
}

function App() {
  const [loading, setLoading] = useState(true);
  const [character, setCharacter] = useState([]);

  //Get character data
  useEffect(() => {
    const loadCharacter = async () => {
      setLoading(true);

      const response = await axios.get(
        "http://127.0.0.1:8000/api/characters/51"
      );
      setCharacter(JSON.parse(response.data));
      //   console.log(response.data);

      setLoading(false);
    };

    loadCharacter();
  }, []);

  setColor("blue", "red");

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
          profInfo={character.proficiencies}
          spellInfo={character.spells}
          graphInfo={character.graph}
          flavorInfo={character.flavor}
        />
      </section>
    );
  }
}

export default App;
