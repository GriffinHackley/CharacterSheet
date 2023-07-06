import "../../../css/main/combat/CombatHeader.css";
import formatSource from "../../../scripts/formatSource";

export default function CombatHeader({ combatInfo }) {
  let headerItems = ["Armor Class", "Initiative", "Speed"];

  if (combatInfo.config == "Pathfinder") {
    headerItems.push("CMD");
  }

  let content = [];
  headerItems.forEach(item => {
    let data = combatInfo[item];

    content.push(
      <div
        className="tooltip centered headerItem"
        data-tooltip={formatSource(data.source)}
      >
        <div className="value">
          {data.value}
        </div>
        <div className="key">
          {item}
        </div>
      </div>
    );
  });

  return (
    <div className="combatHeader">
      {content}
    </div>
  );
}
