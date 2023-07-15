import "../../../css/sheet/main/Consumables.css";

export default function Consumables({ consumableInfo }) {
  let consumables = [];

  for (let consumable in consumableInfo) {
    consumables.push(
      <div key={"consumable-" + consumable}>
        <div className="total">
          <div className="key">Total</div>
          <div className="value">
            {consumableInfo[consumable].uses}
          </div>
        </div>
        <div className="remainingConsumable">
          <input name="remainingConsumable" type="text" id="{{ key }}" />

          <label htmlFor="remainingConsumable">
            {consumable}
          </label>
        </div>
      </div>
    );
  }

  return (
    <section className="consumables">
      {consumables}
    </section>
  );
}
