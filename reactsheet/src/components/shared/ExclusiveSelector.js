import { MenuItem, Select } from "@mui/material";

function onSelect(
  type,
  e,
  proficiencyChoices,
  setProficiencyChoices,
  setCurrentChoice,
  id
) {
  for (let i of Object.keys(proficiencyChoices)) {
    if (id in proficiencyChoices[i]) {
      delete proficiencyChoices[i][id];
    }
  }
  proficiencyChoices[type][id] = e.target.value;
  setProficiencyChoices(proficiencyChoices);
  setCurrentChoice(e.target.value);
}

export default function ExclusiveSelector({
  name,
  type,
  currentChoice,
  setCurrentChoice,
  proficiencyChoices,
  setProficiencyChoices,
  allChoices,
  index
}) {
  let id = `background-${name}-${index}`;

  //Filter out all entries that are already being used
  let filterChoices = [];
  for (const [key, entry] of Object.entries(proficiencyChoices[type])) {
    if (key !== id) {
      filterChoices.push(entry);
    }
  }

  if (proficiencyChoices[type][id] !== currentChoice) {
    proficiencyChoices[type][id] = currentChoice;
    setProficiencyChoices(structuredClone(proficiencyChoices));
  }

  if (!allChoices.includes(currentChoice)) {
    currentChoice = "default";
  }

  allChoices = allChoices.map(choice => {
    let disabled = filterChoices.includes(choice);

    return (
      <MenuItem disabled={disabled} key={id + choice} value={choice}>
        {choice}
      </MenuItem>
    );
  });

  allChoices.push(
    <MenuItem
      style={{ display: "none" }}
      disabled
      key={id + "default"}
      value={"default"}
    >
      --Make a Selection --
    </MenuItem>
  );

  return (
    <Select
      id={id}
      key={id}
      value={currentChoice}
      defaultValue={"default"}
      onChange={e =>
        onSelect(
          type,
          e,
          proficiencyChoices,
          setProficiencyChoices,
          setCurrentChoice,
          id
        )}
    >
      {allChoices}
    </Select>
  );
}
