import { useState } from "react";
import axios from "axios";

function submitForm(e, setCharacter, id, activeToggles) {
  e.preventDefault();
  loadCharacter(setCharacter, id, activeToggles);
}

const loadCharacter = async (setCharacter, id, toggles) => {
  const response = await axios.post(
    "http://127.0.0.1:8000/api/characters/toggles/" + id,
    toggles
  );

  let character = JSON.parse(response.data);
  setCharacter(character);
};

function updateForm(activeToggles, setActive, target) {
  let value = target.checked;
  let name = target.name;

  activeToggles[name] = value;
  setActive(activeToggles);
}

export default function Toggles({ togglesInfo, setCharacter, id }) {
  const [toggles, setToggles] = useState(togglesInfo);
  const [activeToggles, setActiveToggles] = useState({});

  let display = [];
  for (let toggle in togglesInfo.default) {
    display.push(
      <div className="defaultToggles">
        <label>
          {toggle}
        </label>
        <input
          type="checkbox"
          id={toggle}
          name={toggle}
          onChange={e => updateForm(activeToggles, setActiveToggles, e.target)}
        />
      </div>
    );
  }
  for (let toggle in togglesInfo.other) {
    display.push(
      <div className="otherToggles">
        <label>
          {toggle}
        </label>
        <input
          type="checkbox"
          id={toggle}
          name={toggle}
          onChange={e => updateForm(activeToggles, setActiveToggles, e.target)}
        />
      </div>
    );
  }

  return (
    <section className="toggles">
      <form onSubmit={e => submitForm(e, setCharacter, id, activeToggles)}>
        {display}
        <input type="submit" value="Submit" />
      </form>
    </section>
  );
}
