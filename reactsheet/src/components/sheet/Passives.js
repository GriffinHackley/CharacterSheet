import { Paper } from "@mui/material";
import formatSource from "../../utils/formatSource";
import Tooltip from "@mui/material/Tooltip";

function addPassive(passive) {
  return (
    <Tooltip
      className="passive"
      componentsProps={{
        tooltip: {
          sx: {
            bgcolor: "common.black",
            "& .MuiTooltip-arrow": {
              color: "common.black"
            }
          }
        }
      }}
      title={formatSource({ Base: 10, ...passive.source })}
      key={"skill-" + passive.name}
    >
      <div className="skill" style={{ display: "flex", flexDirection: "row" }}>
        <div className="skillValue">
          {10 + passive.value}
        </div>
        <div className="skillName">
          {" Passive "}
          {passive.name}{" "}
        </div>
      </div>
    </Tooltip>
  );
}

export default function Passives({ skillsInfo }) {
  let passives = skillsInfo
    .filter(skill =>
      ["Perception", "Insight", "Investigation"].includes(skill.name)
    )
    .sort((a, b) => b.value - a.value)
    .map(passive => addPassive(passive));

  return (
    <Paper>
      {passives}
    </Paper>
  );
}
