import "../css/Combat.css";
import AttacksAndSpellcasting from "./AttacksAndSpellcasting";
import CombatHeader from "./CombatHeader";
import Conditions from "./Conditions";
import CurrentHP from "./CurrentHP";
import DeathSaves from "./DeathSaves";
import HitDice from "./HitDice";
import Resistances from "./Resistances";
import TempHP from "./TempHP";

export default function Combat({ combatInfo, config }) {
  //TODO: Fix getItems()
  return (
    <section class="combatPane">
      <section class="combat">
        <CombatHeader combatInfo={combatInfo} config={config} />
        <div class="hp">
          <div class="otherHP">
            <HitDice hitDice={combatInfo.hitDice} />
            <DeathSaves />
            <Conditions />
          </div>
          <div class="currentTotalHealth">
            <CurrentHP HP={combatInfo.HP} />
            <TempHP />
            <Resistances />
          </div>
        </div>
      </section>
      <section class="attacksandspellcasting">
        <AttacksAndSpellcasting attacks={combatInfo.Attacks} config={config}/>
      </section>
    </section>
  );
}
