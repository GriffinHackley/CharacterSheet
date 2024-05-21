import { useState } from "react";
import axios from "axios";
import { Checkbox, FormControlLabel, Paper } from "@mui/material";
import "../../css/sheet/Toggles.css";

function submitForm(e, setCharacter, id, activeToggles) {
  e.preventDefault();
  loadCharacter(setCharacter, id, activeToggles);
}

const loadCharacter = async (setCharacter, id, toggles) => {
  const response = await axios
    .post("http://127.0.0.1:8000/api/characters/toggles/" + id, toggles)
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
