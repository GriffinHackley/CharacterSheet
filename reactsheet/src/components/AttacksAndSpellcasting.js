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
          <div class="critRange">
            {element.critRange}/x{element.critDamage}
          </div>
        </td>
      );
    }
    rows.push(
      <tr>
        <td>
          <div class="atk">
            {element.name}
          </div>
        </td>
        {critRangeBody}
        <td>
          <div class="tooltip centered toHit" data-tooltip="{{ source }}">
            +{element.toHit.value}
          </div>
        </td>
        <td>
          <div class="tooltip centered damage" data-tooltip="{{ source }}">
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
