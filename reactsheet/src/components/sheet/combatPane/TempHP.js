import "../../../css/sheet/combat/TempHP.css";
import { useEffect } from "react";
import {
  storeCheckboxValue,
  getCheckboxValue
} from "../../../scripts/localState.js";

function handleChange(event) {
  storeCheckboxValue("temphp", charName);
}

let charName = null;

export default function TempHP({ config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getCheckboxValue("temphp", charName);
  }, []);

  return (
    <div className="temporary">
      <input type="text" id="temphp" onChange={handleChange} />
      <label htmlFor="temphp">Temporary Hit Points</label>
    </div>
  );
}
