import "../../../../css/main/combat/HitDice.css";
import { useEffect } from "react";
import { storeItem, getItem } from "../../../../scripts/localState.js";

function handleChange(event) {
  storeItem("remainingHD", charName);
}

let charName = null;

export default function HitDice({ hitDice, config }) {
  charName = config.name;

  //Load value from local storage when component is mounted
  useEffect(() => {
    getItem("remainingHD", charName);
  }, []);
  return (
    <div className="hitDice">
      <div className="totalHD">
        <div className="key">Total Hit Dice</div>
        <div className="value">
          {hitDice}
        </div>
      </div>
      <input type="text" id="remainingHD" onChange={handleChange} />
      <label htmlFor="remainingHD">Hit Dice</label>
    </div>
  );
}
