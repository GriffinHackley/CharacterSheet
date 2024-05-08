import { useState, useEffect } from "react";
import ClassChoice from "./ClassChoice";

export default function Classes({ classes }) {
  const [classChoiceList, setClassChoiceList] = useState([]);

  let selections = [];
  for (const [name, value] of Object.entries(classes.choice)) {
    selections.push({ name: name, endLevel: value.level });
  }

  const [selectionList, setSelectionList] = useState(selections);

  useEffect(
    () => {
      const choices = Object.keys(classes.choice);
      let choiceList = selectionList.map((selection, index) => {
        // let def = "default";
        // let def = choices[index];
        return (
          <ClassChoice
            def={selection}
            selectionList={selectionList}
            setSelectionList={setSelectionList}
            allClasses={classes.all}
            index={index}
            key={"classChoice-" + index}
          />
        );
      });
      setClassChoiceList(choiceList);
    },
    [selectionList]
  );

  return (
    <div>
      <h3>Classes</h3>
      <button
        onClick={() =>
          setSelectionList([
            ...selectionList,
            { name: "default", endLevel: -1 }
          ])}
      >
        Add Class
      </button>
      {classChoiceList}
    </div>
  );
}
