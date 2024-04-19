import { useState, useEffect } from "react";
import ClassChoice from "./ClassChoice";

export default function Classes({ classes }) {
  const [classChoiceList, setClassChoiceList] = useState([]);
  const [selectionList, setSelectionList] = useState([
    {
      name: "",
      endLevel: -1
    }
  ]);

  useEffect(
    () => {
      let choiceList = selectionList.map((selection, index) => {
        return (
          <ClassChoice
            selectionList={selectionList}
            setSelectionList={setSelectionList}
            allClasses={classes.all}
            index={index}
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
          setSelectionList([...selectionList, { name: "", endLevel: -1 }])}
      >
        Add Class
      </button>
      {classChoiceList}
    </div>
  );
}
