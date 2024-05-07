import { useState } from "react";
import axios from "axios";
import { Checkbox, FormControlLabel, Paper } from "@mui/material";
import "../../css/sheet/Toggles.css";

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
  let id = target.id;

  activeToggles[id] = value;
  setActive(activeToggles);
}

export default function Toggles({ togglesInfo, setCharacter, id }) {
  const [activeToggles, setActiveToggles] = useState({});

  let display = [];
  for (let toggle in togglesInfo.default) {
    display.push(
      <FormControlLabel
        className="defaultToggles"
        key={toggle}
        control={
          <Checkbox
            id={toggle}
            onChange={e =>
              updateForm(activeToggles, setActiveToggles, e.target)}
          />
        }
        label={toggle}
      />
    );
  }
  for (let toggle in togglesInfo.other) {
    display.push(
      <FormControlLabel
        className="otherToggles"
        key={toggle}
        control={
          <Checkbox
            id={toggle}
            onChange={e =>
              updateForm(activeToggles, setActiveToggles, e.target)}
          />
        }
        label={toggle}
      />
    );
  }

  return (
    <Paper className="toggles">
      <form onSubmit={e => submitForm(e, setCharacter, id, activeToggles)}>
        {display}
        <input type="submit" value="Submit" />
      </form>
    </Paper>
  );
}
