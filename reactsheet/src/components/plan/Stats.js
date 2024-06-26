import { TableBody } from "@mui/material";

const AbilityScores = Object.freeze({
  Strength: 0,
  Dexterity: 1,
  Constitution: 2,
  Intelligence: 3,
  Wisdom: 4,
  Charisma: 5
});

function getStatRow(stat, baseValues, racial, asi) {
  let arrPos = AbilityScores[stat];
  let value =
    Number(baseValues[arrPos]) + Number(racial[arrPos]) + Number(asi[arrPos]);
  return (
    <tr>
      <th>
        {stat}
      </th>
      <td>
        {Math.floor((value - 10) / 2)}
      </td>
      <td>
        {value}
      </td>
      <td>
        {baseValues[arrPos]}
      </td>
      <td>
        {racial[arrPos]}
      </td>
      <td>
        {asi[arrPos]}
      </td>
    </tr>
  );
}

function getASI(feats) {
  let asi = Array(6).fill(0);
  for (let feat in feats) {
    if (!feats[feat].options?.ASI) {
      continue;
    }
    for (let [stat, value] of Object.entries(feats[feat].options.ASI)) {
      stat = AbilityScores[stat];
      asi[stat] += Number(value);
    }
  }
  return asi;
}

export default function Stats({ stats }) {
  let baseValues = stats.base.split(",");
  let asi = getASI(stats.feats);
  let racial = Array(6).fill(0);
  for (let stat in stats.racial) {
    racial[AbilityScores[stat]] += stats.racial[stat];
  }

  return (
    <div>
      <h3>Stats</h3>
      <table>
        <thead>
          <tr>
            <th>Stat</th>
            <th>Bonus</th>
            <th>Value</th>
            <th>Base</th>
            <th>Racial</th>
            <th>ASI</th>
          </tr>
        </thead>
        <tbody>
          {getStatRow("Strength", baseValues, racial, asi)}
          {getStatRow("Dexterity", baseValues, racial, asi)}
          {getStatRow("Constitution", baseValues, racial, asi)}
          {getStatRow("Intelligence", baseValues, racial, asi)}
          {getStatRow("Wisdom", baseValues, racial, asi)}
          {getStatRow("Charisma", baseValues, racial, asi)}
        </tbody>
      </table>
    </div>
  );
}
