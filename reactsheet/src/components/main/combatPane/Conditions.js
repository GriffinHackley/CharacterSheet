import "../../../css/Conditions.css";
import { useEffect } from "react";
import { storeItem, getItem } from "../../../scripts/localState.js";

function handleChange(event) {
  storeItem("conditions", charName);
}

let charName = null;

export default function Conditions({ config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getItem("conditions", charName);
  }, []);

  return (
    <div className="conditions">
      <textarea id="conditions" onChange={handleChange} />

      <label>Conditions</label>
    </div>
  );
}
