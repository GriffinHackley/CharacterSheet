import formatSource from "../../../scripts/formatSource";
import "../../../css/sheet/combat/AttacksAndSpellcasting.css";
import {
  Table,
  TableBody,
  TableHead,
  TableRow,
  TableCell,
  Paper
} from "@mui/material";

export default function AttacksAndSpellcasting({ attacks, config }) {
  let rows = [];
  let critRangeHeader = null;
  let critRangeBody = null;
  let includeCrit = false;

  if (config == "Pathfinder") {
    includeCrit = true;
  }

  if (includeCrit) {
    critRangeHeader = <TableHead>Crit Range</TableHead>;
  }

  attacks.forEach(element => {
    if (includeCrit) {
      critRangeBody = (
        <TableCell>
          <div className="critRange">
            {element.critRange}/x{element.criTableCellamage}
          </div>
        </TableCell>
      );
    }
    rows.push(
      <TableRow key={"attack-" + element.name}>
        <TableCell>
          <div className="atk">
            {element.name}
          </div>
        </TableCell>
        {critRangeBody}
        <TableCell>
          <div
            className="tooltip centered toHit"
            data-tooltip={formatSource(element.toHit.source)}
          >
            +{element.toHit.value}
          </div>
        </TableCell>
        <TableCell>
          <div
            className="tooltip centered damage"
            data-tooltip={formatSource(element.damage.source)}
          >
            {element.damage.value}
          </div>
        </TableCell>
      </TableRow>
    );
  });

  return (
    <Paper className="attacksAndSpellcasting">
      <label>Attacks & Spellcasting</label>
      <Table style={{ height: "100%" }}>
        <TableHead className="tableHeader">
          <TableRow>
            <TableCell>Name</TableCell>
            {critRangeHeader}
            <TableCell>Atk Bonus</TableCell>
            <TableCell>Damage/Type</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows}
        </TableBody>
      </Table>
    </Paper>
  );
}
