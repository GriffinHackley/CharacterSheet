import formatSource from "../../../../scripts/formatSource";

export default function AttacksAndSpellcasting({ attacks, config }) {
  let rows = [];
  let critRangeHeader = null;
  let critRangeBody = null;
  let includeCrit = false;

  if (config == "Pathfinder") {
    includeCrit = true;
  }

  if (includeCrit) {
    critRangeHeader = <th>Crit Range</th>;
  }

  attacks.forEach(element => {
    if (includeCrit) {
      critRangeBody = (
        <td>
          <div className="critRange">
            {element.critRange}/x{element.critDamage}
          </div>
        </td>
      );
    }
    rows.push(
      <tr key={"attack-" + element.name}>
        <td>
          <div className="atk">
            {element.name}
          </div>
        </td>
        {critRangeBody}
        <td>
          <div
            className="tooltip centered toHit"
            data-tooltip={formatSource(element.toHit.source)}
          >
            +{element.toHit.value}
          </div>
        </td>
        <td>
          <div
            className="tooltip centered damage"
            data-tooltip={formatSource(element.damage.source)}
          >
            {element.damage.value}
          </div>
        </td>
      </tr>
    );
  });

  return (
    <div>
      <label>Attacks & Spellcasting</label>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            {critRangeHeader}
            <th>Atk Bonus</th>
            <th>Damage/Type</th>
          </tr>
        </thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    </div>
  );
}
