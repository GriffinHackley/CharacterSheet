import { useEffect, useState } from "react";
import Selector from "../shared/Selector";
import "../../css/plan/ClassChoice.css";
import CollapsibleTab from "../shared/collapsibleTab";
import SubclassSelector from "./SubclassSelector";

function getPrevMax(selectionList, index) {
  let selection = selectionList[index].name;
  let max = 0;

  if (selection === "") {
    return max;
  }

  for (let i = 0; i < index; i++) {
    if (selectionList[i].name !== selection) {
      continue;
    }

    let level = parseInt(selectionList[i].endLevel);

    if (selectionList[i].endLevel > max) {
      max = level;
    } else if (level <= max) {
      //   throw `Selection at index ${i} has an endlevel less than the previous max`;
    }
  }
  return max;
}

function getFeatures(max, end, currentSelection, allClasses, subclassChoice) {
  let ret = [];
  for (let level = max; level <= end; level++) {
    let currentClass = currentSelection;
    if (currentSelection.includes("-")) {
      currentClass = currentClass.split("-")[0];
    }
    let arr = allClasses[currentClass]["features"][level];
    ret = ret.concat(
      arr.map(feature => {
        if (feature.name === allClasses[currentClass]["subclassName"]) {
          return (
            <SubclassSelector
              subclassName={allClasses[currentClass]["subclassName"]}
              choice={subclassChoice}
              allSubclasses={allClasses[currentClass]["allSubclasses"]}
            />
          );
        }
        return (
          <CollapsibleTab
            value={feature.name}
            name={feature.name}
            text={feature.text}
            key={feature.key + "-" + level}
          />
        );
      })
    );
  }

  return ret;
}

function getSelectionList(selectionList, name, subclass, end, index) {
  let ret = selectionList.map((selection, i) => {
    if (i === index) {
      if (name === "") {
        name = selection.name;
      }
      return {
        name: name,
        subclass: subclass,
        endLevel: end
      };
    } else {
      return {
        name: selection.name,
        subclass: selection.subclass,
        endLevel: selection.endLevel
      };
    }
  });
  return ret;
}

function getEndSelector(choice, allChoices, setEndLevel, index) {
  return (
    <Selector
      className="endLevel"
      type={"level"}
      choice={choice}
      allChoices={allChoices}
      setFunction={setEndLevel}
      showLabel={false}
      index={index}
    />
  );
}

export default function ClassChoice({
  def,
  selectionList,
  setSelectionList,
  allClasses,
  index
}) {
  let prevMax = getPrevMax(selectionList, index) + 1;
  if (def.level < prevMax) {
    throw new Error(`Invalid class selections for ${def.name}`);
  }
  const [currentSelection, setCurrentSelection] = useState(def.name);
  const [startLevel, setStartLevel] = useState(prevMax);

  const [endLevel, setEndLevel] = useState(def.endLevel);
  const [features, setFeatures] = useState([]);

  let endSelector = getEndSelector(
    prevMax > endLevel ? prevMax : endLevel,
    [...Array(21).keys()].slice(prevMax),
    setEndLevel,
    index
  );

  useEffect(
    () => {
      const newList = getSelectionList(
        selectionList,
        currentSelection,
        "",
        getPrevMax(selectionList, index) + 1,
        index
      );
      setSelectionList(newList);
    },
    [currentSelection]
  );

  useEffect(
    () => {
      const newList = getSelectionList(selectionList, "", "", endLevel, index);
      setSelectionList(newList);
    },
    [endLevel]
  );

  useEffect(
    () => {
      const newMax = getPrevMax(selectionList, index) + 1;
      setStartLevel(newMax);

      let newEnd = endLevel;
      if (newEnd < newMax) {
        newEnd = newMax;
        setEndLevel(newEnd);
      }

      endSelector = getEndSelector(
        newEnd,
        [...Array(21).keys()].slice(newMax),
        setEndLevel,
        index
      );

      if (currentSelection !== "default") {
        setFeatures(
          getFeatures(
            newMax,
            newEnd,
            currentSelection,
            allClasses,
            "Artificer Specialist"
          )
        );
      }
    },
    [selectionList]
  );

  let levelOne = [];
  if (startLevel === 1 && currentSelection !== "default") {
    let starting = allClasses[currentSelection]["starting"];

    if (starting["Armor"] !== "None") {
      levelOne.push(
        <div key="startingArmor">
          Armor: {starting["Armor"]}
        </div>
      );
    }

    if (starting["Weapons"] !== "None") {
      <div key="startingWeapons">
        Weapons: {starting["Weapons"]}
      </div>;
    }

    if (starting["Tools"].defaults[0] !== "None") {
      levelOne.push(
        <div key="startingTools">
          Tools: {starting["Tools"].defaults.join(", ")}
        </div>
      );
    }
  }

  return (
    <div className="classChoice">
      <div className="classHeader">
        <Selector
          className={"classSelector"}
          type={"class"}
          choice={currentSelection}
          allChoices={Object.keys(allClasses)}
          setFunction={setCurrentSelection}
          showLabel={false}
          index={index}
        />
        <div className="levels">
          {startLevel}
          {"--->"}
          {endSelector}
        </div>
      </div>
      {levelOne}
      {features}
    </div>
  );
}
