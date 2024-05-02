import "../../css/App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import Header from "../sheet/Header";
import Combat from "../sheet/combatPane/Combat";
import Consumables from "../sheet/Consumables";
import Toggles from "../sheet/Toggles";
import Proficiency from "../sheet/Proficiency";
import { useParams } from "react-router-dom";
import Attributes from "../sheet/Attributes";
import Passives from "../sheet/Passives";

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
        <Attributes
          attributesInfo={character.attributes}
          skillsInfo={character.skills}
          savesInfo={character.saves}
        />
        <main>
          <section className="passivesAndProficiencies">
            <Proficiency />
            <Passives skillsInfo={character.skills} />
          </section>

          <Combat combatInfo={character.combat} />

          <section className="rightPane">
            <Consumables consumableInfo={character.consumables} />
            <Toggles
              togglesInfo={character.toggles}
              setCharacter={setCharacter}
              id={id}
            />
          </section>
        </main>
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
