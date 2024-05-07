import { useTheme } from "@emotion/react";
import "../../../css/sheet/combat/Combat.css";

import CombatHeader from "./CombatHeader";
import Conditions from "./Conditions";
import CurrentHP from "./CurrentHP";
import DeathSaves from "./DeathSaves";
import HitDice from "./HitDice";
import Resistances from "./Resistances";
import TempHP from "./TempHP";
import { Paper } from "@mui/material";

export default function Combat({ combatInfo }) {
  //TODO: Fix getCheckboxValues()
  return (
    <Paper className="combat">
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
    </Paper>
  );
}
