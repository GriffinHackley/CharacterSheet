import { Paper } from "@mui/material";
import "../../css/sheet/Consumables.css";

export default function Consumable({ name, consumableInfo }) {
  return (
    <Paper className="consumable">
      <div className="total">
        <div className="key">Total</div>
        <div className="value">
          {consumableInfo.uses}
        </div>
      </div>
      <div className="remainingConsumable">
        <input name="remainingConsumable" type="text" />
        <label className="consumableLabel" htmlFor="remainingConsumable">
          {name}
        </label>
      </div>
    </Paper>
  );
}
