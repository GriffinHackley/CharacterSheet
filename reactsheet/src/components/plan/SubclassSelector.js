import { useState } from "react";
import { MenuItem, Select, InputLabel, FormControl } from "@mui/material";

function getSelector(
  className,
  subclassName,
  allSubclasses,
  choice,
  setChoice
) {
  const handleChange = event => {
    console.log(event.target);

    setChoice(event.target.value);
  };
  let menuItems = allSubclasses.map(subclass => {
    return (
      <MenuItem key={`${subclass}-menuItem`} value={subclass}>
        {subclass}
      </MenuItem>
    );
  });

  return (
    <FormControl sx={{ minWidth: 300 }} autoWidth>
      <InputLabel id={`${className}-subclass-selector`}>
        {subclassName}
      </InputLabel>
      <Select
        labelId={`${className}-subclass-selector`}
        id={`${className}-subclass-selector`}
        value={choice}
        defaultValue={""}
        label={subclassName}
        onChange={handleChange}
        autoWidth
      >
        {menuItems}
      </Select>
    </FormControl>
  );
}

export default function SubclassSelector({
  className,
  subclassName,
  subclassChoice,
  allSubclasses
}) {
  let value;
  if (subclassChoice) {
    value = subclassChoice;
  } else {
    value = "";
  }
  const [choice, setChoice] = useState(value);

  return (
    <div>
      {getSelector(className, subclassName, allSubclasses, choice, setChoice)}
    </div>
  );
}
