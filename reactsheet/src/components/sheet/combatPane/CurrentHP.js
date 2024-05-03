import "../../../css/sheet/combat/CurrentHP.css";
import { useEffect, useState } from "react";
import {
  storeCheckboxValue,
  getCheckboxValue
} from "../../../scripts/localState.js";

function handleChange(event) {
  storeCheckboxValue("currentHealth   ", charName);
}

let charName = null;

export default function CurrentHP({ HP, config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getCheckboxValue("currentHealth", charName);
  }, []);
  return (
    <div className="current">
      <div className="maxHP">
        <div className="key">Max Hit Points</div>
        <div className="value">
          {HP}
        </div>
      </div>
      <input type="text" id="currentHealth" onChange={handleChange} />
      <label>Current Hit Points</label>
    </div>
  );
}
