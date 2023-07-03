import "../../../css/main/combat/Combat.css";
import AttacksAndSpellcasting from "./AttacksAndSpellcasting";
import CombatHeader from "./CombatHeader";
import Conditions from "./Conditions";
import CurrentHP from "./CurrentHP";
import DeathSaves from "./DeathSaves";
import HitDice from "./HitDice";
import Resistances from "./Resistances";
import TempHP from "./TempHP";

export default function Combat({ combatInfo }) {
  //TODO: Fix getItems()
  return (
    <section className="combatPane">
      <section className="combat">
        <CombatHeader combatInfo={combatInfo} />
        <div className="hp">
          <div className="otherHP">
            <HitDice hitDice={combatInfo.hitDice} config={combatInfo.config} />
            <DeathSaves />
            <Conditions config={combatInfo.config} />
          </div>
          <div className="currentTotalHealth">
            <CurrentHP HP={combatInfo.HP} config={combatInfo.config} />
            <TempHP config={combatInfo.config} />
            <Resistances config={combatInfo.config} />
          </div>
        </div>
      </section>
      <section className="attacksandspellcasting">
        <AttacksAndSpellcasting
          attacks={combatInfo.Attacks}
          config={combatInfo.config}
        />
      </section>
    </section>
  );
}
