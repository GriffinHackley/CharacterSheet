function getChoices(allChoices, index) {
  if (index !== null) {
    index = "-" + index;
  } else {
    index = "";
  }
  allChoices = allChoices.map(choice => {
    let value = choice + index;
    return (
      <option value={value} key={value}>
        {choice}
      </option>
    );
  });

  allChoices.push(
    <option hidden disabled value={"default" + index} key={"default" + index}>
      --- Make a Selection ---
    </option>
  );

  return allChoices;
}

export default function Selector({
  type,
  choice,
  allChoices,
  setFunction,
  className,
  showLabel = true,
  index = null
}) {
  let label = null;
  if (showLabel) {
    label = (
      <label htmlFor={type + "Choice"}>
        {type}:{" "}
      </label>
    );
  }

  let currentValue = choice;

  if (index !== null) {
    currentValue = currentValue + "-" + index;
  }

  return (
    <div className={className + " selector"}>
      {label}
      <select
        name={type + "Choice"}
        id={type + "Choice"}
        value={currentValue}
        onChange={e => setFunction(e.target.value.split("-")[0])}
      >
        {getChoices(allChoices, index)}
      </select>
    </div>
  );
}
