import { useState } from "react";
import axios from "axios";

function submitForm(e, setCharacter, id, toggles) {
  e.preventDefault();
  loadCharacter(setCharacter, id, toggles);
}

const loadCharacter = async (setCharacter, id, toggles) => {
  const response = await axios.post(
    "http://127.0.0.1:8000/api/characters/toggles/" + id,
    toggles
  );

  let character = JSON.parse(response.data);
  setCharacter(character);
};

function updateForm(toggles, target) {
  let value = target.checked;
  let name = target.name;

  toggles[name] = value;
}

export default function Toggles({ togglesInfo, setCharacter, id }) {
  const [toggles, setToggles] = useState(togglesInfo);

  let display = [];
  for (let toggle in togglesInfo) {
    display.push(
      <div>
        <label>
          {toggle}
        </label>
        <input
          type="checkbox"
          id={toggle}
          name={toggle}
          onChange={e => updateForm(toggles, e.target)}
        />
      </div>
    );
  }

  return (
    <section className="toggles">
      <form onSubmit={e => submitForm(e, setCharacter, id, toggles)}>
        {display}
        <input type="submit" value="Submit" />
      </form>
    </section>
  );
}
