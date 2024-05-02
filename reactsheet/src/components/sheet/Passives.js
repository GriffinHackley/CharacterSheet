import formatSource from "../../scripts/formatSource";
import Tooltip from "@mui/material/Tooltip";

function addPassive(passive) {
  passive.source = { Base: 10, ...passive.source };
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
      title={formatSource(passive.source)}
      key={"skill-" + passive.name}
    >
      <li className="skill">
        <div className="skillValue">
          {10 + passive.value}
        </div>
        <div className="skillName">
          {" Passive "}
          {passive.name}{" "}
        </div>
      </li>
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

  return passives;
}
