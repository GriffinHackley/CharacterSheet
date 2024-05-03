import "../../css/sheet/Consumables.css";

export default function Consumable({ name, consumableInfo }) {
  return (
    <div className="consumable">
      <div className="total">
        <div className="key">Total</div>
        <div className="value">
          {consumableInfo.uses}
        </div>
      </div>
      <div className="remainingConsumable">
        <input name="remainingConsumable" type="text" id="{{ key }}" />

        <label className="consumableLabel" htmlFor="remainingConsumable">
          {name}
        </label>
      </div>
    </div>
  );
}
