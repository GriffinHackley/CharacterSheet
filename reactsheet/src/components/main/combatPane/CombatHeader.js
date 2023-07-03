import "../../../css/main/combat/CombatHeader.css";

export default function CombatHeader({ combatInfo }) {
  let CMD = null;
  if (combatInfo.config == "Pathfinder") {
    CMD = (
      <div className="tooltip centered CMD" data-tooltip="{ source }">
        <div className="value">
          {combatInfo.CMD.value}
        </div>
        <div className="key">CMD</div>
      </div>
    );
  }
  return (
    <div className="combatHeader">
      <div className="tooltip centered armorclass" data-tooltip="{ source }">
        <div className="value">
          {combatInfo.AC.value}
        </div>
        <div className="key">Armor Class</div>
      </div>
      {CMD}
      <div className="tooltip centered initiative" data-tooltip="{ source }">
        <div className="value">
          {combatInfo.Initiative.value}
        </div>
        <div className="key">Initiative</div>
      </div>
      <div className="tooltip centered speed" data-tooltip="{ source }">
        <div className="value">
          {combatInfo.Speed.value}
        </div>
        <div className="key">Speed</div>
      </div>
    </div>
  );
}
