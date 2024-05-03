import "../../../css/sheet/combat/Conditions.css";
import { useEffect } from "react";
import {
  storeCheckboxValue,
  getCheckboxValue
} from "../../../scripts/localState.js";

function handleChange(event) {
  storeCheckboxValue("conditions", charName);
}

let charName = null;

export default function Conditions({ config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getCheckboxValue("conditions", charName);
  }, []);

  return (
    <div className="conditions">
      <textarea id="conditions" onChange={handleChange} />

      <label>Conditions</label>
    </div>
  );
}
