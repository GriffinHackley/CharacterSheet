import "../css/CombatHeader.css";

export default function CombatHeader({ combatInfo, config }) {
  let CMD = null;
  if (config == "Pathfinder") {
    CMD = (
      <div class="tooltip centered CMD" data-tooltip="{ source }">
        <div class="value">
          {combatInfo.CMD.value}
        </div>
        <div class="key">CMD</div>
      </div>
    );
  }
  return (
    <div class="combatHeader">
      <div class="tooltip centered armorclass" data-tooltip="{ source }">
        <div class="value">
          {combatInfo.AC.value}
        </div>
        <div class="key">Armor Class</div>
      </div>
      {CMD}
      <div class="tooltip centered initiative" data-tooltip="{ source }">
        <div class="value">
          {combatInfo.Initiative.value}
        </div>
        <div class="key">Initiative</div>
      </div>
      <div class="tooltip centered speed" data-tooltip="{ source }">
        <div class="value">
          {combatInfo.Speed.value}
        </div>
        <div class="key">Speed</div>
      </div>
    </div>
  );
}
