import "../../css/main/Consumables.css";

export default function Consumables({ consumableInfo }) {
  let consumables = [];

  consumableInfo.forEach(element => {
    consumables.push(
      <div key={"consumable-" + element.name}>
        <div className="total">
          <div className="key">Total</div>
          <div className="value">
            {element.number}
          </div>
        </div>
        <div className="remainingConsumable">
          <input name="remainingConsumable" type="text" id="{{ key }}" />

          <label htmlFor="remainingConsumable">
            {element.name}
          </label>
        </div>
      </div>
    );
  });
  return (
    <section className="consumables">
      {consumables}
    </section>
  );
}
