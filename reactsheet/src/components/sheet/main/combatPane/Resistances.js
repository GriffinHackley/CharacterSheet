import "../../../../css/sheet/main/combat/Resistances.css";
import { useEffect } from "react";
import { storeItem, getItem } from "../../../../scripts/localState.js";

function handleChange(event) {
  storeItem("resistances", charName);
}

let charName = null;

export default function Resistances({ config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getItem("resistances", charName);
  }, []);

  return (
    <div className="resistances">
      <textarea id="resistances" onChange={handleChange} />
      <label>Resistances</label>
    </div>
  );
}
