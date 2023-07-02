import "./css/App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

import Header from "./components/Header";
import Attributes from "./components/Attributes";
import Saves from "./components/Saves";
import Skills from "./components/Skills";
import Combat from "./components/Combat";
import Consumables from "./components/Consumables";
import Toggles from "./components/Toggles";
import Inspiration from "./components/Inspiration";
import Proficiency from "./components/Proficiency";
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
          flavorInfo={character.flavor}
        />
      </section>
    );
  }
}

export default App;
