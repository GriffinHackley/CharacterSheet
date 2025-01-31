import "../../../css/sheet/combat/Resistances.css";
import { useEffect } from "react";
import {
  storeCheckboxValue,
  getCheckboxValue
} from "../../../utils/localState.js";

function handleChange(event) {
  storeCheckboxValue("resistances", charName);
}

let charName = null;

export default function Resistances({ config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getCheckboxValue("resistances", charName);
  }, []);

  return (
    <div className="resistances">
      <textarea id="resistances" onChange={handleChange} />
      <label>Resistances</label>
    </div>
  );
}
