import "../../../css/main/combat/TempHP.css";
import { useEffect } from "react";
import { storeItem, getItem } from "../../../scripts/localState.js";

function handleChange(event) {
  storeItem("temphp", charName);
}

let charName = null;

export default function TempHP({ config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getItem("temphp", charName);
  }, []);
  return (
    <div className="temporary">
      <input type="text" id="temphp" onChange={handleChange} />
      <label htmlFor="temphp">Temporary Hit Points</label>
    </div>
  );
}
